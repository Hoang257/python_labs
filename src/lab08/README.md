# Лабораторная работа №7
## Задание models 
```python
from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class Student:
    fio : str
    birthdate : str
    group : str
    gpa : float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y/%m/%d")
        except ValueError:
            raise ValueError('Warning: birthdate format might be invalid')
        if not (0.0 <= self.gpa <= 5.0):
            raise ValueError("gpa must be between 0 and 5")
        
    def age(self) -> int:
        birth_data = datetime.strptime(self.birthdate, "%Y/%m/%d").date()
        today = date.today()
        if (today.month, today.day) < (birth_data.month, birth_data.day):
            age = today.year - birth_data.year -1
        else:
            age = today.year - birth_data.year

        return age
    
    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    
    @classmethod 
    def from_dict(cls, data):
        for key in ["fio", "birthdate", "group", "gpa"]:
            if key not in data:
                raise ValueError("Отсутствует поле")
        return cls(
            fio = str(data['fio']),
            birthdate = str(data["birthdate"]),
            group = str(data["group"]),
            gpa = float(data["gpa"]),
        )

    def __str__(self):
            return f"Name: {self.fio}, birthday: {self.birthdate}, group: {self.group}, GPA: {self.gpa}"
```
## Задание serialize
```python
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
```
### Результат работы функции 
![результат](/images/image-46.png)
![результат](/images/image-47.png)
![результат](/images/image-48.png)



