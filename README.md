# Лабораторная работа №1

##  Задание 1
```python
name = input('Введите ваше имя: ')
age = int(input('Введите ваш возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```

![Результат задания 1](/images/image-0.png)

##  Задание 2
```python
first_value = str(input('Введите превое число: '))
second_value = str(input('Введите второе число: '))
if ',' in first_value or second_value:
    first_value = first_value.replace(',', '.')
    second_value = second_value.replace(',', '.')
a = float(first_value)
b = float(second_value)
avg = round((a + b)/2,2)
sum = a + b
print(sum, avg)
```
![Результат задания 2](/images/image-1.png)

##  Задание 3
```python
price = float(input('Еnter the product price: '))
discount = float(input('Еnter the discount of the product:' ))
vat = float(input('Еnter vat of the product:' ))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f'Base after discount: {base}')
print(f'Vat: {vat}')
print(f'Final summ: {total}')
```
![Результат задания 3](/images/image-2.png)

##  Задание 4
```python
minutes = int(input('Минуты: '))
hour = minutes//60
min = minutes % 60
if min < 10: 
    min = '0' + f'{min}'
print(f'{hour}:{min}')
```
![Результат задания 4](/images/image-3.png)

##  Задание 5
```python
name = str(input('ФИО: ')).strip().title()
name = ' '.join(name.split())
initials = name.split()
initials = ''.join(initials[0] for initials in initials)
print(len(f'{name}'), initials)
```
![Результат задания 5](/images/image-4.png)

##  Задание 6
```python
n = int(input('Количество участников: '))
online = 0
offline = 0
for _ in range(n):
    data = input().split()
    format = data[-1]
    if format == 'False':
        offline+=1
    else:
        online+= 1
print(f'{online} {offline}')
```
![Результат задания 6](/images/image-5.png)

##  Задание 7
```python
a = 'QWERTYUIOPASDFGHJKLZXCVBNM'
b = '012345689'
ch = 'thisisabracadabraHt1eadljjl12ojh.'
word = ''
moves = []
for i in range(len(ch)):
    if ch[i] in a:
        word += ch[i]
        moves.append(i)
        break
for i in range(len(ch)):
    if ch[i] in b:
        word += ch[i+1]
        moves.append(i+1)
        break
for i in range(len(ch)):
    if moves[-1] - moves[-2] == i-moves[-1]:
        word += ch[i]
        moves.append(i)
if word[-1] == '.':
    print(word)
else:
    print('В конце дожна быть точка!!! ')
```
![Результат задания 7](/images/image-6.png)

# Лабораторная работа №2

##  Задание 1.1
```python
from typing import Union, List, Tuple 
def min_max(nums: List[Union[float, int]]) -> Tuple[Union[float, int]]:
    if not nums:
        return ('ValueError')
    return min(nums), max(nums)
print('\nТест min_max: ')
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))
```
![Результат задания 1.1](/images/image-8.png)

##  Задание 1.2
```python
def unique_sorted(nums: List[float|int]) -> List[float|int]:
    return sorted(set(nums)) #возвращаем отсортированный список
print("\nТест unique_sorted:")
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
![Результат задания 1.2](/images/image-10.png)
```
##  Задание 1.3
```python
def flatten(mat: List[List|Tuple]) -> List:
    result = [] 
    for element in mat:
        if not isinstance(element, (list, tuple)): #проверка на тип даных
            return ('TypeError')
        result.extend(element)
    return result
print("\nТест flatten:")
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1, 2], "ab"]))
```
![Результат задания 1.3](/images/image-12.png)

##  Задание 2.1
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat)==0:
        return []
    num_cols = len(mat[0]) #длина столбиков
    if any(len(row) != num_cols for row in mat):
        return ('ValueError')
    return [[mat[i][j] for i in range(len(mat))] for j in range(num_cols)]
print('\nТест transpose:')
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
```
![Результат задания 2.1](/images/image-13.png)

##  Задание 2.2
```python
def row_sums(mat: list[list[float|int]]) -> list[float]:
    if len(mat) == 0: 
        return []
    num_cols = len(mat[0])
    if any(len(row) != num_cols for row in mat):
        return ('ValueError')
    return[sum(row) for row in mat]
