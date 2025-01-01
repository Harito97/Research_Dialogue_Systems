# Dialogue Act Detection for Task-Oriented Dialogue Systems

## Objective

**Description**:
This project implements a dialogue act detection system using the MultiWOZ dataset. Dialogue act detection is a fundamental task in building task-oriented dialogue systems, laying the groundwork for dialogue state tracking, policy generation, and response generation.

Key features of this project include:
- **Data Processing**: Extraction of (utterance, dialogue act) pairs from the MultiWOZ dataset and splitting into train/validation/test sets.
- **Model Implementation**: Sequence labelling models using GRU, LSTM, and BERT encoders for dialogue act detection.
- **Performance Evaluation**: Metrics such as Precision, Recall, and F1-score to compare the effectiveness of different models.
- **Documentation**: Detailed reports and notebooks explaining the methodology, implementation, and results.

This repository is ideal for anyone interested in natural language processing (NLP), dialogue systems, or practical applications of sequence labelling techniques.

**Keywords**:
- Dialogue Systems
- Dialogue Act Detection
- Task-Oriented Dialogue
- MultiWOZ Dataset
- Sequence Labelling
- Natural Language Processing (NLP)
- GRU
- LSTM
- BERT
- Machine Learning
- Python

## Guide to run

```bash
pip install -r requirements.txt
python main.py --tasks download_data
# Args = Namespace(tasks='download_data', data_dir='./data/dataset_multiwoz_2_2.json')
# Downloading the raw data of MultiWOZ 2.2 dataset...
# Save dataset to disk
# Downloaded the raw data of MultiWOZ 2.2 dataset in ./data/dataset_multiwoz_2_2.json
python main.py --tasks process_and_save
python main.py --tasks load_process_and_train
python main.py --tasks evaluate
python main.py --tasks demo
```

python main.py --tasks process_and_save && python main.py --tasks load_process_and_train && python main.py --tasks evaluate && python main.py --tasks demo
#&
