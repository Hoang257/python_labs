import csv
from pathlib import Path
from openpyxl import Workbook

def csv_xlsx(csv_path: str, xlsx_path: str) -> None:
    # Преобразуем пути в Path объекты и нормализуем их
    input_file = Path(csv_path).expanduser().resolve()
    output_file = Path(xlsx_path).expanduser().resolve()

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