from pathlib import Path
import csv 

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    """Котировку файла можно поменять, например: encoding="cp1251" """
    try:
        with open(path, 'r', encoding=encoding) as file:
            return file.read()
    except FileNotFoundError:
        print(f'Файл {path} не найден')
        raise
    except UnicodeDecodeError:
        print(f'Ошибка в кодировании файла {path}')
        raise





def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...]):
    if not rows:
        return  
    length = len(rows[0])
    for i in rows:
        if len(i) != length:
            raise ValueError
    with open(path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        if header:
            writer.writerow(header)
        writer.writerow(rows)