print('\nТест row_sums:')
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
```
![Результат задания 2.2](/images/image-14.png)
##  Задание 2.3
```python
def col_sums(mat: list(list[float|int])) -> list[float]:
    if len(mat) == 0:
        return []
    num_cols = len(mat[0])
    if any(len(row) != num_cols for row in mat):
        return ('ValueError')
    return[sum(mat[i][j] for i in range(len(mat))) for j in range(num_cols) ]
print('\nТест col_sums:')
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```
![Результат задания 2.2](/images/image-15.png)

## Задание 3
```python
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
```
![Результат задания 3](/images/image-16.png)

# Лабораторная работа №3

## Задание 1.1
```python
import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text:
        return []
    if casefold == True:
        text = text.casefold()
    if yo2e == True:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = re.sub("[^a-zа-яё0-9\s]","", text) # Удаление всех символов, кроме букв, цифр и пробелов
    text = re.sub(r'\s+', ' ', text).strip()
    return text

if __name__ == "__main__":
    test_cases = [
        "ПрИвЕт\nМИр\t",
        "ёжик, Ёлка" ,
        "Hello\r\nWorld",
        "  двойные   пробелы  "
    ]
    print('\nТест normalize:')
    for test in test_cases:
        print(f"{normalize(test, casefold= True, yo2e = True)}")
```
![Результат задания 1](/images/image-17.png)

## Задание 1.2
```python
def tokenize(text:str) -> list[str]:
    if not text:
        return []
    word = r'\b\w+(?:-\w+)*\b' # через регулярку задаем каким должен быть слово
    tokens = re.findall(word, text)
    return tokens

if __name__ == '__main__':
    test_cases = [
        "привет мир",
        "hello,world!!!",
        "по-настоящему круто",
        "2025 год",
        "emoji 😀 не слово"
    ]
    print("\nТест на tokenize")
    for test in test_cases:
        print(f"{tokenize(test)}")
```
![Результат задания 1.2](/images/image-18.png)

## Задание 1.3
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    dictionary = {}
    for token in tokens:
        dictionary[token] = dictionary.get(token, 0) + 1
    return dictionary

if __name__ == '__main__':
    test_cases = [
        "a","b","a","c","b","a"
        ]
    print("\nТест на count_freq")
    print(count_freq(test_cases))
```
![Результат задания 1.3](/images/image-19.png)

## Задание 1.4
```python
def top_n(freq: dict[str, int], n: int = None) -> list[str, int]:
    items = sorted(freq.items(), key= lambda x: (-x[1], x[0]))
    return items[:n]

if __name__ == '__main__':
    test_cases = [
        'aa bb b b d b b d a a'
        ]
    print('\nТест на top_words:')
    for test in test_cases:
        normalized = normalize(test)
        tokens = tokenize(normalized)
        freq = count_freq(tokens)
        top_words = top_n(freq,3)
    print(top_words)
```
![Результат задания 1.4](/images/image-20.png)

## Задание 2 

```python 
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.text import normalize, tokenize, count_freq, top_n
TABLE_MODE = True
def print_table(top_items):
    max_len_word = max(len(word) for word, _ in top_items)
    col_1 = "слово"
    col_2 = "частота"
    width = max(max_len_word, len(col_1))

    print('слово' + ' '* ((width+4)-len(col_1)) + "| частота" )
    print("-"*(width+4)*2)

    for word, count in top_items:
        print(f"{word}" + ' ' * ((width+4)-len(word)) + f'| {count}')

def main():
    text = sys.stdin.readline().strip()
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)

    total_words = len(tokens)
    unique_words = len(set(tokens))
    top_5 = top_n(freq,5)
    all_words = count_freq(tokens)

    if TABLE_MODE:
        print_table(top_5)
    else:
        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print("Топ-5:")
        for word, count in top_5:
            print(f"{word}:{count}")
if __name__ == "__main__":
    print(f"Табличный режим: {'ВКЛ' if TABLE_MODE else 'ВЫКЛ'}")
    main()
```
## Если включен режим показаа таблицы:
![Результат задания 1.4](/images/image-21.png)
## Если выключен режим показаа таблицы:
![Результат задания 1.4](/images/image-22.png)


