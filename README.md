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

### Use simple method (need to train)

```bash
pip install -r requirements.txt
nohup python main.py --tasks download_data > download_data.log 2>&1 &
nohup python main.py --tasks process_and_save > process_and_save.log 2>&1 &
nohup python main.py --tasks load_process_and_train > load_process_and_train.log 2>&1 &
nohup python main.py --tasks evaluate > evaluate.log 2>&1 &
nohup python main.py --tasks demo #> demo.log 2>&1 &
```

Or:
```bash
python main.py --tasks download_data
# Args = Namespace(tasks='download_data', data_dir='./data/dataset_multiwoz_2_2.json')
# Downloading the raw data of MultiWOZ 2.2 dataset...
# Save dataset to disk
# Downloaded the raw data of MultiWOZ 2.2 dataset in ./data/dataset_multiwoz_2_2.json
python main.py --tasks process_and_save
python main.py --tasks load_process_and_train
python main.py --tasks evaluate
python main.py --tasks demo

python main.py --tasks process_and_save && python main.py --tasks load_process_and_train && python main.py --tasks evaluate && python main.py --tasks demo #&
```

### Use LLM model (no need to train)
```bash
# Remember the GEMINI api key
python main.py --tasks use_llm
```

## S1 & S2 model structure

```markdown
┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Layer (type)        ┃ Output Shape      ┃    Param # ┃ Connected to      ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ input_layer         │ (None, 20, 312)   │          0 │ -                 │
│ (InputLayer)        │                   │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ bidirectional       │ (None, 20, 256)   │    451,584 │ input_layer[0][0] │
│ (Bidirectional)     │                   │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ dropout (Dropout)   │ (None, 20, 256)   │          0 │ bidirectional[0]… │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ global_average_poo… │ (None, 256)       │          0 │ dropout[0][0]     │
│ (GlobalAveragePool… │                   │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ dropout_1 (Dropout) │ (None, 256)       │          0 │ global_average_p… │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ slot_output         │ (None, 20, 53)    │     13,621 │ dropout[0][0]     │
│ (TimeDistributed)   │                   │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ action_output       │ (None, 24)        │      6,168 │ dropout_1[0][0]   │
│ (Dense)             │                   │            │                   │
└─────────────────────┴───────────────────┴────────────┴───────────────────┘
 Total params: 471,373 (1.80 MB)
 Trainable params: 471,373 (1.80 MB)
 Non-trainable params: 0 (0.00 B)
```
