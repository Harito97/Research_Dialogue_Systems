**Nghiên cứu [MultiWOZ 2.4](../../references/MultiWOZ%202.4_%20A%20Multi-Domain%20Task-Oriented%20Dialogue%20Dataset%20with%20Essential%20Annotation%20Corrections%20to%20Improve%20State%20Tracking%20Evaluation%20__%202104.00773v2.pdf) và [DialogStudio](../../references/DialogStudio_%20Towards%20Richest%20and%20Most%20Diverse%20Unified%20Dataset%20Collection%20for%20Conversational%20AI%20__%202307.10172v3.pdf)**

# Tổng quan về **bài toán**, **phương pháp** và **bình luận** hai nghiên cứu

Cả hai nghiên cứu MultiWOZ 2.4 và DialogStudio đều tập trung vào lĩnh vực **Hệ thống hội thoại định hướng nhiệm vụ (Task-Oriented Dialogue Systems)**, một nhánh quan trọng của **Trí tuệ nhân tạo hội thoại (Conversational AI)**.  

**Bài toán chung của cả hai nghiên cứu là nâng cao chất lượng của các hệ thống hội thoại định hướng nhiệm vụ.** Các hệ thống này thường được huấn luyện dựa trên các tập dữ liệu hội thoại lớn, và hiệu suất của chúng phụ thuộc rất nhiều vào chất lượng của dữ liệu. 

**MultiWOZ 2.4** tập trung vào việc **cải thiện chất lượng chú thích (annotation)** cho tập dữ liệu hội thoại đa miền MultiWOZ 2.1. Nghiên cứu này đã xác định và sửa chữa một lượng lớn các lỗi chú thích trong tập dữ liệu MultiWOZ 2.1, từ đó tạo ra một phiên bản mới là **MultiWOZ 2.4 với chất lượng dữ liệu cao hơn.** 

**DialogStudio**, mặt khác, tập trung vào việc **xây dựng một tập hợp dữ liệu hội thoại thống nhất và đa dạng**. Nghiên cứu này đã thu thập và tổ chức hơn 80 tập dữ liệu hội thoại từ nhiều nguồn khác nhau, bao gồm cả dữ liệu hội thoại mở, dữ liệu hội thoại định hướng nhiệm vụ, dữ liệu hiểu ngôn ngữ tự nhiên, dữ liệu đề xuất hội thoại, dữ liệu tóm tắt hội thoại và dữ liệu hội thoại dựa trên kiến thức. DialogStudio cung cấp một **nguồn dữ liệu phong phú và đa dạng** cho việc nghiên cứu và huấn luyện các mô hình hội thoại.

**Bình luận:**

* Cả hai nghiên cứu đều có đóng góp quan trọng cho lĩnh vực Hệ thống hội thoại định hướng nhiệm vụ. 
* MultiWOZ 2.4 cung cấp một tập dữ liệu chất lượng cao hơn cho việc đánh giá hiệu suất của các mô hình theo dõi trạng thái hội thoại. 
* DialogStudio cung cấp một nguồn dữ liệu phong phú và đa dạng cho việc nghiên cứu và huấn luyện các mô hình hội thoại.

# Về paper MultiWOZ

**Mục tiêu:**

* Cải thiện chất lượng chú thích của tập dữ liệu MultiWOZ 2.1, tập trung vào tập validation và tập test.
* Tạo ra một phiên bản mới là MultiWOZ 2.4 với chất lượng dữ liệu cao hơn, giúp đánh giá hiệu suất của các mô hình theo dõi trạng thái hội thoại một cách chính xác và công bằng hơn.

**Phương pháp:**

* Xác định và phân loại 6 loại lỗi chú thích chính trong tập dữ liệu MultiWOZ 2.1.
* Sửa chữa thủ công các lỗi chú thích trong tập validation và tập test.
* Giữ nguyên chú thích trong tập huấn luyện để khuyến khích các mô hình học cách xử lý dữ liệu nhiễu.

**Kết quả:**

* MultiWOZ 2.4 đã sửa chữa hơn 41% lượt hội thoại trong 65% các hội thoại của tập validation và tập test.
* Các mô hình theo dõi trạng thái hội thoại đạt hiệu suất cao hơn đáng kể trên MultiWOZ 2.4 so với MultiWOZ 2.1.
* Đánh giá con người cho thấy chất lượng chú thích của MultiWOZ 2.4 tốt hơn so với MultiWOZ 2.1.

