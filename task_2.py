def main():
    list_ = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

    print("Общее количество чисел (я делал не уникальные числа)")
    print(sum(map(len, list_)))

    print("Общая сумма чисел")
    print(sum(map(sum, list_)))

    print("посчитать среднее значение")
    print(sum(map(sum, list_)) / sum(map(len, list_)))

    print("Все числа из множеств в один кортеж:")
    print(tuple(sum(map(tuple, list_), ())))


if __name__ == "__main__":
    main()
