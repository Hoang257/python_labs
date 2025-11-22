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
# python src/lab06/cli_convert.py json2csv -h
# python src/lab06/cli_convert.py csv2json -h
# python src/lab06/cli_convert.py csv2xlsx -h

# python src/lab06/cli_convert.py json2csv --input src\lab06\data\people.json --output src\lab06\data\people.csv
# python src/lab06/cli_convert.py csv2json --input src\lab06\data\people.csv --output src\lab06\data\people.json
# python src/lab06/cli_convert.py csv2xlsx --input src\lab06\data\people.csv --output src\lab06\data\people.xls