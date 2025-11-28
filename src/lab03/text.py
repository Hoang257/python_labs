import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text:
        return []
    if casefold == True:
        text = text.casefold()
    if yo2e == True:
        text = text.replace("ё", "е").replace("Ё", "Е")
    text = re.sub(
        "[^a-zа-яё0-9\s]", "", text
    )  # Удаление всех символов, кроме букв, цифр и пробелов
    text = re.sub(r"\s+", " ", text).strip()
    return text


if __name__ == "__main__":
    test_cases = [
        "ПрИвЕт\nМИр\t",
        "ёжик, Ёлка",
        "Hello\r\nWorld",
        "  двойные   пробелы  ",
    ]
    print("\nТест normalize:")
    for test in test_cases:
        print(f"{normalize(test, casefold= True, yo2e = True)}")


def tokenize(text: str) -> list[str]:
    if not text:
        return []
    word = r"\b\w+(?:-\w+)*\b"  # через регулярку задаем каким должен быть слово
    tokens = re.findall(word, text)
    return tokens


if __name__ == "__main__":
    test_cases = [
        "привет мир",
        "hello,world!!!",
        "по-настоящему круто",
        "2025 год",
        "emoji 😀 не слово",
    ]
    print("\nТест на tokenize")
    for test in test_cases:
        print(f"{tokenize(test)}")


def count_freq(tokens: list[str]) -> dict[str, int]:
    dictionary = {}
    for token in tokens:
        dictionary[token] = dictionary.get(token, 0) + 1
    return dictionary


if __name__ == "__main__":
    test_cases = ["a", "b", "a", "c", "b", "a"]
    print("\nТест на count_freq")
    print(count_freq(test_cases))


def top_n(freq: dict[str, int], n: int = None) -> list[str, int]:
    items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return items[:n]


if __name__ == "__main__":
    test_cases = ["aa bb b b d b b d a a"]
    print("\nТест на top_words:")
    for test in test_cases:
        normalized = normalize(test)
        tokens = tokenize(normalized)
        freq = count_freq(tokens)
        top_words = top_n(freq, 3)
    print(top_words)
