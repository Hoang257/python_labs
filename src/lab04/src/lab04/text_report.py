import sys # модуль для работы с системными вещами
import os # модуль для перемещения по директориям
import csv # модуль для работы с CSV-файлами
import argparse # модуль для работы с данными с командной строки 
from pathlib import Path
# получаем абсолютный путь к src
project_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..', 'src'))
sys.path.append(project_src)
from lab03.text import tokenize, top_n, normalize, count_freq

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--in', 
        dest= 'input_file',
        default='data/input.txt',
        help='Путь к входному текстовому файлу'
        )
    parser.add_argument(
    '--out',
    dest='output_file', 
    default= 'data/report.csv',
    help='Путь для сохранения CSV отчета'
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="Кодировка файла (по умолчанию utf-8)"
    )
    return parser.parse_args()

def main():
    args = parse_args()  # берем аргументы из командной строки
    """Превращаем строки пути в объекты Path, чтобы было удобнее работать"""
    input_path = Path(args.input_file)
    output_path = Path(args.output_file)
    encoding = args.encoding
    if input_path.suffix not in {'.txt', '.cvs'}:
        print("Ошибка в формате файла, должен быть в формате .txt или .csv.")
        sys.exit(1)
    if not input_path.exists():
        print('Файл не найден ')
        sys.exit(1) # завершаем принудительно файл
    try:
        text = input_path.read_text(encoding="utf-8")
    except UnicodeDecodeError as e:
        print(f"Ошибка кодировки при чтении {input_path}: {e}")
        sys.exit(1)
    
    text = input_path.read_text()
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)

    total_words = len(tokens)
    unique_words = len(set(tokens))
    top_5 = top_n(freq, 5)
    
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    """Создание CVS"""
    with output_path.open('w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["word", "count"])
        writer.writerows(sorted_items)
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_5:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()