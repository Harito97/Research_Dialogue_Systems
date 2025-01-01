import json
import re
import numpy as np
import tensorflow as tf
import os
from datasets import load_dataset
import tensorflow as tf
import gc  # Import garbage collector
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from transformers import BertTokenizer, TFBertModel
# from transformers import AutoTokenizer, TFAutoModel
from sklearn.utils import class_weight
from sklearn.preprocessing import MultiLabelBinarizer

class MultiWOZ_2_2:
    def __init__(self):
        self.bio_labels = [
            "O",
            "B-address",
            "B-area",
            "B-arriveby",
            "B-bookday",
            "B-bookpeople",
            "B-bookstay",
            "B-booktime",
            "B-choice",
            "B-day",
            "B-department",
            "B-departure",
            "B-destination",
            "B-duration",
            "B-entrancefee",
            "B-food",
            "B-leaveat",
            "B-name",
            "B-openhours",
            "B-phone",
            "B-postcode",
            "B-price",
            "B-pricerange",
            "B-ref",
            "B-stars",
            "B-trainid",
            "B-type",
            "I-address",
            "I-area",
            "I-arriveby",
            "I-bookday",
            "I-bookpeople",
            "I-bookstay",
            "I-booktime",
            "I-choice",
            "I-day",
            "I-department",
            "I-departure",
            "I-destination",
            "I-duration",
            "I-entrancefee",
            "I-food",
            "I-leaveat",
            "I-name",
            "I-openhours",
            "I-phone",
            "I-postcode",
            "I-price",
            "I-pricerange",
            "I-ref",
            "I-stars",
            "I-trainid",
            "I-type",
        ]

        self.unique_act_types = [
            "None",
            "Attraction-Inform",
            "Attraction-NoOffer",
            "Attraction-Recommend",
            "Attraction-Select",
            "Booking-Book",
            "Booking-Inform",
            "Booking-NoBook",
            "Hospital-Inform",
            "Hotel-Inform",
            "Hotel-NoOffer",
            "Hotel-Recommend",
            "Hotel-Select",
            "Police-Inform",
            "Restaurant-Inform",
            "Restaurant-NoOffer",
            "Restaurant-Recommend",
            "Restaurant-Select",
            "Taxi-Inform",
            "Train-Inform",
            "Train-NoOffer",
            "Train-OfferBook",
            "Train-OfferBooked",
            "Train-Select",
        ]
        # self.guide()

    def guide(self):
        print(
            """
            This class is for preprocessing the raw data of MultiWOZ 2.4 dataset.

            You can use the following methods step by step:
            - self.download_data(data_path:str='./dataset_multiwoz.json')
            - self.setup_hyperparameters(max_seq_length:int=50, embedding_dim:int=128)
            - self.get_raw_data(data_path:str='dataset_multiwoz.json')
            - self.get_clean_data_and_weight_classes()
            """
        )

    def download_data(self, data_path: str = "./dataset_multiwoz.json"):
        dataset = load_dataset("pfb30/multi_woz_v22", trust_remote_code=True)
        print("Save dataset to disk")
        dataset_dict = {split: dataset[split].to_dict() for split in dataset}
        with open(data_path, 'w') as f:
            json.dump(dataset_dict, f)

    def __load_json(self, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data

    def __create_bio_labels(self, utterance, spans, slot_names):
        # Tách câu thành các token
        tokens = re.findall(r'\w+|[^\w\s]', utterance, re.UNICODE)

        # Khởi tạo nhãn BIO cho các token
        bio_labels = ['O'] * len(tokens)

        # Duyệt qua từng span
        for start, end, slot_name in zip(spans['span_start'], spans['span_end'], slot_names):
            # Xác định vị trí token đầu tiên và cuối cùng của span
            token_start = len(re.findall(r'\w+|[^\w\s]', utterance[:start]))
            token_end = len(re.findall(r'\w+|[^\w\s]', utterance[:end]))

            # Gán nhãn BIO cho các token trong span
            if token_start < len(tokens):
                bio_labels[token_start] = f'B-{slot_name}'
            for i in range(token_start + 1, min(token_end, len(tokens))):
                bio_labels[i] = f'I-{slot_name}'

        return tokens, bio_labels

    def __get_raw_data1(self, dataset):
        data_train = []
        data_validation = []
        data_test = []

        for index_dialogue in range(len(dataset["train"]["dialogue_id"])):
            dialogue_id = dataset["train"]["dialogue_id"][index_dialogue]
            for index_turn in range(len(dataset["train"]["turns"][index_dialogue]['turn_id'])):
                record = [None] * 4
                record[0] = dialogue_id
                record[1] = dataset["train"]["turns"][index_dialogue]["turn_id"][index_turn]
                record[2] = dataset["train"]["turns"][index_dialogue]["utterance"][index_turn]
                record[3] = dataset["train"]["turns"][index_dialogue]["dialogue_acts"][index_turn]["span_info"]
                data_train.append(record)

        for index_dialogue in range(len(dataset["validation"]["dialogue_id"])):
            dialogue_id = dataset["validation"]["dialogue_id"][index_dialogue]
            for index_turn in range(len(dataset["validation"]["turns"][index_dialogue]['turn_id'])):
                record = [None] * 4
                record[0] = dialogue_id
                record[1] = dataset["validation"]["turns"][index_dialogue]["turn_id"][index_turn]
                record[2] = dataset["validation"]["turns"][index_dialogue]["utterance"][index_turn]
                record[3] = dataset["validation"]["turns"][index_dialogue]["dialogue_acts"][index_turn]["span_info"]
                data_validation.append(record)

        for index_dialogue in range(len(dataset["test"]["dialogue_id"])):
            dialogue_id = dataset["test"]["dialogue_id"][index_dialogue]
            for index_turn in range(len(dataset["test"]["turns"][index_dialogue]['turn_id'])):
                record = [None] * 4
                record[0] = dialogue_id
                record[1] = dataset["test"]["turns"][index_dialogue]["turn_id"][index_turn]
                record[2] = dataset["test"]["turns"][index_dialogue]["utterance"][index_turn]
                record[3] = dataset["test"]["turns"][index_dialogue]["dialogue_acts"][index_turn]["span_info"]
                data_test.append(record)

        return data_train, data_validation, data_test


    def __get_raw_data2(self, data):
        # data is data_train, data_validation, or data_test
        X_token_classification = []
        y_token_classification = []
        y_act = []

        # Tạo từ điển ánh xạ nhãn BIO thành chỉ số
        label_to_id = {label: idx for idx, label in enumerate(self.bio_labels)}

        # Tạo từ điển ánh xạ nhãn act_type thành chỉ số
        act_type_to_id = {act_type: idx for idx, act_type in enumerate(self.unique_act_types)}

        # Lặp qua các dữ liệu train
        for item in data:
            # Câu thoại (utterance)
            utterance = item[2]  # Câu trong vị trí thứ 2

            # Các nhãn act_type và act_slot_name từ `dialogue_acts`
            dialogue_acts = item[3]  # Nhận phần dialogue_acts
            span_start = dialogue_acts["span_start"]
            span_end = dialogue_acts["span_end"]
            act_slot_name = dialogue_acts["act_slot_name"]
            act_type = dialogue_acts["act_type"]  # Nhãn act_type

            # Gán nhãn BIO cho các token trong câu
            tokens, bio_labels_for_tokens = self.__create_bio_labels(
                utterance, {"span_start": span_start, "span_end": span_end}, act_slot_name
            )

            # Lưu các token và nhãn BIO
            X_token_classification.append(tokens)

            # Chuyển nhãn BIO thành chỉ số
            y_token_classification.append(
                [label_to_id[label] for label in bio_labels_for_tokens]
            )

            # Khởi tạo ma trận one-hot cho các hành động
            act_type_one_hot = np.zeros(len(self.unique_act_types))

            # Nếu có nhiều hành động, đặt giá trị 1 cho những hành động xuất hiện trong `act_type`
            for act in act_type:
                act_type_id = act_type_to_id[act]
                act_type_one_hot[act_type_id] = 1  # Gán 1 cho các vị trí của các hành động xuất hiện

            # Append vào y_act
            y_act.append(act_type_one_hot)

        return X_token_classification, y_token_classification, y_act

    def setup_hyperparameters(self, max_seq_length:int=20, embedding_dim:int=128):
        self.MAX_SEQUENCE_LENGTH = max_seq_length
        self.EMBEDDING_DIM = embedding_dim
        self.NUM_CLASSES_ACT = len(self.unique_act_types)
        self.NUM_CLASSES_SLOT = len(self.bio_labels)

    def get_raw_data(self, data_path:str='dataset_multiwoz.json'):
        dataset = self.__load_json(data_path)
        data_train, data_validation, data_test = self.__get_raw_data1(dataset)
        self.X_train, self.y_train, self.y_train_act = self.__get_raw_data2(data_train)
        self.X_validation, self.y_validation, self.y_validation_act = self.__get_raw_data2(data_validation)
        self.X_test, self.y_test, self.y_test_act = self.__get_raw_data2(data_test)

    def setup_embedding(self):
        # # Sử dụng BERT embedding (với `bert-base-uncased`)
        # bert_model_name = 'bert-base-uncased'
        # Sử dụng TinyBERT
        bert_model_name = "huawei-noah/TinyBERT_General_4L_312D"
        try:
            # self.bert_tokenizer = AutoTokenizer.from_pretrained(bert_model_name)
            # self.bert_model = TFAutoModel.from_pretrained(bert_model_name, from_pt=True)
            self.bert_tokenizer = BertTokenizer.from_pretrained(bert_model_name)
            self.bert_model = TFBertModel.from_pretrained(bert_model_name, from_pt=True)
            # In thông tin model (thay vì summary, vì summary không hoạt động tốt với TFAutoModel)
            print(f"Model {bert_model_name} loaded successfully.")
            print(f"Model config: {self.bert_model.config}") # In cấu hình model
            print(f"Hidden size: {self.bert_model.config.hidden_size}")
            print(f"Number of parameters: {self.bert_model.count_params()}")
            print("BERT embedding setup complete.")

        except Exception as e:
            print(f"Error loading model {bert_model_name}: {e}")
            raise  # Re-raise exception after printing for debugging

    def __create_bert_embedding(self, texts, batch_size=32):
        """Tạo embedding BERT với batch để tránh lỗi OOM."""

        # def preprocess_text(text_list):
        #     """Trích xuất câu từ list chứa cấu trúc lồng nhau."""
        #     sentences = []
        #     for item in text_list:
        #         if isinstance(item, str):
        #             sentences.append(item)
        #         elif isinstance(item, list):
        #             print(item)
        #             sentences.extend(preprocess_text(item))
        #             return sentences

        # # Tiền xử lý dữ liệu để đảm bảo texts là list các string
        # texts = preprocess_text(texts)
        # texts = [str(text).strip() for text in texts if str(text).strip()] # Chuyển sang string, loại bỏ khoảng trắng và string rỗng

        input_ids = []
        attention_masks = []

        print("Tokenizing texts...")
        print(f"Type of texts after preprocessing: {type(texts)}") # Kiểm tra type sau xử lý
        for i, text in enumerate(texts):
            print(f"Tokenizing text {i+1}/{len(texts)}: {text}") # In ra text đang được token hóa
            encoded_dict = self.bert_tokenizer.encode_plus(
                text,
                add_special_tokens=True,
                max_length=self.MAX_SEQUENCE_LENGTH,
                padding='max_length',
                truncation=True,
                return_attention_mask=True,
                return_tensors='tf'
            )
            input_ids.append(encoded_dict['input_ids'][0])
            attention_masks.append(encoded_dict['attention_mask'][0])

        input_ids = tf.stack(input_ids)
        attention_masks = tf.stack(attention_masks)

        embeddings = []
        print("Creating BERT embeddings...")
        num_batches = (len(texts) + batch_size - 1) // batch_size # Tính số batch
        for i in range(num_batches):
            start = i * batch_size
            end = min((i + 1) * batch_size, len(texts))
            print(f"Processing batch {i + 1}/{num_batches}: {start}-{end}")
            batch_input_ids = input_ids[start:end]
            batch_attention_masks = attention_masks[start:end]

            batch_embeddings = self.bert_model(batch_input_ids, attention_mask=batch_attention_masks)[0]
            embeddings.append(batch_embeddings)

        embeddings = tf.concat(embeddings, axis=0)
        return embeddings

    def get_clean_data_and_weight_classes(self):
        if not hasattr(self, 'X_train'):
            raise ValueError("Cần gọi get_raw_data trước khi gọi get_clean_data_and_weight_classes")

        def process_data(X, y, y_act):
           X_bert = self.__create_bert_embedding(X)
           del X  # Xóa X ngay sau khi tạo embedding
           gc.collect() # Gọi garbage collector ngay lập tức
           y_padded = pad_sequences(y, maxlen=self.MAX_SEQUENCE_LENGTH, padding='post')
           del y
           gc.collect()
           y_padded_one_hot = np.array([to_categorical(y_i, num_classes=self.NUM_CLASSES_SLOT) for y_i in y_padded])
           del y_padded
           gc.collect()
           y_act_one_hot = np.array(y_act)
           del y_act
           gc.collect()
           return X_bert, y_padded_one_hot, y_act_one_hot

        self.X_train_bert, self.y_train_padded_one_hot, self.y_act_one_hot = process_data(self.X_train, self.y_train, self.y_train_act)
        self.X_val_bert, self.y_val_padded_one_hot, self.y_act_val_one_hot = process_data(self.X_validation, self.y_validation, self.y_validation_act)
        self.X_test_bert, self.y_test_padded_one_hot, self.y_act_test_one_hot = process_data(self.X_test, self.y_test, self.y_test_act)

        # Tính class weights (chỉ cần tính trên tập train)
        slot_class_weights = class_weight.compute_class_weight('balanced', classes=np.unique(self.y_train_padded_one_hot.flatten()), y=self.y_train_padded_one_hot.flatten())
        self.slot_class_weights_dict = dict(enumerate(slot_class_weights))

        mlb = MultiLabelBinarizer()
        y_act_mlb = mlb.fit_transform([np.where(r==1)[0] for r in self.y_act_one_hot])
        act_class_weights = class_weight.compute_class_weight('balanced', classes=np.unique(y_act_mlb.flatten()), y=y_act_mlb.flatten())
        self.act_class_weights_dict = dict(enumerate(act_class_weights))
        print("Đã xử lý dữ liệu và tính class weights.")

    def save_data(self, save_path: str = './data/multiwoz_2_2_processed_data.json'):
        try:
            print(f"Saving data to {save_path}")
            os.makedirs(os.path.dirname(save_path), exist_ok=True) # Tạo thư mục nếu chưa tồn tại
            data_to_save = {
                'X_train_bert': self.X_train_bert.numpy().tolist(),  # Convert to list for JSON serialization
                'X_val_bert': self.X_val_bert.numpy().tolist(),
                'X_test_bert': self.X_test_bert.numpy().tolist(),
                'y_train_padded_one_hot': self.y_train_padded_one_hot.tolist(),
                'y_val_padded_one_hot': self.y_val_padded_one_hot.tolist(),
                'y_test_padded_one_hot': self.y_test_padded_one_hot.tolist(),
                'y_act_one_hot': self.y_act_one_hot.tolist(),
                'y_act_val_one_hot': self.y_act_val_one_hot.tolist(),
                'y_act_test_one_hot': self.y_act_test_one_hot.tolist(),
                'slot_class_weights_dict': self.slot_class_weights_dict,
                'act_class_weights_dict': self.act_class_weights_dict,
                'MAX_SEQUENCE_LENGTH': self.MAX_SEQUENCE_LENGTH,
                'EMBEDDING_DIM': self.EMBEDDING_DIM,
                'NUM_CLASSES_ACT': self.NUM_CLASSES_ACT,
                'NUM_CLASSES_SLOT': self.NUM_CLASSES_SLOT,
                'bio_labels': self.bio_labels,
                'unique_act_types': self.unique_act_types
            }
            with open(save_path, 'w') as f:
                json.dump(data_to_save, f, indent=4) # Thêm indent để dễ đọc
            print(f"Data saved to {save_path}")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self, load_path: str = './data/multiwmultiwoz_2_2_processed_data.json', load_train: bool = False, load_val: bool = False, load_test: bool = False):
        try:
            print(f"Loading data from {load_path}")
            with open(load_path, 'r') as f:
                data_loaded = json.load(f)

            if load_train:
                self.X_train_bert = tf.constant(data_loaded['X_train_bert'], dtype=tf.float32) # Convert back to tensors, specify dtype
                self.y_train_padded_one_hot = np.array(data_loaded['y_train_padded_one_hot'])
                self.y_act_one_hot = np.array(data_loaded['y_act_one_hot'])
            if load_val:
                self.X_val_bert = tf.constant(data_loaded['X_val_bert'], dtype=tf.float32)
                self.y_val_padded_one_hot = np.array(data_loaded['y_val_padded_one_hot'])
                self.y_act_val_one_hot = np.array(data_loaded['y_act_val_one_hot'])
            if load_test:
                self.X_test_bert = tf.constant(data_loaded['X_test_bert'], dtype=tf.float32)
                self.y_test_padded_one_hot = np.array(data_loaded['y_test_padded_one_hot'])
                self.y_act_test_one_hot = np.array(data_loaded['y_act_test_one_hot'])

            self.slot_class_weights_dict = data_loaded['slot_class_weights_dict']
            self.act_class_weights_dict = data_loaded['act_class_weights_dict']
            self.MAX_SEQUENCE_LENGTH = data_loaded['MAX_SEQUENCE_LENGTH']
            self.EMBEDDING_DIM = data_loaded['EMBEDDING_DIM']
            self.NUM_CLASSES_ACT = data_loaded['NUM_CLASSES_ACT']
            self.NUM_CLASSES_SLOT = data_loaded['NUM_CLASSES_SLOT']
            self.bio_labels = data_loaded['bio_labels']
            self.unique_act_types = data_loaded['unique_act_types']

            print(f"Data loaded from {load_path}")
        except FileNotFoundError:
            print(f"Error: File not found at {load_path}. Please run process_and_save() first.")
            return False # Trả về False để báo hiệu lỗi
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {load_path}")
            return False
        except KeyError as e:
            print(f"Error: Missing key {e} in loaded data.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred during loading: {e}")
            return False
        return True # Trả về True nếu load thành công

    def process_and_save(self, data_path:str='./data/dataset_multiwoz_2_2.json', save_path: str = './data/multiwoz_2_2_processed_data.json'):
        print("Setting up hyperparameters...")
        self.setup_hyperparameters()
        print("Getting raw data...")
        self.get_raw_data(data_path)
        print("Setting up BERT embedding...")
        self.setup_embedding()
        print("Getting clean data and weight classes...")
        self.get_clean_data_and_weight_classes()
        print("Saving clean data...")
        self.save_data(save_path)

    def preprocess_text(self, text):
        encoded_dict = self.bert_tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=self.MAX_SEQUENCE_LENGTH,
            padding='max_length',
            truncation=True,
            return_attention_mask=False,  # No need to return attention mask in inference
            return_tensors='tf'
        )
        return encoded_dict['input_ids'][0]

    def decode_predictions(self, predictions):
        predicted_indexes = np.argmax(predictions, axis=-1)
        decoded_labels = [self.bio_labels[i] for i in predicted_indexes]
        return decoded_labels

    def decode_act_predictions(self, predictions):
        predicted_indexes = np.where(predictions > 0.5)[0]  # Threshold at 0.5 for sigmoid
        decoded_labels = [self.unique_act_types[i] for i in predicted_indexes]
        return decoded_labels