# Лабораторная работа №4

## Задание A
```python
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Открыть файл на чтение в указанной кодировке и вернуть содержимое как одну строку.
    Обрабатывать ошибки: если файл не найден — поднимать FileNotFoundError (пусть падает), если кодировка не подходит — поднимать UnicodeDecodeError (пусть падает).
    НО: в докстринге опишите, как пользователь может выбрать другую кодировку (пример: encoding="cp1251")."""
    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    try:
        return p.read_text(encoding=encoding) # Считываем текст
    except FileNotFoundError:
        raise FileNotFoundError('Нет такого файла')
    except UnicodeDecodeError:
        raise UnicodeDecodeError('Неправильная кодировка')
    
text_1 = read_text(r'C:\Users\hoang\OneDrive\Desktop\laba\python_labs\data\input.txt')
print(text_1)


import csv
from typing import Iterable, Sequence

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """Создать/перезаписать CSV с разделителем ,.
    Если передан header, записать его первой строкой.
    Проверить, что каждая строка в rows имеет одинаковую длину (иначе ValueError)."""
    p = Path(path)
    rows = list(rows)
    if not rows:
        return 
    
    length = len(rows[0])
    for i in rows:
        if len(i)!= length:
            raise ValueError('Все строки должны быть одинаковой длины')
            
    with p.open('w', newline='', encoding='utf-8') as f: # коректирует перенос строк в csv
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL) # упраление кавычками, ставит только когда надо
        if header:
            writer.writerow(header)
        writer.writerows(rows)


text_2 = write_csv([("word","count"),("test",3)], r'python_labs/data/checkcsv')
print(text_2) 
 ```
 ## Задание B
 ```python
 import sys, os, csv
from pathlib import Path 
import argparse
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from func_from_3lab import normalize, tokenize, count_freq, top_n

def main():
    parser = argparse.ArgumentParser(description='Word freq report')#создаём объект парсера для обработки аргументов. 
    parser.add_argument('--in', dest='input_file', default='data/input.txt')
    parser.add_argument('--out', dest='output_file', default='data/output.txt')
    parser.add_argument('--encoding', default='utf-8')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding=args.encoding) as f:
            text = f.read()
    except FileNotFoundError:
        raise FileNotFoundError('Нет такого файла')
    except UnicodeDecodeError:
        raise UnicodeDecodeError('Неправильная кодировка')
    
    normalized_text = normalize(text)
    words = tokenize(normalized_text)
    freq = count_freq(words)

    total_words = len(words)
    unique_words = len(freq)

    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    os.makedirs(os.path.dirname(args.output_file), exist_ok=True)
    with open(args.output_file, 'w', encoding='utf-8') as f:
        f.write("word,count\n")
        for word, count in sorted_words:
            f.write(f"{word},{count}\n")
    
    print(f'Всего слов: {total_words}')
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in sorted_words[:5]:
        print(f"{word}: {count}")

if __name__ == '__main__':
    main()
 ```
## Тест-кейсы:
### запуск с обычным файлом

![Результат задания 1](/images/image-23.png)

![Результат задания 2](/images/image-24.png)

![Результат задания 3](/images/image-25.png)

### запуск с пустым файлом

![Результат задания 1](/images/image-26.png)

![Результат задания 2](/images/image-27.png)

![Результат задания 3](/images/image-28.png)

### запуск когда файл не существует
![Результат задания 1](/images/image-29.png)

# Лабораторная работа №5
## Задание A 
### (JSON -> CSV)

