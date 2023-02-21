

def text_reading(stroka):
    with open('text.txt', 'r', encoding='utf-8') as file:
        text = str(file.readlines()[stroka])
        print('\nФраза Винни_Пуха: ', text)
        text = text.lower()
    return text

def verse_check(phrase):
    word_list = phrase.split(" ")
    vowel_list = ('а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я',)
    cout = 0
    cout_list = []
    for word in word_list:
        if cout != 0:
            cout_list.append(cout)
            cout = 0
        for vowel in word:
            if vowel in vowel_list:
                cout += 1
    summa = 0
    for i in range(len(cout_list)):
        if cout_list[i] == cout_list[i-1]:
            summa += 1
    if summa == (len(cout_list)):
        return print('C ритмом все в порядке - Парам пам-пам')
    else:
        return print('C ритмом во фразе не порядок -  Пам парам')


def main():
    verse_check(text_reading(0))
    verse_check(text_reading(1))
    verse_check(text_reading(2))
    

if __name__ == '__main__':  # усли в качестве импорта не будт запускаться
    print('Запускаю')
