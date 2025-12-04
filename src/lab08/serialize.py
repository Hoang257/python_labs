import json
from pathlib import Path
from typing import List
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from lab08.models import Student


def student_to_json(students: List[Student], path: str) -> None:
    data = [student.to_dict() for student in students]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str | Path):
    input_path = Path(path)
    if not input_path.exists():
        raise FileNotFoundError(f"JSON file не найден: {input_path}")

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список студентов")

    student_list = []
    for item in data:
        student = Student.from_dict(item)
        student_list.append(student)

    return student_list


if __name__ == "__main__":
    test_students = [
        Student("Чан Хоанг", "2000/08/25", "Б-ИВТ-1", 4.5),
        Student("Петя Петр", "2007/11/23", "Б-ИВТ-1", 5.0),
        Student("Джек Сноу", "2003/02/21", "Б-ИВТ-1", 4.8),
        Student("John Sina", "2011/06/10", "Б-ИВТ-1", 3.7),
        Student("Ли Сяо Мин", "2004/11/25", "Б-ИВТ-1", 4.5),
        Student("Отличник", "2000/01/01", "Б-ИВТ-1", 5.0),
        Student("Троечник", "2000/01/01", "Б-ИВТ-1", 3.0),
        Student("Двоечник", "2000/01/01", "Б-ИВТ-1", 2.0),
    ]
    in_file = r"data_lab_08\students_input.json"
    student_to_json(test_students, in_file)
    out_load = students_from_json(in_file)
    for student in out_load:
        print(student)
