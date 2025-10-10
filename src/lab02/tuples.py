# name_input = input('ФИО: ').strip()
# group_input = input('Группа: ').strip()
# gpa_input = float(input('GPA: ').strip())
# student_data = (name_input, group_input, gpa_input)
def format_record(rec: tuple([str, str, float])) -> str:
    if not isinstance(rec, tuple):
        return TypeError("Аргкмент должен быть кортежем")
    if len(rec) < 3:
        return ValueError("Кортеж должен содержать 3 элемента")
    if not isinstance(rec[2], float):
        return TypeError("3 элемент должен быть плавающим числом")
    name, group, gpa = rec
    name_set = ' '.join(name.strip().split()).title()
    parts_name = name_set.split()
    if len(parts_name) < 2:
        raise ValueError('ФИО дожен быть длинее двух слов')
    surname = parts_name[0]
    initials = [x[0] + '.' for x in parts_name[1:]]
    name_end = f"{surname} {''.join(initials)}"
    group_set= group
    gpa_set = f'{gpa:.2f}'
    return f'{name_end}, гр. {group_set}, GPA {gpa_set}'

# result = format_record(student_data)
# print(result)

if __name__ == "__main__":
    # Тест-кейсы из задания
    test_cases = [
        ("Иванов Иван Иванович", "BIVT-25", 4.6),
        ("Петров Пётр", "IKBO-12", 5.0),
        ("Петров Пётр Петрович", "IKBO-12"),
        ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
    ]
    
    for test in test_cases:
        print(format_record(test))