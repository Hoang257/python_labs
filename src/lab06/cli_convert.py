import argparse
import sys, os
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from lab05.csv_json import csv_to_json
from lab05.csv_xls import csv_xlsx
from lab05.json_csv import json_to_csv


def main():
    parser = argparse.ArgumentParser(description="Конверты данных")
    subparsers = parser.add_subparsers(dest="command")

    json_csv_parser = subparsers.add_parser(
        "json2csv", help="конвертирует из json в csv"
    )
    json_csv_parser.add_argument("--input", required=True, help="Входной файл")
    json_csv_parser.add_argument("--output", required=True, help="Выходной файл")

    csv_json_parser = subparsers.add_parser(
        "csv2json", help="конвертирует из csv в json"
    )
    csv_json_parser.add_argument("--input", required=True, help="Входной файл")
    csv_json_parser.add_argument("--output", required=True, help="Выходной файл")

    csv_xlsx_parser = subparsers.add_parser(
        "csv2xlsx", help="конвертирует из csv в xlsx"
    )
    csv_xlsx_parser.add_argument("--input", required=True, help="Входной файл")
    csv_xlsx_parser.add_argument("--output", required=True, help="Выходной файл")

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        sys.exit(1)

    current_file = Path(__file__).resolve()
    python_labs_root = current_file.parent.parent.parent

    def normalize_path(path_str: str) -> Path:
        # Создаём объект Path из строки и разворачиваем ~ в домашнюю директорию пользователя
        path_obj = Path(path_str).expanduser()
        # Проверяем, является ли путь абсолютным (начинается с C:\ или /)
        if not path_obj.is_absolute():
            # Если путь относительный, добавляем его к корню python_labs и получаем абсолютный путь
            path_obj = (python_labs_root / path_obj).resolve()
        else:
            # Если путь уже абсолютный, просто нормализуем его (убираем .. и .)
            path_obj = path_obj.resolve()
        try:
            # Преобразуем абсолютный путь в относительный относительно python_labs_root
            return path_obj.relative_to(python_labs_root)
        except ValueError as exc:
            # Если путь находится вне каталога python_labs, выбрасываем ошибку
            raise ValueError(
                f"Путь {path_obj} должен находиться внутри каталога {python_labs_root}"
            ) from exc

    # Нормализуем входной путь (преобразуем в относительный от python_labs_root)
    input_path = normalize_path(args.input)
    # Нормализуем выходной путь (преобразуем в относительный от python_labs_root)
    output_path = normalize_path(args.output)

    # Собираем полный абсолютный путь к выходному файлу
    output_full = python_labs_root / output_relative
    # Создаём все необходимые директории для выходного файла, если их нет
    output_full.parent.mkdir(parents=True, exist_ok=True)

    if args.command == "json2csv":
        json_to_csv(str(input_relative), str(output_relative))
    elif args.command == "csv2json":
        csv_to_json(str(input_relative), str(output_relative))
    elif args.command == "csv2xlsx":
        csv_xlsx(str(input_relative), str(output_relative))


if __name__ == "__main__":
    main()
# python src/lab06/cli_convert.py json2csv -h
# python src/lab06/cli_convert.py csv2json -h
# python src/lab06/cli_convert.py csv2xlsx -h


# python src/lab06/cli_convert.py json2csv --input src\lab06\data\people.json --output src\lab06\data\people.csv
# python src/lab06/cli_convert.py csv2json --input src\lab06\data\people.csv --output src\lab06\data\people.json