# Về paper DialogStudio

**Mục tiêu:**

* Xây dựng một tập hợp dữ liệu hội thoại thống nhất và đa dạng, bao gồm nhiều loại dữ liệu hội thoại từ nhiều nguồn khác nhau.
* Hỗ trợ nghiên cứu trên từng tập dữ liệu riêng lẻ cũng như huấn luyện các mô hình ngôn ngữ lớn (LLM).
* Cung cấp dữ liệu dễ dàng truy cập với định dạng và tài liệu thống nhất.

**Phương pháp:**

* Thu thập và tổ chức hơn 80 tập dữ liệu hội thoại từ nhiều nguồn khác nhau.
* Thống nhất định dạng dữ liệu, bao gồm thông tin về ID hội thoại, nhãn phân chia dữ liệu, miền, nhiệm vụ, nội dung, kiến thức bên ngoài, kiến thức theo dõi trạng thái hội thoại (DST), và kiến thức về mục đích.
* Xây dựng các mô hình hội thoại dựa trên DialogStudio và đánh giá hiệu suất của chúng.

**Kết quả:**

* DialogStudio là tập hợp dữ liệu hội thoại thống nhất lớn nhất hiện nay, bao gồm dữ liệu từ nhiều lĩnh vực và nhiệm vụ khác nhau.
* Dữ liệu DialogStudio có thể được tải xuống thông qua HuggingFace.
* Các mô hình được huấn luyện trên DialogStudio đạt hiệu suất vượt trội trong cả hai kịch bản học zero-shot và few-shot.

**Thông tin bổ sung:**

* DialogStudio được phát hành công khai trên GitHub và HuggingFace.
* Mã nguồn của DialogStudio được cấp phép theo giấy phép Apache 2.0.
* Nghiên cứu DialogStudio khuyến khích đóng góp từ cộng đồng. 

---

# Chi tiết về hai bộ dữ liệu MultiWOZ 2.4 và DialogStudio

## Thông tin chi tiết về bộ dữ liệu MultiWOZ 2.4

MultiWOZ 2.4 là phiên bản cải tiến của tập dữ liệu hội thoại đa miền MultiWOZ 2.1. Nghiên cứu tập trung vào việc khắc phục các lỗi chú thích tồn tại trong tập validation và tập test của MultiWOZ 2.1, trong khi vẫn giữ nguyên tập huấn luyện. 

**Các điểm nổi bật về MultiWOZ 2.4:**

* **Mục tiêu:**  Nâng cao chất lượng chú thích của tập dữ liệu MultiWOZ 2.1 để cải thiện việc đánh giá hiệu suất của các mô hình theo dõi trạng thái hội thoại. 
* **Quy trình tinh chỉnh:**  Nghiên cứu xác định và sửa chữa sáu loại lỗi chú thích chính:
    * **Không khớp ngữ cảnh:**  Giá trị slot không khớp với thông tin được đề cập trong ngữ cảnh hội thoại.
    * **Thiếu chú thích:**  Slot không được gán nhãn mặc dù giá trị của nó đã được đề cập.
    * **Không được đề cập:**  Slot được gán nhãn nhưng giá trị của nó không được đề cập trong hội thoại.
    * **Giá trị không đầy đủ:**  Giá trị slot là một chuỗi con hoặc viết tắt của dạng đầy đủ của nó.
    * **Xử lý thời gian ngầm:**  Giá trị thời gian được xử lý ngầm thay vì sao chép trực tiếp từ ngữ cảnh.
    * **Chú thích không cần thiết:**  Các chú thích không cần thiết được loại bỏ để tăng tính nhất quán.
* **Kết quả:**  Hơn 41% lượt hội thoại trong 65% các hội thoại của tập validation và tập test đã được sửa chữa. 
* **Lợi ích:**  Cung cấp một tập dữ liệu với chất lượng chú thích cao hơn, giúp đánh giá hiệu suất của các mô hình theo dõi trạng thái hội thoại một cách chính xác và công bằng hơn.


## Các mô hình áp dụng trên MultiWOZ 2.4 và kết quả

Nghiên cứu đã đánh giá hiệu suất của tám mô hình theo dõi trạng thái hội thoại hiện đại trên MultiWOZ 2.4:

* SUMBT
* STAR
* TRADE
* PIN
* SOM-DST
* SimpleTOD
* SAVN
* TripPy

