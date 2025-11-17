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
    current_file = Path(__file__) 
    project_root = current_file.parent.parent.parent 
    
    input_path = project_root / json_path
    output_path = project_root / csv_path
    if not input_path.exists():
        raise FileNotFoundError(f"JSON file не найден: {json_path}")
    
    with open(input_path, encoding='utf-8') as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError:
            raise ValueError("Неправильная кодировка")
    if not data:
        raise ValueError('JSON пуст')
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
json_to_csv("data_lab_05\people.json", "data_lab_05\people_from_json.csv")
```
## Тест-кейсы:
### запуск с обычным файлом
![Исходный JSON](/images/image-30.png)
![Результат конвертации из JSON в CSV](/images/image-30.png)

### запуск с несуществующим файлом
![Результат запуска](/images/image-32.png)

### (CSV -> JSON)
```python
import json 
import csv
import sys
from pathlib import Path
def csv_to_json(csv_path: str, json_path: str) -> None:
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent.parent

    input_file = project_root / csv_path
    output_file = project_root / json_path

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

csv_to_json(r'python_labs\data_lab_05\people.csv', r'python_labs\data_lab_05\people_from_csv.json')
```