```python
import json 
import csv
import sys
from pathlib import Path
def json_to_csv(json_path: str, csv_path:str) -> None:
    # Преобразуем пути в Path объекты и нормализуем их
    input_path = Path(json_path).expanduser().resolve()
    output_path = Path(csv_path).expanduser().resolve()
    if not input_path.exists():
        raise FileNotFoundError(f"JSON file не найден: {json_path}")
    if input_path.stat().st_size == 0:
        raise ValueError("JSON файл пустой")
    
    with open(input_path, encoding='utf-8') as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError:
            raise ValueError("Неправильная кодировка")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")
    
    all_keys = set()
    for item in data:
        all_keys.update(item.keys())
    
    fieldnames = sorted(all_keys)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            row = {}
            for field in fieldnames:
                value = item.get(field)
                row[field] = str(value) if value is not None else ""
            writer.writerow(row)
if __name__ == "__main__":
    json_to_csv("data_lab_05\people.json", "data_lab_05\people_from_json.csv")
```
## Тест-кейсы:
### запуск с обычным файлом
![Исходный JSON](/images/image-30.png)
![Результат конвертации из JSON в CSV](/images/image-31.png)

### запуск с несуществующим файлом
![Результат запуска](/images/image-32.png)

### запуск с пустым файлом
![Результат запуска](/images/image-33.png)


### (CSV -> JSON)
```python
import json 
import csv
import sys
from pathlib import Path
def csv_to_json(csv_path: str, json_path: str) -> None:
    # Преобразуем пути в Path объекты и нормализуем их
    input_file = Path(csv_path).expanduser().resolve()
    output_file = Path(json_path).expanduser().resolve()

    if not input_file.exists():
        raise FileNotFoundError('Файл не существует')
    if not csv_path.lower().endswith('.csv'):
        raise ValueError('Некоректный формат файла')
    
    data = []
    try:
        with open(input_file, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
    except UnicodeDecodeError:
        raise UnicodeDecodeError('Некорректная кодировка файла')
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
if __name__ == "__main__":
    csv_to_json(r'python_labs\data_lab_05\people.csv', r'python_labs\data_lab_05\people_from_csv.json')
```
## Тест-кейсы:
### запуск с обычным файлом
![Исходный JSON](/images/image-34.png)
![Результат конвертации из CSV в JSON](/images/image-35.png)

### запуск с несуществующим файлом
![Результат запуска](/images/image-36.png)

### запуск с пустым файлом
![Результат запуска](/images/image-37.png)

## Задание B (CSV → XLSX)
```python
import csv
from pathlib import Path
from openpyxl import Workbook

def csv_xlsx(csv_path: str, xlsx_path: str) -> None:
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent

    input_file = project_root / csv_path
    output_file = project_root / xlsx_path

    if not input_file.exists():
        raise FileNotFoundError('Файл не существует')
    if not csv_path.lower().endswith('.csv'):
        raise ValueError('Некорректный формат файла')

    output_file.parent.mkdir(parents=True, exist_ok=True)

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    try:
        with open(input_file, 'r', encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                ws.append(row)
    except UnicodeEncodeError:
        raise UnicodeEncodeError('Некорректная кодировка файла')
    wb.save(output_file)
```

## запуск с обычным файлом

![Исходный файл CSV](/images/image-38.png)
![Результат конвертации из CSV в XLSX](/images/image-39.png)


