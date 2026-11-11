# Báo cáo Lab 5 — Git Flow & Code Review

## Thông tin nhóm
- Nhóm: [Bổ sung]
- Người thực hiện: [Điền họ tên — MSSV].
- Vai Dev A: BangViet0311, tài khoản chính.
- Vai Dev B: Bangviet-0311, tài khoản phụ của cùng người thực hiện.
- Hình thức cá nhân mô phỏng hai vai; không khai là nhóm hai người hoặc review độc lập.
- Tài khoản GitHub: BangViet0311.
- Repository: https://github.com/BangViet0311/devops-lab5-student-manager
  (đã tạo public và push các nhánh ban đầu).
- PR #1: https://github.com/BangViet0311/devops-lab5-student-manager/pull/1
- PR #2: https://github.com/BangViet0311/devops-lab5-student-manager/pull/2
- Hai PR đã được tài khoản phụ review/approve và merge thật trên GitHub.
- Bản hoàn chỉnh tích hợp lịch sử PR được đồng bộ vào main/develop.
- Nhánh `lab/local-completed` là bản lưu bổ sung của bài thực hành.

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

## Hoàn tất GitHub và minh chứng
- GitHub PR #1: review của Bangviet-0311 và merge commit `01befe8`.
- Sau khi merge #1, đồng bộ develop vào nhánh search và xử lý conflict thật,
  giữ cả hai hàm; chạy lại demo trước khi push.
- GitHub PR #2: review của Bangviet-0311 và merge commit `eee4c7f`.
- Fetch lịch sử PR về local, merge với bản hoàn chỉnh, kiểm thử, push main/develop.
- Ảnh 01/02/08 chụp cửa sổ PowerShell thật chạy lệnh trên dự án.
- Ảnh 03/04/05 chụp trực tiếp trang GitHub, gồm trạng thái Merged và Approve.
- Ảnh 06/07 chụp VS Code trong clone riêng tên `Lab5-conflict-replay-0f8cad7f`.
  Clone này lấy đúng hai nhánh README trong lịch sử, bắt đầu từ nhánh B rồi merge A,
  tạo conflict thật; sau đó sửa README, add, commit và kiểm tra working tree sạch.
  Đây là tái hiện phục vụ ảnh minh chứng, không phải ảnh chụp tại thời điểm conflict đầu tiên.
- Không chỉnh sửa nội dung ảnh để giả trạng thái; không tạo người review giả.
- Tên Nhóm A/B trong README là nhãn của kịch bản, không phải hai người thực hiện.

## Việc người nộp bài cần làm
- Điền họ tên, MSSV và thông tin nhóm nếu được yêu cầu, đổi tên ZIP theo quy định.
- Xin giảng viên chấp thuận việc một người dùng hai tài khoản thay nhóm hai người.
- Không có máy Dev B độc lập; clone thứ hai được thực hiện trên cùng máy.
