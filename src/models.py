import json
import re
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Embedding, LSTM, Bidirectional, Dense, TimeDistributed, GlobalAveragePooling1D, Input, Dropout
from tensorflow.keras.models import Model, load_model # Import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import classification_report, multilabel_confusion_matrix
from transformers import logging
logging.set_verbosity_error()
from transformers import BertTokenizer, TFBertModel
import os
from tensorflow.keras.layers import Input, Lambda

class S2_Model:
    def __init__(self, max_sequence_length, num_classes_slot, num_classes_act, bert_model, embedding_dim:int=128, dropout_rate:float=0.2):
        # Model (Sử dụng BERT embedding và dropout)
        input_seq = Input(shape=(max_sequence_length,), dtype="int32")
        # embedding = bert_model(input_seq)[0]
        # Sử dụng Lambda layer để ép kiểu
        input_seq_casted = Lambda(lambda x: tf.cast(x, dtype=tf.int32))(input_seq)

        embedding = bert_model(input_seq_casted)[0]
        bilstm = Bidirectional(LSTM(embedding_dim, return_sequences=True))(embedding) # Tăng số units
        bilstm = Dropout(dropout_rate)(bilstm) # Thêm dropout

        slot_output = TimeDistributed(Dense(num_classes_slot, activation="softmax"), name="slot_output")(bilstm)

        sentence_representation = GlobalAveragePooling1D()(bilstm)
        sentence_representation = Dropout(dropout_rate)(sentence_representation) # Thêm dropout
        action_output = Dense(num_classes_act, activation="sigmoid", name="action_output")(sentence_representation) # Sigmoid cho multi-label

        self.model = Model(inputs=input_seq, outputs=[slot_output, action_output])

    def compile_summary(self):
        # Compile model với class weights
        self.model.compile(
            optimizer="adam",
            loss={
                "slot_output": "categorical_crossentropy",
                "action_output": "binary_crossentropy", # Binary crossentropy cho multi-label
            },
            loss_weights={
                "slot_output": 1.0,
                "action_output": 1.0
            },
            metrics={"slot_output": ["accuracy"], "action_output": ["binary_accuracy"]}, # Binary accuracy cho multi-label
        )

        print(self.model.summary())

    def train(self, X_train_bert, y_train_padded_one_hot, y_act_one_hot, X_val_bert, y_val_padded_one_hot, y_act_val_one_hot, slot_class_weights_dict, act_class_weights_dict):
        # Huấn luyện mô hình
        history = self.model.fit(
            X_train_bert,
            [y_train_padded_one_hot, y_act_one_hot],
            validation_data=(X_val_bert, [y_val_padded_one_hot, y_act_val_one_hot]),
            epochs=20, # Tăng số epochs
            batch_size=32,
            class_weight=[slot_class_weights_dict, act_class_weights_dict]
        )
        return history

    def predict(self, X):
        return self.model.predict(X)

    def evaluate(self, X_test_bert, y_test_padded_one_hot, y_test_act_one_hot):
        # Đánh giá và in report (chỉnh sửa cho multi-label)
        y_pred_slot, y_pred_action = self.model.predict(X_test_bert)

        y_pred_slot_labels = np.argmax(y_pred_slot, axis=-1)
        y_true_slot_labels = np.argmax(y_test_padded_one_hot, axis=-1)

        y_pred_slot_flatten = y_pred_slot_labels.reshape(-1)
        y_true_slot_flatten = y_true_slot_labels.reshape(-1)

        print("Slot Classification Metrics:")
        print(classification_report(y_true_slot_flatten, y_pred_slot_flatten, zero_division=0))

        y_pred_action_labels = (y_pred_action > 0.5).astype(int) # Ngưỡng 0.5 cho sigmoid
        print("Action Classification Metrics:")
        print(multilabel_confusion_matrix(y_test_act_one_hot, y_pred_action_labels, zero_division=0))

    def save(self, path: str = "./results/models/s2_model.keras"):
            """Saves the current model to the specified path."""
            try:
                os.makedirs(os.path.dirname(path), exist_ok=True) # Tạo thư mục nếu chưa tồn tại
                self.model.save(path)
                print(f"Model saved to {path}")
            except Exception as e:
                print(f"Error saving model: {e}")

    def load(self, path: str = "./results/models/s2_model.keras"):
        """Loads a pre-trained model from the specified path."""
        try:
            self.model = load_model(path)
            print(f"Model loaded from {path}")
        except FileNotFoundError:
            print(f"Error: Model file not found at {path}")
            return False
        except Exception as e:
            print(f"An error occurred during model loading: {e}")
            return False
        return True
