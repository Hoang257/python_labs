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

