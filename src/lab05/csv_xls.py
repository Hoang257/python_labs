import json 
import csv
from pathlib import Path
from openpyxl import Workbook

def csv_xlsx(csv_path: str, xlsx_path: str) -> None:
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent.parent

    input_file =  project_root / csv_path
    output_file = project_root / xlsx_path

    if not input_file.exists():
        raise FileNotFoundError('Файл не сузествует')
    if not csv_path.lower().endswith('.csv'):
        raise ValueError('Некоректный формат файла')
    
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
    wb.save(r'python_labs\data_lab_05\people.xlsx')

csv_xlsx(r'python_labs\data_lab_05\people.csv', r'python_labs\data_lab_05\people.xlsx')
    