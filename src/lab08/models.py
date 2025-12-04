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

# student = Student(
#     fio = "Hoang",
#     birthdate="2007/12/04", 
#     group="bivt-7",
#     gpa = 4.5
# )
# print(student.age())