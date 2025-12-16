from pathlib import Path
import csv
from typing import List
import sys, os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lab08.models import Student


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exits()

    def _ensure_storage_exits(
        self,
    ) -> None:  # создание файла с заголовком, если его ещё нет
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["fio", "birthdate", "group", "gpa"])

    def _write_all_rows(self, rows):  # записывает данные в csv
        with open(self.path, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["fio", "birthdate", "group", "gpa"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def _validate_student_data(
        self, data: dict
    ) -> bool:  # проверяет корректность данных
        if not data:
            return False
        if set(data.keys()) != {"fio", "birthdate", "group", "gpa"}:
            return False
        try:
            if not isinstance(data["fio"], str) or not data["fio"].strip():
                return False
            datetime.strptime(data["birthdate"], "%Y/%m/%d")
            if not isinstance(data["group"], str) or not data["group"].strip():
                return False
            gpa = float(data["gpa"])
            return 0 <= gpa <= 5
        except (ValueError, TypeError, KeyError):
            return False

    def _read_all(self) -> List[dict]:  # реализация чтение строк из csv
        rows = []
        with open(self.path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row = dict(row)
                rows.append(row)
        return rows

    def list(self) -> List[Student]:  # возвращение всех студентов в виде списка
        rows = self._read_all()
        students = []

        for row in rows:
            if self._validate_student_data(row):
                try:
                    student = Student(
                        fio=row["fio"],
                        birthdate=row["birthdate"],
                        group=row["group"],
                        gpa=float(row["gpa"]),
                    )
                    students.append(student)
                except:
                    print("Неудалось создать студента")
        return students

    def add(self, student: Student) -> bool:  # добавление нового студента
        ex_student = self.list()
        for ex in ex_student:
            if ex.fio == student.fio:
                print(f"Студент {student.fio} уже существует")
                return False
        student_data = {
            "fio": student.fio,
            "birthdate": student.birthdate,
            "group": student.group,
            "gpa": str(student.gpa),
        }

        if not self._validate_student_data(student_data):
            print(f"Некорректные данные студента {student.fio}")
            return False

        with open(self.path, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writerow(student_data)
        return True

    def find(
        self, substr: str
    ) -> List[Student]:  # нахождение нового студента по подстроке fio
        list_students = self.list()
        found_student = []

        for student in list_students:
            if substr.lower() in student.fio.lower():
                found_student.append(student)
        return found_student

    def remove(self, fio):  # удалить запись(и) с данными fio
        rows = self._read_all()
        original_count = len(rows)

        filtered_rows = [row for row in rows if row["fio"] != fio]
        if len(filtered_rows) == original_count:
            print(f"Студент {fio} не найден")
            return False

        self._write_all_rows(filtered_rows)
        print(f"Студент {fio} удален")
        return True

    def update(self, fio, **fields) -> bool:  # обновление поля существующего студента
        rows = self._read_all()
        update = False

        for row in rows:
            if row["fio"] == fio:
                for key, value in fields.items():
                    if key in row:
                        row[key] = value
                if self._validate_student_data(row):
                    update = True
        if update:
            self._write_all_rows(rows)
            return True
        else:
            print(f"Студент {fio} не найден")
            return False


def main():
    group = Group(r"src\data\lab09\students.csv")
    student_1 = Student("Чан Хоанг", "2000/08/25", "Б-ИВТ-1", 4.5)
    student_2 = Student("Петя Петр", "2007/11/23", "Б-ИВТ-1", 5.0)
    student_3 = Student("Джек Сноу", "2003/02/21", "Б-ИВТ-1", 4.8)

    group.add(student_1)
    group.add(student_2)
    group.add(student_3)
    group.remove("Чан Хоанг")
    print(group.find("Чан Хоанг"))
    group.update("Петя Петр", gpa=3.5)
    final_students = group.list()
    for s in final_students:
        print(f"  {s.fio}, {s.group},  GPA: {s.gpa}")


if __name__ == "__main__":
    main()