# ----------------------------

# def split_train_dev_test(
#     data_dir: str = "./data/raw/MULTIWOZ2.4",
#     des_dir: str = "./data/processed/MULTIWOZ2.4",
# ):
#     """
#     This code will split the raw data in `../data/MULTIWOZ2.4/` to train, dev, and test data.
#     that downloaded from `https://github.com/smartyfh/MultiWOZ2.4`.

#     This code also refer to the original code of MultiWOZ 2.4 dataset,
#     that can be found in `https://github.com/smartyfh/MultiWOZ2.4/blob/main/split.py`.

#     This code only use for MULTIWOZ2.4 dataset.
#     """
#     import json
#     import os
#     import re

#     testListFile = []
#     fin = open(os.path.join(data_dir, "testListFile.json"), "r")
#     for line in fin:
#         testListFile.append(line[:-1])
#     fin.close()

#     valListFile = []
#     fin = open(os.path.join(data_dir, "valListFile.json"), "r")
#     for line in fin:
#         valListFile.append(line[:-1])
#     fin.close()

#     data = json.load(open(os.path.join(data_dir, "data.json")))

#     test_dials = {}
#     val_dials = {}
#     train_dials = {}
#     count_train, count_val, count_test = 0, 0, 0
#     for dialogue_name in data:
#         if dialogue_name in testListFile:
#             test_dials[dialogue_name] = data[dialogue_name]
#             count_test += 1
#         elif dialogue_name in valListFile:
#             val_dials[dialogue_name] = data[dialogue_name]
#             count_val += 1
#         else:
#             train_dials[dialogue_name] = data[dialogue_name]
#             count_train += 1

#     print(
#         "# of dialogues: Train {}, Val {}, Test {}".format(
#             count_train, count_val, count_test
#         )
#     )

#     # save all dialogues
#     with open(os.path.join(des_dir, "dev_dials.json"), "w") as f:
#         json.dump(val_dials, f, indent=4)

#     with open(os.path.join(des_dir, "test_dials.json"), "w") as f:
#         json.dump(test_dials, f, indent=4)

#     with open(os.path.join(des_dir, "train_dials.json"), "w") as f:
#         json.dump(train_dials, f, indent=4)