**Kết quả:**

* **Tất cả các mô hình đều đạt hiệu suất cao hơn đáng kể trên MultiWOZ 2.4 so với MultiWOZ 2.1**. 
* Độ chính xác mục tiêu chung (Joint Goal Accuracy) và độ chính xác slot (Slot Accuracy) đều được cải thiện đáng kể. 
* **Kết quả này cho thấy MultiWOZ 2.4 là một tập dữ liệu hiệu quả hơn cho việc đánh giá và so sánh các mô hình theo dõi trạng thái hội thoại.**

## Thông tin chi tiết về bộ dữ liệu DialogStudio

**DialogStudio là tập hợp dữ liệu hội thoại thống nhất lớn nhất hiện nay, bao gồm hơn 80 tập dữ liệu hội thoại đa dạng từ nhiều nguồn khác nhau**.  Nghiên cứu này nhằm mục đích giải quyết vấn đề thiếu dữ liệu huấn luyện toàn diện và đa dạng cho các mô hình hội thoại.

**Các điểm nổi bật về DialogStudio:**

* **Mục tiêu:**
    * Xây dựng một tập hợp dữ liệu hội thoại thống nhất và đa dạng để hỗ trợ nghiên cứu và phát triển các mô hình hội thoại hiệu quả hơn.
    * Hỗ trợ nghiên cứu trên từng tập dữ liệu riêng lẻ cũng như huấn luyện các mô hình ngôn ngữ lớn (LLM).
    * Cung cấp dữ liệu dễ dàng truy cập với định dạng và tài liệu thống nhất.
* **Nội dung:**  Bao gồm dữ liệu từ các hạng mục:
    * Hội thoại mở (Open-Domain Dialogues)
    * Hội thoại định hướng nhiệm vụ (Task-Oriented Dialogues)
    * Hiểu ngôn ngữ tự nhiên (Natural Language Understanding)
    * Đề xuất hội thoại (Conversational Recommendation)
    * Tóm tắt hội thoại (Dialogue Summarization)
    * Hội thoại dựa trên kiến thức (Knowledge-Grounded Dialogues)
* **Định dạng:**  Thống nhất định dạng dữ liệu cho tất cả các tập dữ liệu, bao gồm thông tin về ID hội thoại, nhãn phân chia dữ liệu, miền, nhiệm vụ, nội dung, kiến thức bên ngoài, kiến thức theo dõi trạng thái hội thoại (DST), và kiến thức về mục đích.
* **Truy cập dữ liệu:**  Dữ liệu DialogStudio có thể được tải xuống thông qua HuggingFace bằng API `load_dataset()`.


## Các mô hình áp dụng trên DialogStudio và kết quả

Nghiên cứu đã huấn luyện các mô hình hội thoại dựa trên DialogStudio, bao gồm DialogStudio-T5 và DialogStudio-Flan-T5. 

**Các mô hình này được đánh giá trên nhiều nhiệm vụ khác nhau, bao gồm:**

* Tạo phản hồi hội thoại
* Hiểu hướng dẫn dựa trên prompt
* MMLU và BBH
* Các điểm chuẩn thay thế như AlpacaEval và MT-Bench

**Kết quả:**

* **Các mô hình được huấn luyện trên DialogStudio đạt hiệu suất vượt trội trong cả hai kịch bản học zero-shot và few-shot**.
* Cụ thể, DialogStudio-T5 và DialogStudio-Flan-T5 cho thấy khả năng khái quát hóa mạnh mẽ và vượt trội so với các mô hình cơ sở trong các nhiệm vụ tạo phản hồi hội thoại và hiểu hướng dẫn.
* Mặc dù hiệu suất trên MMLU và BBH giảm nhẹ, nhưng khả năng xử lý hội thoại của các mô hình được cải thiện đáng kể. 

---

**Kết luận:** 

Cả MultiWOZ 2.4 và DialogStudio đều là những đóng góp quan trọng cho lĩnh vực nghiên cứu và phát triển Hệ thống hội thoại định hướng nhiệm vụ. 

* MultiWOZ 2.4 cung cấp một tập dữ liệu chất lượng cao hơn cho việc đánh giá hiệu suất của các mô hình theo dõi trạng thái hội thoại. 
* DialogStudio cung cấp một nguồn dữ liệu phong phú và đa dạng cho việc nghiên cứu và huấn luyện các mô hình hội thoại. 
