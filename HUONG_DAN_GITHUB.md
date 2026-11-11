# Hoàn tất phần GitHub

## 1. Tạo remote
Dev A đăng nhập GitHub và tạo repo public `devops-lab5-student-manager` rỗng
(không tạo README/.gitignore). Trong terminal tại thư mục dự án:

```powershell
git remote -v
```

Origin đã được cấu hình thành `https://github.com/BangViet0311/devops-lab5-student-manager.git`.
Trong các lệnh bên dưới, thay `YOUR_USERNAME` bằng `BangViet0311`.
Đăng nhập bằng Git Credential Manager khi được hỏi.
Không đặt token trong URL, source code, báo cáo hoặc ảnh chụp.

## 2. Tạo hai PR có diff thật từ lịch sử đã có
Main/develop local đã chứa các feature. Nếu push toàn bộ ngay thì PR từ
feature cũ vào develop sẽ không còn diff. Với **repo GitHub mới và rỗng**,
làm theo thứ tự dưới đây để tái hiện đúng quá trình review:

```powershell
git push origin 8a8e86c:refs/heads/main
git push origin 8a8e86c:refs/heads/develop
git push origin feature/add-student feature/search-student
```

Nếu remote không rỗng hoặc lệnh bị từ chối, dừng kiểm tra, không force-push.

1. Tạo PR `feature/add-student` → `develop`.
   Tiêu đề: `feat: Add student function`.
   Mô tả: thêm SV004, kiểm tra mã trùng; chạy `python src/main.py` trên nhánh PR.
2. Thêm Dev B vào Settings → Collaborators. Dev B chấp nhận lời mời,
   mở Files changed, nhận xét thật, Review changes → Approve.
   Tác giả không thể tự approve PR của mình.
3. Merge PR #1 bằng **Create a merge commit**, không squash/rebase.
4. Tạo PR `feature/search-student` → `develop`, tiêu đề
   `feat: Search student by name or ID`.
5. PR này có thể conflict vì hai hàm cùng được thêm tại một vị trí.
   Để giữ đúng quy trình PR, dùng một clone mới, không dùng develop local đã merge:

```powershell
# Chạy ở thư mục cha, chọn tên thư mục mới chưa tồn tại
git clone https://github.com/YOUR_USERNAME/devops-lab5-student-manager.git student-manager-review
cd student-manager-review
git switch feature/search-student
git merge origin/develop
```

Mở `src/main.py`, bỏ marker và giữ cả add_student/search_student cùng cả hai
lời gọi trong main. Hai hàm phải nằm trước `if __name__ == "__main__"`.

```powershell
python src/main.py
git add src/main.py
git commit -m "merge: resolve add and search conflict for review"
git push origin feature/search-student
```

Nhờ người thứ hai review PR #2 rồi merge bằng merge commit. Chụp ảnh hai PR
và review trước khi tiếp tục.

## 3. Đồng bộ lịch sử local đã hoàn thành với remote
Quay lại **thư mục dự án ban đầu**. Giữ cả lịch sử PR remote và lịch sử local:

```powershell
git fetch origin
git switch develop
git merge --no-ff origin/develop -m "merge: synchronize reviewed GitHub features"
```

Nếu có conflict, giữ bản hoàn chỉnh có cả hai tính năng, chạy kiểm thử rồi
`git add` đúng file và commit. Không force-push.

```powershell
git merge --no-ff main -m "merge: sync final documentation and tests"
git push -u origin develop
git switch main
git merge --no-ff origin/main -m "merge: synchronize remote main"
git merge --no-ff develop -m "merge: release reviewed changes"
git push -u origin main
git pull --ff-only origin main
```

Dev B clone hoặc pull repo trên máy mình và chạy demo.
Nếu bật bảo vệ nhánh, thay push trực tiếp bằng PR theo yêu cầu bảo vệ.

## 4. Minh chứng và nộp
Xem `screenshots/README.md`. Với conflict README đã resolve, có thể xem
log thật tại `evidence/`; nếu cần ảnh conflict trong editor, tái hiện trong
một clone thực hành riêng từ hai nhánh README (merge B trước rồi A).
Không thay đổi hoặc xóa lịch sử dự án để dựng ảnh.

Điền họ tên, MSSV, nhóm, URL repo trong README và báo cáo. Chụp ảnh thật,
commit tài liệu đã cập nhật, push và tạo lại ZIP nộp LMS.
Chỉ xóa nhánh bằng `git branch -d TEN_NHANH` khi đã kiểm tra merge;
không dùng `-D` để ép xóa.