# Лабораторная работа №6
## Задание A - cli_convert
```python
import argparse
import sys, os
from pathlib import Path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from lab05.csv_json import csv_to_json
from lab05.csv_xls import csv_xlsx
from lab05.json_csv import json_to_csv

def main():
    parser = argparse.ArgumentParser(description='Конверты данных')
    subparsers = parser.add_subparsers(dest='command')

    json_csv_parser = subparsers.add_parser('json2csv', help='конвертирует из json в csv')
    json_csv_parser.add_argument('--input', required=True, help='Входной файл')
    json_csv_parser.add_argument('--output', required=True, help='Выходной файл')

    csv_json_parser = subparsers.add_parser('csv2json', help='конвертирует из csv в json')
    csv_json_parser.add_argument('--input', required=True, help='Входной файл')
    csv_json_parser.add_argument('--output', required=True, help='Выходной файл')

    csv_xlsx_parser = subparsers.add_parser('csv2xlsx', help='конвертирует из csv в xlsx')
    csv_xlsx_parser.add_argument('--input', required=True, help='Входной файл')
    csv_xlsx_parser.add_argument('--output', required=True, help='Выходной файл')

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        sys.exit(1)

    input_file = Path(args.input).expanduser()
    if not input_file.is_absolute():
        input_file = (Path.cwd() / input_file).resolve()
    else:
        input_file = input_file.resolve()

    output_file = Path(args.output).expanduser()
    if not output_file.is_absolute():
        output_file = (Path.cwd() / output_file).resolve()
    else:
        output_file = output_file.resolve()

    if not input_file.exists():
        print(f"Ошибка: входной файл не найден: {input_file}")
        sys.exit(1)

    if args.command == 'json2csv':
        json_to_csv(str(input_file), str(output_file))
    elif args.command == 'csv2json':
        csv_to_json(str(input_file), str(output_file))
    elif args.command == 'csv2xlsx':
        csv_xlsx(str(input_file), str(output_file))
            
if __name__ == "__main__":
    main()
```
## сводка -h команд
### python src/lab06/cli_convert.py json2csv -h
### python src/lab06/cli_convert.py csv2json -h
### python src/lab06/cli_convert.py csv2xlsx -h

## сводка команд для проверки
### python src/lab06/cli_convert.py json2csv --input src\lab06\data\people.json --output src\lab06\data\people.csv
### python src/lab06/cli_convert.py csv2json --input src\lab06\data\people.csv --output src\lab06\data\people.json
### python src/lab06/cli_convert.py csv2xlsx --input src\lab06\data\people.csv --output src\lab06\data\people.xlsx

## Задание B - cli_text

```python
import argparse
import sys, os
from pathlib import Path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lab03.text import tokenize, count_freq, top_n

def num_str(input_path, number_lines=False): 
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            line_num = 1
            for line in f:
                if number_lines:
                    print(f"{line_num}: {line}", end='')
                    line_num+=1
                else:
                    print(line, end='')
    except FileNotFoundError:
        print('Файл не найден')
        sys.exit(1)

def stat_text(input_path: Path, top=5):
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print("Файл не найден:", input_path)
        sys.exit(1)

    tokens = tokenize(text)
    freq = count_freq(tokens)
    top_words = top_n(freq, top)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(set(tokens))}")
    print("Топ слов:")

    for word, count in top_words:
        print(f"{word}: {count}")

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Выводит содержимое файла")
    cat_parser.add_argument('--input', required=True, help='Путь к текущему файлу')
    cat_parser.add_argument('-n', action="store_true", help='Нумерует строки')

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument('--input', required=True, help='Путь к текущему файлу')
    stats_parser.add_argument('--top', type=int, default=5, help='сколько в топе должно быть слов, по умолчанию 5')

    args = parser.parse_args()

    if args.command == 'cat':
        input_path = Path(args.input)
        num_str(input_path, number_lines=args.n)
    elif args.command == 'stats':
        input_path = Path(args.input, top=args.top)
        stat_text(input_path)

if __name__ == "__main__":
    main()
```
## сводка -h команд
### python src/lab06/cli_text.py cat --input src\lab06\data\test.txt -h
### python src/lab06/cli_text.py stats --input src\lab06\data\test.txt -h
## сводка команд
#### просто выводит текст 
### python src/lab06/cli_text.py stats --input src\lab06\data\test.txt
#### выводит текст с нумерацием
### python src/lab06/cli_text.py cat --input src\lab06\data\test.txt -n
## Результат работы:
### подсказки
![подсказки](/images/image-40.png)
![подсказки](/images/image-41.png)
### обычная работа
![результат](/images/image-42.png)
![результат](/images/image-43.png)
![результат](/images/image-44.png)


