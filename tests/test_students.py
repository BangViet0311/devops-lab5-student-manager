"""Kiểm thử bằng thư viện chuẩn, không cần pytest."""

import contextlib
import io
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from main import add_student, search_student
from student import Student


class StudentTests(unittest.TestCase):
    def setUp(self):
        self.students = [
            Student("SV001", "Nguyen Van A", 20, "K20"),
            Student("SV002", "Tran Thi B", 21, "K20"),
            Student("SV003", "Le Van C", 19, "K21"),
        ]
        self.output = io.StringIO()
        self.redirect = contextlib.redirect_stdout(self.output)
        self.redirect.__enter__()
        self.addCleanup(self.redirect.__exit__, None, None, None)

    def test_to_dict(self):
        self.assertEqual(self.students[0].to_dict(), {
            "student_id": "SV001", "name": "Nguyen Van A", "age": 20, "grade": "K20",
        })

    def test_string(self):
        self.assertEqual(str(self.students[0]),
                         "Student(id=SV001, name='Nguyen Van A', age=20, grade='K20')")

    def test_add_student(self):
        result = add_student(self.students, "SV004", "Pham Thi D", 22, "K19")
        self.assertIs(result, self.students)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[-1].student_id, "SV004")

    def test_duplicate_does_not_change_list(self):
        before = list(self.students)
        self.assertIs(add_student(self.students, "SV001", "Other", 22, "K19"), self.students)
        self.assertEqual(self.students, before)

    def test_add_to_empty_list(self):
        self.assertEqual(len(add_student([], "SV001", "A", 20, "K20")), 1)

    def test_search_name_case_insensitive(self):
        self.assertEqual(search_student(self.students, "vAn"),
                         [self.students[0], self.students[2]])

    def test_search_id_case_insensitive(self):
        self.assertEqual(search_student(self.students, "sv002"), [self.students[1]])

    def test_search_partial_id(self):
        self.assertEqual(search_student(self.students, "SV00"), self.students)

    def test_search_missing(self):
        self.assertEqual(search_student(self.students, "missing"), [])

    def test_search_empty_list(self):
        self.assertEqual(search_student([], "Van"), [])

    def test_empty_keyword_matches_all_as_in_lab(self):
        self.assertEqual(search_student(self.students, ""), self.students)

    def test_search_does_not_change_list(self):
        before = list(self.students)
        search_student(self.students, "Van")
        self.assertEqual(self.students, before)


if __name__ == "__main__":
    unittest.main()
