from itertools import permutations


def find_combinations(word, word_list):
    # Находим все возможные комбинации двух слов из списка
    combinations = permutations(word_list, 2)
    # Фильтруем комбинации, которые начинаются с введенного слова
    valid_combinations = [
        "".join(comb) for comb in combinations if "".join(comb).startswith(word)
    ]
    return valid_combinations


def main():
    # Чтение слов из файла
    with open("tmp/words.txt", "r", encoding="utf-8") as file:
        word_list = [line.strip() for line in file]

    # Ввод слова пользователем
    user_word = input("Введите слово: ")

    # Поиск и вывод комбинаций
    combinations = find_combinations(user_word, word_list)
    for comb in combinations:
        print(comb)


if __name__ == "__main__":
    main()
