"""Student Manager — chương trình minh họa DevOps Lab 5."""

from student import Student


def search_student(students: list, keyword: str) -> list:
    """Tìm theo một phần tên hoặc mã, không phân biệt hoa thường."""
    keyword_lower = keyword.lower()
    results = [
        student for student in students
        if keyword_lower in student.name.lower()
        or keyword_lower in student.student_id.lower()
    ]
    if results:
        print(f"Tìm thấy {len(results)} sinh viên với từ khóa '{keyword}':")
        for student in results:
            print(f"  {student}")
    else:
        print(f"Không tìm thấy sinh viên nào với từ khóa '{keyword}'")
    return results


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
    print("\n--- Tìm kiếm ---")
    search_student(students, "Van")


if __name__ == "__main__":
    main()
