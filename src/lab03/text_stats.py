import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from text import normalize, tokenize, count_freq, top_n

TABLE_MODE = False
def print_table(top_items):
    
    max_len_word = max(len(word) for word, _ in top_items)
    col_1 = "слово"
    col_2 = "частота"
    width = max(max_len_word, len(col_1))

    print('слово' + ' '* ((width+4)-len(col_1)) + "| частота" )


    print("-"*(width+4)*2)
    for word, count in top_items:

        print(f"{word}" + ' ' * ((width+4)-len(word)) + f'| {count}')

def main():
    text = sys.stdin.readline().strip()
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)

    total_words = len(tokens)
    unique_words = len(set(tokens))
    top_5 = top_n(freq,5)
    all_words = count_freq(tokens)

    if TABLE_MODE:
        print_table(top_5)
    else:
        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print("Топ-5:")
        for word, count in top_5:
            print(f"{word}:{count}")
        

if __name__ == "__main__":

    print(f"Табличный режим: {'ВКЛ' if TABLE_MODE else 'ВЫКЛ'}")
    main()