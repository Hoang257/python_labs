import argparse
import sys, os
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lab03.text import tokenize, count_freq, top_n


def num_str(input_path, number_lines=False):
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            line_num = 1
            for line in f:
                if number_lines:
                    print(f"{line_num}: {line}", end="")
                    line_num += 1
                else:
                    print(line, end="")
    except FileNotFoundError:
        print("Файл не найден")
        sys.exit(1)


def stat_text(input_path: Path, top=5):
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print("Файл не найден:", input_path)
        sys.exit(1)

    tokens = tokenize(text)
    freq = count_freq(tokens)
    top_words = top_n(freq, top)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(set(tokens))}")
    print("Топ слов:")

    for word, count in top_words:
        print(f"{word}: {count}")


def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Выводит содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к текущему файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумерует строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к текущему файлу")
    stats_parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="сколько в топе должно быть слов, по умолчанию 5",
    )

    args = parser.parse_args()

    if args.command == "cat":
        input_path = Path(args.input)
        num_str(input_path, number_lines=args.n)
    elif args.command == "stats":
        input_path = Path(args.input, top=args.top)
        stat_text(input_path)


if __name__ == "__main__":
    main()

# python src/lab06/cli_text.py stats --input src\lab06\data\test.txt
# python src/lab06/cli_text.py cat --input src\lab06\data\test.txt -n
# python src/lab06/cli_text.py cat --input src\lab06\data\test.txt -h
# python src/lab06/cli_text.py stats --input src\lab06\data\test.txt -h
