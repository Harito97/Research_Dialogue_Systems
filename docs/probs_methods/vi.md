**Hệ Thống Hỗ Trợ Hội Thoại (Dialogue Systems)**

Hệ thống hỗ trợ hội thoại (**Dialogue Systems**, còn được gọi là **Dialogue Agents** hay **Chatbots**) là một lĩnh vực quan trọng trong xử lý ngôn ngữ tự nhiên (NLP) và tương tác người-máy (HCI). Báo cáo này sẽ trình bày chi tiết về các vấn đề, bài toán và phương pháp chung liên quan đến Dialogue Systems dựa trên hai tài liệu [Book_ Chapter_15](../../references/Book_%20Chapter_15.pdf) & [Slides_ 24_Dialogue_May_6_2021](../../references/Slides_%2024_Dialogue_May_6_2021.pdf).

# Vấn Đề và Bài Toán

## Giới Thiệu

Dialogue Systems là các hệ thống có khả năng thực hiện hội thoại với người dùng, mô phỏng cuộc trò chuyện tự nhiên giữa người và người. Chúng có nhiều ứng dụng trong thực tế, bao gồm:

* **Trợ lý ảo cá nhân:** Siri, Alexa, Cortana, Google Assistant
* **Giải trí:** Chatbots có thể trò chuyện, kể chuyện cười, cung cấp thông tin
* **Hỗ trợ công việc:** Đặt lịch hẹn, đặt vé máy bay, đặt chỗ nhà hàng
* **Chăm sóc sức khỏe:** Cung cấp hỗ trợ tâm lý

## Phân Loại

Có hai loại Dialogue Systems chính:

1. **Chatbots:** Mục tiêu là mô phỏng hội thoại tự nhiên, thường mang tính chất giải trí hoặc hỗ trợ tâm lý.
2. **Hệ thống hội thoại hướng nhiệm vụ (Task-based Dialogue Agents):** Mục tiêu là hỗ trợ người dùng hoàn thành một nhiệm vụ cụ thể, ví dụ như đặt vé máy bay, đặt chỗ nhà hàng.

## Đặc Điểm Của Hội Thoại Tự Nhiên

Để xây dựng Dialogue Systems hiệu quả, cần hiểu rõ các đặc điểm của hội thoại tự nhiên giữa người và người. Một số đặc điểm quan trọng bao gồm:

* **Lượt lời (Turns):** Mỗi lượt lời là một đóng góp của một người nói trong cuộc hội thoại.
* **Vấn đề chuyển lượt lời:** Xác định thời điểm bắt đầu và kết thúc lượt lời. Việc gián đoạn cũng là một vấn đề cần xem xét.
* **Ngôn ngữ như một hành động:** Mỗi lượt lời là một hành động (**speech act**) mà người nói thực hiện, ví dụ như khẳng định, yêu cầu, hứa hẹn, cảm ơn.
* **Hiểu ngầm:** Người nói và người nghe cần thiết lập nền tảng chung (**common ground**), sử dụng các tín hiệu để đảm bảo hiểu ý của nhau (**grounding**).
* **Cấu trúc hội thoại:** Hội thoại có cấu trúc, ví dụ như cặp câu hỏi-trả lời, đề xuất-chấp nhận/từ chối. Ngoài ra còn có các hội thoại con (**subdialogues**), ví dụ như hội thoại sửa lỗi, làm rõ thông tin.
* **Chủ động hội thoại:** Hội thoại có thể do một người chủ động (ví dụ như phỏng vấn), hoặc cả hai bên cùng chủ động (**mixed initiative**).
* **Suy luận:** Người nghe thường phải suy luận từ thông tin được cung cấp để hiểu đầy đủ ý của người nói.

# Các Phương Pháp

## Chatbots Dựa Trên Luật (Rule-based Chatbots)

* ELIZA (1966) và PARRY (1971) là hai ví dụ điển hình của Chatbots dựa trên luật.
* ELIZA mô phỏng nhà tâm lý học Rogerian, phản ánh lại lời nói của người dùng để tạo cảm giác trò chuyện.
* PARRY mô phỏng bệnh nhân tâm thần phân liệt, sử dụng hệ thống luật phức tạp hơn để tạo ra các phản ứng.
* Cả ELIZA và PARRY đều sử dụng các mẫu câu (pattern) và luật biến đổi (transformation rules) để tạo phản hồi.
* **Hạn chế:** Tốn kém, dễ bị lỗi, khó mở rộng.

## Chatbots Dựa Trên Dữ Liệu (Corpus-based Chatbots)

* Sử dụng kho dữ liệu hội thoại lớn để huấn luyện mô hình.
* Hai kiến trúc chính:
    * **Phản hồi bằng truy xuất (Retrieval):** Tìm câu trả lời phù hợp nhất từ kho dữ liệu dựa trên độ tương đồng.
    * **Phản hồi bằng sinh (Generation):** Sử dụng mô hình ngôn ngữ hoặc mô hình encoder-decoder để tạo phản hồi mới.
* **Kho dữ liệu:**
    * Bản ghi âm cuộc gọi điện thoại, hội thoại phim ảnh.
    * Dữ liệu từ các nền tảng mạng xã hội như Twitter, Reddit, Weibo.
    * Dữ liệu được tạo bởi con người, ví dụ như Topical-Chat, EMPATHETICDIALOGUES.
