import time
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Tắt các thông báo từ TensorFlow (0=DEBUG, 1=INFO, 2=WARNING, 3=ERROR)
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import warnings
warnings.filterwarnings("ignore")
import logging
logging.basicConfig(level=logging.ERROR)
import argparse
from src.preprocess import MultiWOZ_2_2
from src.models import S2_Model


def main():
    parser = argparse.ArgumentParser(
        description="Define tasks with the MultiWOZ 2.2 dataset."
    )
    parser.add_argument(
        "--tasks",
        type=str,
        default="",
        help="Tasks to perform: [download_data, process_and_save, load_process_and_train, evaluate, demo]",
    )

    args = parser.parse_args()  # Move this line before checking args.tasks

    dataset = MultiWOZ_2_2()

    start_time = time.time()
    if args.tasks == "download_data":
        parser.add_argument(
            "--data_dir",
            type=str,
            default="./data/dataset_multiwoz_2_2.json",
            help="The directory of raw data of MultiWOZ 2.2 dataset.",
        )
        args = parser.parse_args()
        print(f"Args = {args}")
        print("Downloading the raw data of MultiWOZ 2.2 dataset...")

        dataset.download_data(args.data_dir)
        print("Downloaded the raw data of MultiWOZ 2.2 dataset in", args.data_dir)
        print("Time taken:", time.time() - start_time)
        return 0

    if args.tasks == "process_and_save":
        parser.add_argument(
            "--data_dir",
            type=str,
            default="./data/dataset_multiwoz_2_2.json",
            help="The directory of raw data of MultiWOZ 2.2 dataset.",
        )
        parser.add_argument(
            "--des_dir",
            type=str,
            default="./data/multiwoz_2_2_processed_data.json",
            help="The directory of processed data of MultiWOZ 2.2 dataset.",
        )
        args = parser.parse_args()
        print(f"Args = {args}")
        print("Processing and saving the raw data of MultiWOZ 2.2 dataset...")
        dataset.process_and_save(args.data_dir, args.des_dir)
        print(
            "Processed and saved the raw data of MultiWOZ 2.2 dataset in", args.des_dir
        )
        print("Time taken:", time.time() - start_time)
        return 0

    if args.tasks == "load_process_and_train":
        parser.add_argument(
            "--data_dir",
            type=str,
            default="./data/multiwoz_2_2_processed_data.json",
            help="The directory of processed data of MultiWOZ 2.2 dataset.",
        )
        args = parser.parse_args()
        print(f"Args = {args}")
        print("Loading the processed data of MultiWOZ 2.2 dataset...")
        dataset.load_data(args.data_dir)
        print("Loading the model S2")
        model = S2_Model(
            max_sequence_length=dataset.MAX_SEQUENCE_LENGTH,
            num_classes_slot=dataset.NUM_CLASSES_SLOT,
            num_classes_act=dataset.NUM_CLASSES_ACT,
            bert_model=dataset.bert_model,
            embedding_dim=dataset.EMBEDDING_DIM,
            dropout_rate=0.2,
        )
        model.compile_summary()
        print("Training the model S2")
        history = model.train(
            dataset.X_train_bert,
            dataset.y_train_padded_one_hot,
            dataset.y_act_one_hot,
            dataset.X_val_bert,
            dataset.y_val_padded_one_hot,
            dataset.y_act_val_one_hot,
            dataset.slot_class_weights_dict,
            dataset.act_class_weights_dict,
        )
        print("Saving the model S2")
        model.model.save("./results/models/s2_model.keras")
        # Write history to log file
        with open(f"./results/logs/history.log", "w") as f:
            f.write(str(history.history))
        print("Time taken:", time.time() - start_time)
        return 0

    if args.tasks == "evaluate":
        parser.add_argument(
            "--data_dir",
            type=str,
            default="./data/multiwoz_2_2_processed_data.json",
            help="The directory of processed data of MultiWOZ 2.2 dataset.",
        )
        args = parser.parse_args()
        print(f"Args = {args}")
        print("Loading the processed data of MultiWOZ 2.2 dataset...")
        dataset.load_data(args.data_dir)
        print("Loading the model S2")
        model = S2_Model(
            max_sequence_length=dataset.MAX_SEQUENCE_LENGTH,
            num_classes_slot=dataset.NUM_CLASSES_SLOT,
            num_classes_act=dataset.NUM_CLASSES_ACT,
            bert_model=dataset.bert_model,
            embedding_dim=dataset.EMBEDDING_DIM,
            dropout_rate=0.2,
        )
        model.load("./results/models/s2_model.keras")
        print("Evaluating the model S2")
        model.evaluate(
            dataset.X_test_bert, dataset.y_test_padded_one_hot, dataset.y_act_test_one_hot
        )
        print("Time taken:", time.time() - start_time)
        return 0

    if args.tasks == "demo":
        print("Loading the model S2")
        model = S2_Model(
            max_sequence_length=dataset.MAX_SEQUENCE_LENGTH,
            num_classes_slot=dataset.NUM_CLASSES_SLOT,
            num_classes_act=dataset.NUM_CLASSES_ACT,
            bert_model=dataset.bert_model,
            embedding_dim=dataset.EMBEDDING_DIM,
            dropout_rate=0.2,
        )
        model.load("./results/models/s2_model.keras")
        print("Demo the model S2 (type 'quit' or 'q' to exit)")

        while True:
            user_input = input("Enter your text (or type 'quit' or 'q' to exit): ")
            if user_input.lower() in ("quit", "q"):
                break

            # Preprocess the user input (assuming dataset has preprocess_text function)
            preprocessed_text = dataset.preprocess_text(user_input)
            user_input_tensor = np.expand_dims(preprocessed_text, axis=0)

            # Get predictions
            slot_predictions, act_predictions = model.predict(user_input_tensor)

            # Convert predictions to labels (optional)
            predicted_slots = dataset.decode_predictions(slot_predictions[0])
            predicted_acts = dataset.decode_act_predictions(act_predictions[0])

            # Print the results
            print("Predicted Slots:", predicted_slots)
            print("Predicted Dialogue Acts:", predicted_acts)

            print("\n")  # Add a new line for better readability
        print("Time taken:", time.time() - start_time)
        return 0

    print("Invalid tasks. Please choose from [download_data, process_and_save, load_process_and_train, evaluate, demo].")
    print("Time taken:", time.time() - start_time)
    return 1

