"""Student Manager — mô hình sinh viên."""


class Student:
    """Lưu thông tin mã, họ tên, tuổi và khóa học của sinh viên."""

    def __init__(self, student_id: str, name: str, age: int, grade: str):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self) -> str:
        return (
            f"Student(id={self.student_id}, name='{self.name}', "
            f"age={self.age}, grade='{self.grade}')"
        )

    def to_dict(self) -> dict:
        """Chuyển thông tin sinh viên thành dictionary."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
        }
