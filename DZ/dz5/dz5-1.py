# dz 5.1
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def word_delete(a_list, a, b, v):
    a_list = a_list.lower()
    word = a_list.split(' ')
    print(word)
    new_word = []
    for i in range(0, len(word)):
        if a in word[i]:
            print('В слoве "', word[i], '" есть буква "a" - удаляем')
        elif b in word[i]:
            print('В слoве "', word[i], '" есть буква "б" - удаляем')
        elif v in word[i]:
            print('В слoве "', word[i], '" есть буква "в" - удаляем')
        else:
            new_word.append(word[i])
    return " ".join(new_word)

a_list = 'жлфа длрпмд юлоти.дло кавноьм ьджоборпм фаяр бриюсляыв vvv длрпбжлрпи юлоыввива жзджд'
print('Слова не содержащие букв "а", "б", "в" - ',word_delete( a_list, "а", "б","в"))


