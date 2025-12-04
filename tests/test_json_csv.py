import pytest
import sys, os
import csv
import json
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.lib.csv_json import csv_to_json
from src.lib.json_csv import json_to_csv


def test_json_to_csv_base(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_json_to_csv_file_not_found():  # когда нет файла
    with pytest.raises(FileNotFoundError, match="JSON file не найден"):
        json_to_csv("not_ex_file.json", "output.csv")


def test_json_to_csv_file_is_empty(tmp_path):  # когда файл пустой
    src = tmp_path / "empty_file.json"
    dst = tmp_path / "output.csv"

    src.write_text("")
    with pytest.raises(ValueError, match="JSON файл пустой"):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_not_a_dict(tmp_path):  # когда не все элементы словари
    src = tmp_path / "invalid.json"
    dst = tmp_path / "output.csv"

    data = "не список словарей"
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    with pytest.raises(ValueError, match="Все элементы JSON должны быть словарями"):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_special_characters(tmp_path):
    src = tmp_path / "input.json"
    dst = tmp_path / "output.csv"

    data = [
        {"name": "Хоанг", "age": "18"},
        {"name": "Hoàng", "age": "19"},
    ]

    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    assert dst.exists()

    with open(dst, "r", encoding="utf-8") as f:
        content = f.read()
    assert "Hoàng" in content
    assert "Хоанг" in content


def test_json_to_csv_none_values(tmp_path):
    src = tmp_path / "none.json"
    dst = tmp_path / "output.csv"

    data = [
        {"name": "ALice", "age": None, "city": None},
        {"name": "Bob", "age": "18", "city": None},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with open(dst, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert rows[0]["age"] == ""
    assert rows[1]["city"] == ""


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    with open(src, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerow({"name": "Alice", "age": "22"})
        writer.writerow({"name": "Bob", "age": "25"})

    csv_to_json(str(src), str(dst))
    assert dst.exists()
    with open(dst, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 2
    assert data[0]["name"] == "Alice"
    assert data[1]["name"] == "Bob"
    assert data[0]["age"] == "22"
    assert data[1]["age"] == "25"


def test_csv_to_json_file_not_found():
    with pytest.raises(FileNotFoundError, match="Файл не существует"):
        csv_to_json("not_ex_file.csv", "output.json")


def test_csv_to_json_not_right_format(tmp_path: Path):
    src = tmp_path / "file.txt"
    dst = tmp_path / "output.json"

    src.write_text("some content", encoding="utf-8")

    with pytest.raises(ValueError, match="Некоректный формат файла"):
        csv_to_json(str(src), str(dst))


def test_csv_to_json_empty_cells(tmp_path: Path):
    src = tmp_path / "empty.csv"
    dst = tmp_path / "output.json"
    with open(src, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
        writer.writeheader()
        writer.writerow({"name": "Alice", "age": "22", "city": "Moscow"})
        writer.writerow({"name": "Bob", "age": "", "city": "SPb"})
        writer.writerow({"name": "Charlie", "age": "30", "city": ""})
    csv_to_json(str(src), str(dst))

    with open(dst, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 3
    assert data[1]["age"] == ""
    assert data[2]["city"] == ""


def test_csv_to_json_different_colums(tmp_path: Path):
    src = tmp_path / "input.csv"
    dst = tmp_path / "output.json"

    with open(src, "w", encoding="utf-8", newline="") as f:
        f.write("name,age,city\n")
        f.write("Alice,22,Moscow\n")
        f.write("Bob,25,\n")  # Пустое значение для city
        f.write("Charlie,,SPb\n")  # Пустое значение для age

    csv_to_json(str(src), str(dst))

    with open(dst, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 3
    assert data[1]["city"] == ""  # Проверяем что значение пустое
    assert data[2]["age"] == ""  # Проверяем что age пустое
