#!/bin/bash

# Research_Dialogue_Systems/
# ├── data/                     # Chứa dữ liệu MultiWoZ
# │   ├── raw/                  # Dữ liệu gốc
# │   ├── processed/            # Dữ liệu đã trích chọn (x, y)
# ├── src/                      # Chứa mã nguồn
# │   ├── preprocess.py         # Xử lý dữ liệu MultiWoZ
# │   ├── train.py              # Huấn luyện mô hình
# │   ├── evaluate.py           # Đánh giá mô hình
# ├── models/                   # Chứa các mô hình
# │   ├── lstm_model.py         # Model LSTM
# │   ├── bert_model.py         # Model BERT
# ├── docs/
# │   ├── data/
# │   ├── probs_methods/
# │   ├── main_doc.pdf
# ├── notebooks/                # Các notebook phân tích
# │   ├── exploratory_analysis.ipynb
# ├── results/                  # Lưu kết quả thực nghiệm
# │   ├── logs/                 # Logs huấn luyện
# │   ├── models/               # Trọng số mô hình đã lưu
# │   └── evaluation_doc.txt # Báo cáo đánh giá kết quả
# ├── references/               # Tài liệu tham khảo
# ├── manuscript/               # Bài báo
# ├── README.md                 # Hướng dẫn sử dụng project
# ├── main.py                   # File chạy chính
# ├── .gitignore                # File cấu hình git
# └── requirements.txt          # Danh sách thư viện cần thiết

mkdir data/ data/raw data/processed
touch data/raw/README.md data/processed/README.md

mkdir src/
touch src/preprocess.py src/train.py src/evaluate.py

mkdir models/
touch models/lstm_model.py models/bert_model.py

mkdir docs/ docs/data/ docs/probs_methods/
touch docs/main_doc.pdf

mkdir notebooks/
touch notebooks/exploratory_analysis.ipynb

mkdir results/ results/logs results/models
touch results/evaluation_doc.txt

mkdir references/ references/papers
touch references/README.md

mkdir manuscript/

touch README.md requirements.txt .gitignore main.py
