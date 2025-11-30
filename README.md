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
