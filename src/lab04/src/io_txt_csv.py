# from pathlib import Path
# import csv
# from typing import Iterable, Sequence
# def read_text(path: str | Path, encoding: str = "utf-8") -> str:
#     path = Path(path) # переменная path всегда будет объектом Path -> мы можем вывзвать всякие методы
#     if path.suffix != 'csv' or 'txt':
#         raise ValueError('Ошибка, принимаем только формат тхт и цсв')
#     try:
#         with path.open('r', encoding=encoding) as f:
#             return f.read()
#     except FileNotFoundError:
#         raise
#     except UnicodeDecodeError:
#         raise  # пробрасываем текущую ошибку, не создаём заново
    
# import csv
# from typing import Iterable, Sequence

# def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
#     p = Path(path)
#     path = Path(path) # переменная path всегда будет объектом Path -> мы можем вывзвать всякие методы
#     if path.suffix != 'csv' or 'txt':
#         raise ValueError('Ошибка, принимаем только формат тхт и цсв')
#     rows = list(rows)
#     if rows:
#         length = len(rows[0])
#         for i in rows:
#             if len(i) != length:
#                 raise ValueError('Все строки должны быть одинаковой длины')
#     with p.open('w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         if header:
#             writer.writerow(header)
#         if rows:
#             writer.writerows(rows)


