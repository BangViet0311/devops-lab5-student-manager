# Báo cáo Lab 5 — Git Flow & Code Review

## Thông tin nhóm
- Nhóm: [Bổ sung]
- Dev A: [Họ tên — MSSV — GitHub]
- Dev B: [Họ tên — MSSV — GitHub]
- Tài khoản GitHub: BangViet0311.
- Remote dự kiến: https://github.com/BangViet0311/devops-lab5-student-manager.git
  (đã cấu hình origin local, chưa tạo/xác minh repo online).

## Đã thực hiện trên máy
1. Kiểm tra Git 2.54.0 và Python 3.13.1; dùng cấu hình Git hiện có,
   không thay đổi cấu hình global của máy.
2. Khởi tạo repository riêng, nhánh mặc định `main`.
3. Commit README, .gitignore, Student model và main riêng biệt.
4. Tạo `develop`; tách độc lập `feature/add-student` và `feature/search-student`.
5. Commit hai tính năng, merge local vào develop bằng `--no-ff`.
6. Giải quyết conflict thật trong `src/main.py`, giữ cả hai hàm.
7. Tách hai nhánh README từ cùng develop. Merge B trước, merge A gây conflict.
8. Lưu log và nội dung conflict trong `evidence/06-*`;
   sửa thành “Nhóm A & Nhóm B”, add và commit kết quả.
9. Merge develop về main và bổ sung tài liệu, kiểm thử.

## Giải thích conflict
Hai nhánh thêm phiên bản khác nhau ở cùng vị trí trong README.
Khi develop đã merge B và đang merge A:
- `<<<<<<< HEAD`: phiên bản Nhóm B trên develop.
- `=======`: ranh giới hai thay đổi.
- `>>>>>>> feature/update-readme-a`: phiên bản Nhóm A.
Giữ ý của cả hai, xóa marker, `git add README.md`, rồi `git commit`.
Tài liệu đề gốc đã đảo vai A/B trong phần giải thích marker.

## Kiểm thử
Lệnh: `python -m unittest discover -s tests -v`.
Các ca kiểm tra: model, dictionary, chuỗi hiển thị, thêm mới, mã trùng,
danh sách rỗng, tìm tên/mã, không phân biệt hoa thường, không có kết quả,
từ khóa rỗng và không làm thay đổi danh sách khi tìm.
Xem kết quả thực thi tại `evidence/09-tests.txt`.
Demo: `python src/main.py`, xem `evidence/08-final-output.txt`.

## Phần chưa hoàn thành
- Tạo repository GitHub, push/pull, clone trên máy Dev B.
- Hai PR được merged và review bằng tài khoản người thứ hai.
- Ảnh chụp thật của GitHub, terminal và trình soạn thảo.
- Điền thông tin thành viên và đổi tên ZIP theo đề.

Các merge trong lịch sử hiện tại là **merge local**, không phải GitHub PR.
Toàn bộ commit dùng danh tính Git có sẵn; không giả làm Dev A/Dev B.
Log văn bản không thay thế ảnh minh chứng theo rubric.
