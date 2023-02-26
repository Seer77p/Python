def rythm_exists(text: str) -> bool:
    set_of_vowels = set('ауоиэыяюеё')
    text_strings = text.lower().split()
    count_vowels_list = [
        sum([1 for elem in string if elem in set_of_vowels]) 
        for string in text_strings
    ]
    print(count_vowels_list)
    return len(set(count_vowels_list)) == 1


def main() -> None:
    # input_string = input('Введите строку стихотворения: ')
    input_string = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
    if rythm_exists(input_string):
        print("Парам пам-пам")
    else:
        print("Пам парам")


if __name__ == '__main__':
    main()

#задача 2
def print_operation_table(operation, num_rows: int = 6, num_columns: int = 6) -> None:
    for y in range(1, num_rows+1):
        print(*([operation(x, y) for x in range(1, num_columns + 1)]), sep='\t')


def main() -> None:
    operations = [
        ('Умножение', lambda x, y: x * y),
        ('Сложение', lambda x, y: x + y),
        ('Вычитание', lambda x, y: x - y),
        ('Степень', lambda x, y: x**y)
    ]

    for operation_name, operation_function in operations:
        print(operation_name)
        print_operation_table(operation_function)
        print()


if __name__ == '__main__':
    main()


    # match case