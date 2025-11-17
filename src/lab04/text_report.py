""" задание:
Читает один входной файл data/input.txt (путь можно захардкодить или принять параметром командной строки — опишите в README).
Нормализует текст (lib/text.py), токенизирует и считает частоты слов.
Сохраняет data/report.csv c колонками: word,count, отсортированными: count ↓, слово ↑ (при равенстве).
в консоль печатает краткое резюме:
всего слов: <N>
Уникальных слов: <K>
Топ-5: (список из top_n из ЛР3)"""

import sys, os, csv
from pathlib import Path 
import argparse
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from func_from_3lab import normalize, tokenize, count_freq, top_n

def main():
    parser = argparse.ArgumentParser(description='Word freq report')#создаём объект парсера для обработки аргументов. 
    parser.add_argument('--in', dest='input_file', default='data/input.txt')
    parser.add_argument('--out', dest='output_file', default='data/output.txt')
    parser.add_argument('--encoding', default='utf-8')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding=args.encoding) as f:
            text = f.read()
    except FileNotFoundError:
        raise FileNotFoundError('Нет такого файла')
    except UnicodeDecodeError:
        raise UnicodeDecodeError('Неправильная кодировка')
    
    normalized_text = normalize(text)
    words = tokenize(normalized_text)
    freq = count_freq(words)

    total_words = len(words)
    unique_words = len(freq)

    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    os.makedirs(os.path.dirname(args.output_file), exist_ok=True)
    with open(args.output_file, 'w', encoding='utf-8') as f:
        f.write("word,count\n")
        for word, count in sorted_words:
            f.write(f"{word},{count}\n")
    
    print(f'Всего слов: {total_words}')
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in sorted_words[:5]:
        print(f"{word}: {count}")

if __name__ == '__main__':
    main()
    