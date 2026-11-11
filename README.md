# Student Manager

Ứng dụng quản lý sinh viên — DevOps Lab 5
**Version 1.0.0** — Phát triển bởi Nhóm A & Nhóm B

## Tính năng
- Mô hình `Student`, xuất thông tin bằng `to_dict()`.
- `add_student()`: thêm sinh viên, từ chối mã trùng.
- `search_student()`: tìm một phần tên hoặc mã, không phân biệt hoa thường.
- Chương trình demo có 4 sinh viên, tìm `Van` trả về SV001 và SV003.

## Cài đặt và chạy
Yêu cầu Python 3.9+ và Git; không cần cài thư viện ngoài.
Mở terminal trong thư mục dự án:

```powershell
python src/main.py
python -m unittest discover -s tests -v
git log --oneline --graph --all
git branch -a
```

## Cấu trúc
```text
src/student.py          Mô hình sinh viên
src/main.py             Thêm, tìm kiếm và chạy demo
tests/test_students.py  Kiểm thử tự động
evidence/              Log thực hiện trên máy (không phải ảnh GitHub)
screenshots/           Danh sách ảnh cần chụp bổ sung
BAO_CAO.md             Báo cáo và trạng thái hoàn thành
HUONG_DAN_GITHUB.md     Các bước push, PR và review còn lại
```

## Git Flow
Đã thực hành local: `main`, `develop`, hai nhánh tính năng và hai nhánh
cập nhật README, tạo và giải quyết merge conflict, merge về `main`.
Các nhánh feature được giữ để tiện kiểm tra lịch sử.
Tên Nhóm A/B là nhãn kịch bản của đề, không phải hai người đã review thực tế.

Repository GitHub:
`https://github.com/BangViet0311/devops-lab5-student-manager.git`.
- Đã tạo repo, push/pull và đồng bộ lịch sử local với GitHub.
- PR #1: https://github.com/BangViet0311/devops-lab5-student-manager/pull/1
- PR #2: https://github.com/BangViet0311/devops-lab5-student-manager/pull/2
- Hai PR đã được `Bangviet-0311` review, approve và merge vào `develop`.
- Bản hoàn chỉnh đã tích hợp lịch sử PR, phát hành trên `main` và đồng bộ `develop`.
- Có đủ 8 ảnh thật trong `screenshots/`; ảnh conflict được tái hiện trong clone riêng.

**Hình thức: một người dùng hai tài khoản để mô phỏng Dev A/Dev B.**
Đây không phải review độc lập của hai người. Cần giảng viên chấp nhận hình thức
cá nhân thay cho nhóm hai người theo đề. Xem `BAO_CAO.md` để biết minh chứng.

## Tác giả
- Người thực hiện: [Điền họ tên và MSSV] — DevOps, Bài 5.
- Vai Dev A: `BangViet0311` (tài khoản chính).
- Vai Dev B: `Bangviet-0311` (tài khoản phụ của cùng người thực hiện).

## Tạo lại ảnh (tùy chọn, chỉ Windows)
Ứng dụng và 12 kiểm thử không cần thư viện ngoài. Các script chụp cửa sổ thật
trong `scripts/` cần Pillow, PowerShell và VS Code; không cần chạy khi chấm code.
`capture_evidence.py` hỗ trợ `log`, `branch`, `output`.
