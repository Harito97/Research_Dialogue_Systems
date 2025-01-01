

# Introduction

Theo dõi trạng thái hội thoại (Dialogue State Tracking - DST) là một thành phần **then chốt** trong các hệ thống hội thoại hướng tác vụ (Task-Oriented Dialogue Systems).

Mục tiêu của DST là theo dõi và cập nhật trạng thái hội thoại theo thời gian thực, dựa trên các lượt tương tác giữa người dùng và hệ thống.
Từ đó hỗ trợ cho việc đưa ra quyết định và tạo phản hồi phù hợp từ hệ thống.

Trạng thái này bao gồm những thông tin quan trọng như:

- **Ý định của người dùng (User Intent):** Mong muốn hoặc mục đích của người dùng (ví dụ: đặt vé máy bay, tìm nhà hàng, hỏi thời tiết).
- **Tham số liên quan (Slots/Entities):** Các chi tiết cụ thể liên quan đến ý định, như điểm đi, điểm đến, thời gian, hoặc các yêu cầu đặc thù khác.

**Ví dụ Minh Họa**

Người dùng: "Tôi muốn đặt vé máy bay từ Hà Nội đi Sài Gòn vào ngày mai."

Trong trường hợp này, DST cần xác định:

- **Ý định:** Đặt vé máy bay.

- **Tham số liên quan:**

  - Điểm đi: Hà Nội.

  - Điểm đến: Sài Gòn.

  - Ngày đi: Ngày mai.
