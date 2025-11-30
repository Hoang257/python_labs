import json
import csv
import sys
from pathlib import Path


def csv_to_json(csv_path: str, json_path: str) -> None:
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent

    input_file = project_root / csv_path
    output_file = project_root / json_path

    if not input_file.exists():
        raise FileNotFoundError("Файл не существует")
    if not csv_path.lower().endswith(".csv"):
        raise ValueError("Некоректный формат файла")

    data = []
    try:
        with open(input_file, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
    except UnicodeDecodeError:
        raise UnicodeDecodeError("Некорректная кодировка файла")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)


# if __name__ == "__main__":
#     csv_to_json(r'python_labs\data_lab_05\people.csv', r'python_labs\data_lab_05\people_from_csv.json')