* **Ưu điểm:** Linh hoạt hơn Chatbots dựa trên luật.
* **Hạn chế:** 
    * **Dễ bị lặp lại, nhàm chán.**
    * **Dễ bị ảnh hưởng bởi dữ liệu huấn luyện, có thể tạo ra phản hồi không phù hợp.**

## Kiến Trúc Frame-based (GUS)

* **Mục tiêu:** Hỗ trợ người dùng hoàn thành nhiệm vụ cụ thể.
* **Kiến trúc:** Sử dụng frame (khung) với các slot (ô) và giá trị để biểu diễn ý định của người dùng.
* **Ví dụ:** Frame đặt vé máy bay có các slot như ORIGIN (điểm khởi hành), DEST (điểm đến), DEP DATE (ngày khởi hành), DEP TIME (giờ khởi hành).
* **Hoạt động:** Hệ thống sẽ hỏi người dùng các câu hỏi để lấp đầy các slot trong frame.

## Kiến Trúc Dialogue-State

* **Mở rộng kiến trúc frame-based:** 
    * Sử dụng dialogue acts (hành động hội thoại).
    * Sử dụng machine learning để xử lý ngôn ngữ tự nhiên.
    * Tạo phản hồi tự nhiên hơn.
* **Các thành phần:**
    * NLU (Spoken Language Understanding): Trích xuất thông tin từ lời nói của người dùng.
    * Dialogue state tracker: Theo dõi trạng thái hiện tại của hội thoại.
    * Dialogue policy: Quyết định hành động tiếp theo của hệ thống.
    * NLG (Natural Language Generation): Tạo phản hồi bằng ngôn ngữ tự nhiên.
* **Dialogue acts:** Biểu diễn hành động hội thoại và grounding. Ví dụ: INFORM, REQUEST, CONFIRM.
* **Theo dõi trạng thái hội thoại:** Xác định dialogue act và cập nhật frame dựa trên thông tin từ người dùng.
* **Phát hiện hành động sửa lỗi:** Xác định khi người dùng sửa lỗi hệ thống, sử dụng các đặc trưng về từ vựng, ngữ nghĩa, ngữ âm.
* **Chính sách hội thoại:**
    * Xác định hành động tiếp theo dựa trên trạng thái hội thoại.
    * **Xác nhận (Confirmation):** Đảm bảo hệ thống hiểu ý người dùng. 
        * **Rõ ràng (Explicit):** Hỏi trực tiếp người dùng.
        * **Ngầm (Implicit):** Lặp lại thông tin đã hiểu.
    * **Từ chối (Rejection):** Khi hệ thống không hiểu lời nói của người dùng.
* **Sinh ngôn ngữ tự nhiên:**
    * **Kế hoạch nội dung:** Xác định nội dung cần truyền đạt.
    * **Hiện thực hóa câu:** Tạo câu văn dựa trên nội dung.
    * **Xóa bỏ từ vựng (Delexicalization):** Thay thế các giá trị cụ thể bằng các thẻ chung để tăng khả năng khái quát hóa.
    * **Tạo câu hỏi làm rõ:** Khi hệ thống cần thêm thông tin.

# Đánh Giá Hệ Thống Hội Thoại

* **Chatbots:** Chủ yếu đánh giá bằng con người, thông qua đánh giá của người tham gia hoặc người quan sát.
* **Hệ thống hội thoại hướng nhiệm vụ:**
    * **Đánh giá đầu-cuối (End-to-end evaluation):** Đánh giá khả năng hoàn thành nhiệm vụ.
    * **Tỷ lệ lỗi slot (Slot Error Rate):** Đánh giá độ chính xác của việc trích xuất thông tin.
* Các tiêu chí đánh giá khác:
    * Hiệu quả: Thời gian hội thoại, số lượt lời, số truy vấn.
    * Chất lượng: Số lần từ chối, số lần người dùng phải gián đoạn.

# Thiết Kế Và Vấn Đề Đạo Đức

* **Thiết kế lấy người dùng làm trung tâm:**
    * Nghiên cứu người dùng và nhiệm vụ.
    * Xây dựng mô phỏng và prototype (ví dụ: Wizard of Oz study).
    * Kiểm tra thiết kế lặp đi lặp lại với người dùng.
* **Vấn đề đạo đức:**
    * **An toàn cho người dùng:** Hệ thống cần cung cấp thông tin chính xác, tránh gây hại cho người dùng.
    * **Ngôn ngữ lạm dụng và phân biệt đối xử:** Hệ thống cần tránh tạo ra phản hồi mang tính chất xúc phạm hoặc phân biệt đối xử.
    * **Rò rỉ thông tin:** Bảo vệ thông tin cá nhân của người dùng.

# Kết Luận

Dialogue Systems là một lĩnh vực nghiên cứu thú vị và đầy thách thức. Việc hiểu rõ các vấn đề, bài toán và phương pháp chung liên quan đến Dialogue Systems là rất quan trọng để xây dựng các hệ thống hiệu quả, an toàn và có ích cho người dùng. 
