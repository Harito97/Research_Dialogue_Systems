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
# ├── reports/                  # Chứa báo cáo
# │   ├── report_midterm.pdf
# │   ├── report_final.pdf
# ├── notebooks/                # Các notebook phân tích
# │   ├── exploratory_analysis.ipynb
# ├── references/               # Tài liệu tham khảo
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

mkdir reports/
touch reports/report_midterm.pdf reports/report_final.pdf

mkdir notebooks/
touch notebooks/exploratory_analysis.ipynb

mkdir references/
touch references/README.md

touch README.md requirements.txt .gitignore main.py
