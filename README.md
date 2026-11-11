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
- Đã tạo repo, push main/develop ban đầu và hai nhánh feature.
- PR #1: https://github.com/BangViet0311/devops-lab5-student-manager/pull/1
- PR #2: https://github.com/BangViet0311/devops-lab5-student-manager/pull/2
- Bản local hoàn chỉnh được lưu trên nhánh `lab/local-completed`.
- `develop` online đang giữ base ban đầu để hai PR còn diff và có thể review.

**Hai PR đang chờ review, chưa merge; chưa hoàn tất bài 100%.**
Xem `HUONG_DAN_GITHUB.md` để hoàn tất.

## Tác giả
- Dev A: [Điền họ tên, MSSV, GitHub]
- Dev B: [Điền họ tên, MSSV, GitHub]
- Nhóm: [Điền số nhóm] — DevOps, Bài 5.