# Лабораторная работа №7
## Задание 1 (автотесты для всех функций модуля)
```python
import pytest
import sys, os
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "in_data, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("       ", ""),
        ("123  456", "123 456"),
        ("Много\t\t\tтабов", "много табов"),
    ],
)
def test_normalize(in_data, expected):
    assert normalize(in_data) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
        ("    ", []),
        ("!!!", []),
        ("a-b-c", ["a-b-c"]),
        ("кириллица and english", ["кириллица", "and", "english"]),
    ],
)
def test_tokenize_basic(text, expected):
    assert tokenize(text) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        ([], {}),
        (["word"], {"word": 1}),
        (["word", "Word", "WORD"], {"word": 1, "Word": 1, "WORD": 1}),
        (["word", "word", "word"], {"word": 3}),
    ],
)
def test_count_freq(tokens, expected):
    assert count_freq(tokens) == expected


@pytest.mark.parametrize(
    "freq_dict, n, expected",
    [
        ({"a": 3, "b": 2, "c": 1}, 2, [("a", 3), ("b", 2)]),
        ({}, 1, []),
        ({"c": 3, "b": 3, "v": 3}, 3, [("b", 3), ("c", 3), ("v", 3)]),
        ({"a": 1, "b": 1}, 5, [("a", 1), ("b", 1)]),
        ({"a": 3, "b": 3, "c": 2}, 2, [("a", 3), ("b", 3)]),
    ],
)
def test_top_n(freq_dict, n, expected):
    assert top_n(freq_dict, n) == expected
```


## Задание 2 (автотесты для функций конвертаций файлов)
```python
import pytest
import sys, os
import csv
import json
from pathlib import Path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.lib.csv_json import csv_to_json
from src.lib.json_csv import json_to_csv

def test_json_to_csv_base(tmp_path: Path): 
    src = tmp_path / "people.json" # готовая временная директория (фикстура pytest)
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())

def test_json_to_csv_file_not_found(): # когда нет файла
     with pytest.raises(FileNotFoundError, match="JSON file не найден"):
          json_to_csv("not_ex_file.json", "output.csv")


def test_json_to_csv_file_is_empty(tmp_path): # когда файл пустой
    src = tmp_path / 'empty_file.json'
    dst = tmp_path / "output.csv"

    src.write_text('')
    with pytest.raises(ValueError, match="JSON файл пустой"):
        json_to_csv(str(src), str(dst))
    

def test_json_to_csv_not_a_dict(tmp_path): # когда не все элементы словари
    src = tmp_path / 'invalid.json'
    dst = tmp_path / "output.csv"

    data = 'не список словарей'
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    with pytest.raises(ValueError, match="Все элементы JSON должны быть словарями"):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_special_characters(tmp_path):
    src = tmp_path / 'input.json'
    dst = tmp_path / "output.csv"

    data = [
        {"name": "Хоанг", "age": "18"},
        {"name": "Hoàng", "age": "19"},
    ]
    
    src.write_text(json.dumps(data, ensure_ascii= False, indent=2), encoding='utf-8')
    json_to_csv(str(src), str(dst))

    assert dst.exists()

    with open(dst, 'r', encoding='utf-8') as f:
        content = f.read()
    assert "Hoàng" in content
    assert 'Хоанг' in content

def test_json_to_csv_none_values(tmp_path):
    src = tmp_path / "none.json"
    dst = tmp_path / "output.csv"

    data = [
        {"name": "ALice", "age": None, "city": None},
        {"name": "Bob", "age": '18', "city": None},
    ]
    src.write_text(json.dumps(data, ensure_ascii= False, indent= 2), encoding= 'utf-8')
    json_to_csv(str(src), str(dst))
    
    with open(dst, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    assert rows[0]['age'] == ''
    assert rows[1]['city'] == ''
    


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    with open(src, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerow({"name": "Alice", "age": "22"})
        writer.writerow({"name": "Bob", "age": "25"})

    csv_to_json(str(src), str(dst))
    assert dst.exists()
    with open(dst, 'r', encoding='utf-8') as f:
            data = json.load(f)
    assert len(data) == 2
    assert data[0]["name"] == "Alice"
    assert data[1]["name"] == "Bob"
    assert data[0]["age"] == "22"
    assert data[1]["age"] == "25"


def test_csv_to_json_file_not_found():
    with pytest.raises(FileNotFoundError, match='Файл не существует'):
        csv_to_json("not_ex_file.csv", "output.json")

def test_csv_to_json_not_right_format(tmp_path: Path):
    src = tmp_path / "file.txt"  
    dst = tmp_path / "output.json"
    
    src.write_text("some content", encoding='utf-8')
    
    with pytest.raises(ValueError, match="Некоректный формат файла"):
        csv_to_json(str(src), str(dst))
    


def test_csv_to_json_empty_cells(tmp_path: Path):
        src = tmp_path / "empty.csv"
        dst = tmp_path / "output.json"
        with open(src, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
            writer.writeheader()
            writer.writerow({"name": "Alice", "age": "22", "city": "Moscow"})
            writer.writerow({"name": "Bob", "age": "", "city": "SPb"})                
            writer.writerow({"name": "Charlie", "age": "30", "city": ""})
        csv_to_json(str(src), str(dst))
        
        with open(dst, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        assert len(data) == 3
        assert data[1]["age"] == ""  
        assert data[2]["city"] == ""  



def test_csv_to_json_different_colums(tmp_path: Path):
    src = tmp_path / 'input.csv'
    dst = tmp_path / 'output.json'

    with open(src, 'w', encoding='utf-8', newline='') as f:
        f.write('name,age,city\n')
        f.write("Alice,22,Moscow\n")
        f.write("Bob,25,\n")  # Пустое значение для city
        f.write("Charlie,,SPb\n")  # Пустое значение для age

    csv_to_json(str(src), str(dst))

    with open(dst, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    assert len(data) == 3
    assert data[1]['city'] == ''  # Проверяем что значение пустое
    assert data[2]['age'] == ''   # Проверяем что age пустое

```

