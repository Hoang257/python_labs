from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Открыть файл на чтение в указанной кодировке и вернуть содержимое как одну строку.
    Обрабатывать ошибки: если файл не найден — поднимать FileNotFoundError (пусть падает), если кодировка не подходит — поднимать UnicodeDecodeError (пусть падает).
    НО: в докстринге опишите, как пользователь может выбрать другую кодировку (пример: encoding="cp1251").
    """
    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    try:
        return p.read_text(encoding=encoding)  # Считываем текст
    except FileNotFoundError:
        raise FileNotFoundError("Нет такого файла")
    except UnicodeDecodeError:
        raise UnicodeDecodeError("Неправильная кодировка")


# text_1 = read_text(r"C:\Users\hoang\OneDrive\Desktop\laba\python_labs\data\input.txt")
# print(text_1)


import csv
from typing import Iterable, Sequence


def write_csv(
    rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    """Создать/перезаписать CSV с разделителем ,.
    Если передан header, записать его первой строкой.
    Проверить, что каждая строка в rows имеет одинаковую длину (иначе ValueError)."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    rows = list(rows)
    if not rows:
        return

    length = len(rows[0])
    for i in rows:
        if len(i) != length:
            raise ValueError("Все строки должны быть одинаковой длины")
    with p.open(
        "w", newline="", encoding="utf-8"
    ) as f:  # коректирует перенос строк в csv
        writer = csv.writer(
            f, delimiter=",", quoting=csv.QUOTE_MINIMAL
        )  # упраление кавычками, ставит только когда надо
        if header:
            writer.writerow(header)
        writer.writerows(rows)


# text_2 = write_csv(
#     [("word", "count")],
#     r"C:\Users\hoang\OneDrive\Desktop\laba\python_labs\data_lab_04\input.txt",
# )
# print(text_2)
