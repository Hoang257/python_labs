# import json
# from pathlib import Path
# import csv

# def json_to_csv(json_path: str, csv_path: str) -> None:
#     json_path = Path(json_path)
#     csv_path = Path(csv_path)
#     # Проверка на наличие файла
#     if not json_path.exists():
#         raise FileNotFoundError(f'JSON файл не найден: {json_path}')
#     # Чтение файла JSON
#     try:
#         with json_path.open('r', encoding='utf-8') as file:
#             json_data = json.load(file)
#     except json.JSONDecodeError as e:
#         raise ValueError(f'Ошибка парсинга JSON: {e}') # неверный формат
#     if not json_data:
#         raise ValueError("Пустой JSON ")
    
#     if not all(isinstance(item, dict) for item in json_data):
#         raise ValueError("Все элементы JSON должны быть словарями")
    
#     unique_keys = set()
#     for item in json_data:
#         unique_keys.update(item.keys())
#     fieldnames = sorted(unique_keys)

#     # Запись данных в CSV
#     with csv_path.open('w', newline='', encoding='utf-8') as file:
#         writer = csv.DictWriter(file, fieldnames =fieldnames)
#         writer.writeheader()

#         for item in json_data:
#             row = {key: item.get(key, '') for key in fieldnames}
#             writer.writerow(row)


# import sys
# from pathlib import Path

# sys.path.append('src')  # путь к вашим модулям

# from lab05.json_csv import json_to_csv

# # Тест 1: Корректная конвертация
# json_to_csv("data/samples/test1.json", "data/out/test1.csv")

# # Проверяем результат
# with open("data/out/test1.csv", "r", encoding="utf-8") as f:
#     print(f.read())
import csv

with open(r'C:\Users\hoang\OneDrive\Desktop\laba\python_labs\data\check.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['a', 'b', 'c'])
print()