### Запуск тестов в CLI с покрытием
![результат](/images/image-45.png)


# Лабораторная работа №8
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
![результат](/images/image-48.png)
![результат](/images/image-47.png)
![результат](/images/image-46.png)

# Лабораторная работа №9
## Задание 1 
```python
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

```
### Результат работы функции 
![результат](/images/image-49.png)
![результат](/images/image-50.png)

# Лабораторная работа №9
## Теория
```python
Стек (LIFO)
push/pop/peek: O(1)
Применение: отмена действий (undo), DFS, проверка скобок.
Очередь (FIFO)

enqueue/dequeue/peek: O(1)
Применение: обработка задач, BFS, буферы.
В Python: используй collections.deque.
Односвязный список
Узел: value, next.
Плюсы: вставка/удаление в начале O(1).
Минусы: доступ по индексу O(n); нет прямого доступа к предыдущему элементу.
Операции:
prepend: O(1)
append (с tail): O(1)
поиск: O(n)

Двусвязный список
Узел: value, next, prev.
Плюсы: удаление по ссылке O(1); обход в обе стороны.
Минусы: больше памяти на узел; сложнее в реализации.
Операции (с head/tail):
вставка/удаление в начале/конце: O(1)
удаление по ссылке: O(1)
доступ по индексу/поиск: O(n)
```


