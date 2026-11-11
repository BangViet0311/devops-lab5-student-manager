"""Student Manager — chương trình minh họa DevOps Lab 5."""

from student import Student


def main():
    """Hiển thị danh sách sinh viên mẫu."""
    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)
    students = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
    ]
    for student in students:
        print(f"  {student}")
    print(f"\nTotal: {len(students)} students")


if __name__ == "__main__":
    main()