if __name__ == "__main__":
    # Eg. python main.py --tasks "download_data"
    # Eg. python main.py --tasks "process_and_save"
    # Eg. python main.py --tasks "load_process_and_train"
    # Eg. python main.py --tasks "evaluate"
    # Eg. python main.py --tasks "demo"
    main()

# --------------------------------------------------------------------------------

# import argparse
# from src.preprocess import split_train_dev_test


# def main():
#     parser = argparse.ArgumentParser(description="Define tasks with the MultiWOZ 2.4 dataset.")
#     parser.add_argument("--tasks", type=str, default="[split2.4]", help="Tasks to perform.")

#     args = parser.parse_args()  # Move this line before checking args.tasks

#     if "split" in args.tasks and "2.4" in args.tasks:
#         parser.add_argument(
#             "--data_dir",
#             type=str,
#             default="./data/raw/MULTIWOZ2.4",
#             help="The directory of raw data of MultiWOZ 2.4 dataset.",
#         )
#         parser.add_argument(
#             "--des_dir",
#             type=str,
#             default="./data/processed/MULTIWOZ2.4",
#             help="The directory of processed data of MultiWOZ 2.4 dataset.",
#         )
#         args = parser.parse_args()  # Re-parse to include new arguments
#         print(f"Args = {args}")
#         print("Splitting the raw data of MultiWOZ 2.4 dataset...")
#         split_train_dev_test(args.data_dir, args.des_dir)


# if __name__ == "__main__":
#     # Eg. python main.py --tasks "[split2.4]"
#     # Eg. python main.py --tasks "[split2.4]" --data_dir "./data/raw/MULTIWOZ2.4"
#     # Eg. python main.py --tasks "[split2.4]" --data_dir "./data/raw/MULTIWOZ2.4" --des_dir "./data/processed/MULTIWOZ2.4"
#     main()