## Задание А (structures)
```python
from collections import deque
from typing import Any, Optional


class Stack:
    def __init__(self):
        self._data = []

    def push(self, item: Any) -> None:
        self._data.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Стек пустой")
        return self._data.pop()

    def peek(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Stack({self._data})"

    def __str__(self) -> str:
        return f"Stack(вершина ->{self._data[-1] if self._data else 'пусто'})"

    def __len__(self) -> int:
        return len(self._data)


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item: Any) -> None:
        self._data.append(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Пустая очередь")
        return self._data.popleft()

    def peek(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Queue({list(self._data)})"

    def __str__(self) -> str:
        return f"Queue(начало -> {self._data[0] if self._data else 'пусто'})"

    def __len__(self) -> int:
        return len(self._data)


if __name__ == "__main__":

    print("Тестирование Stack")
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(f"Длина стека: {len(stack)}")
    print(f"Верхний элемент: {stack.peek()}")

    popped = stack.pop()
    print(f"Извлеченный элемент: {popped}")
    print(f"Длина после pop: {len(stack)}")
    print(f"Пустой ли стек: {stack.is_empty()}")

    stack.pop()
    stack.pop()
    print(f"Пустой ли стек после очистки: {stack.is_empty()}")

    try:
        stack.pop()
    except IndexError as e:
        print(f"Ошибка при pop из пустого стека: {e}")

    print()

    print("Тестирование Queue")
    queue = Queue()

    queue.enqueue("первый")
    queue.enqueue("второй")
    queue.enqueue("третий")

    print(f"Длина очереди: {len(queue)}")
    print(f"Первый элемент: {queue.peek()}")

    dequeued = queue.dequeue()
    print(f"Извлеченный элемент: {dequeued}")
    print(f"Длина после dequeue: {len(queue)}")
    print(f"Пустая ли очередь: {queue.is_empty()}")

    queue.dequeue()
    queue.dequeue()
    print(f"Пустая ли очередь после очистки: {queue.is_empty()}")

    try:
        queue.dequeue()
    except IndexError as e:
        print(f"Ошибка при dequeue из пустой очереди: {e}")
```
## Задание B (linked_list)
```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
        self._tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    def prepend(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

        if self._tail is None:
            self._tail = new_node

        self._size += 1

    def insert(self, idx, value):
        if idx < 0:
            raise IndexError("Индекс меньше нуля")
        if idx > self._size:
            raise IndexError("Индекс больше длины коллекции")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        curr = self.head
        for _ in range(idx - 1):
            curr = curr.next

        new_node = Node(value, next=curr.next)
        curr.next = new_node
        self._size += 1

    def get(self, idx):
        if idx < 0 or idx >= self._size:
            raise IndexError("Индекс вне диапазона")

        curr = self.head
        for _ in range(idx):
            curr = curr.next

        return curr.value

    def remove_at(self, idx):
        if idx < 0 or idx >= self._size:
            raise IndexError("Индекс вне диапазона")

        if idx == 0:
            value = self.head.value
            self.head = self.head.next
            self._size -= 1

            if self.head is None:
                self._tail = None

            return value

        curr = self.head
        for _ in range(idx - 1):
            curr = curr.next

        value = curr.next.value
        curr.next = curr.next.next

        if curr.next is None:
            self._tail = curr

        self._size -= 1
        return value

    def remove(self, value):

        if self.head is None:
            return False

        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1

            if self.head is None:
                self._tail = None

            return True

        curr = self.head
        while curr.next is not None and curr.next.value != value:
            curr = curr.next

        if curr.next is None:
            return False

        curr.next = curr.next.next
        self._size -= 1

        if curr.next is None:
            self._tail = curr

        return True

    def find(self, value):

        curr = self.head
        idx = 0

        while curr is not None:
            if curr.value == value:
                return idx
            curr = curr.next
            idx += 1

        return -1

    def clear(self):

        self.head = None
        self._tail = None
        self._size = 0

    def is_empty(self):

        return self._size == 0

    def __iter__(self):

        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next

    def __len__(self):

        return self._size

    def __str__(self):

        if self.head is None:
            return "None"

        return " -> ".join(f"[{value}]" for value in self) + " -> None"

    def __repr__(self):

        vals = list(self)
        return f"SinglyLinkedList({vals})"

    def __getitem__(self, idx):
        return self.get(idx)


if __name__ == "__main__":
    lst = SinglyLinkedList()
    print(f"Пустой список: {lst}")
    print(f"Длина: {len(lst)}")

    lst.append(10)
    lst.append(20)
    lst.append(30)
    print(f"После append 10,20,30: {lst}")
    print(f"Длина: {len(lst)}")

    lst.prepend(5)
    print(f"После prepend 5: {lst}")
    print(f"Длина: {len(lst)}")

    lst.insert(2, 15)
    print(f"После insert 15 на позицию 2: {lst}")
    print(f"Длина: {len(lst)}")

    print("Итерация по списку:")
    for item in lst:
        print(f"  {item}")

    print(f"repr: {repr(lst)}")
```
### Результат работы 
![результат](/images/image-51.png)
![результат](/images/image-52.png)