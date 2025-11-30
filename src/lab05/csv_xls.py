import csv
from pathlib import Path
from openpyxl import Workbook


def csv_xlsx(csv_path: str, xlsx_path: str) -> None:
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent

    input_file = project_root / csv_path
    output_file = project_root / xlsx_path

    if not input_file.exists():
        raise FileNotFoundError("Файл не существует")
    if not csv_path.lower().endswith(".csv"):
        raise ValueError("Некорректный формат файла")

    output_file.parent.mkdir(parents=True, exist_ok=True)

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    try:
        with open(input_file, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                ws.append(row)
    except UnicodeEncodeError as exc:
        raise UnicodeEncodeError("Некорректная кодировка файла") from exc
    wb.save(output_file)
