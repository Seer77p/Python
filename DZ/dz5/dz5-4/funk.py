
def rle_stroka(stroka):
    print()
    print('Исходная строка: ',stroka, '\n')
    stroka_list = list()
    cout = 1
    for i in range(1, len(stroka)):
        if stroka[i] == stroka[i-1]:
            cout += 1
        else:
            stroka_list.append(cout)
            stroka_list.append(stroka[i-1])
            cout = 1
    stroka_list.append(str(cout))
    stroka_list.append(str(stroka[len(stroka)-1]))
    rle = str(stroka_list)
    rle = rle.replace(",", "").replace("'", "").replace(
        " ", "").replace("[", "").replace("]", "")
    return rle



def new_stroka(rle):
    stroka_new = []
    print('Сжатая строка: ', rle)
    for i in range(len(rle)):
        if rle[i].isnumeric():
            for j in range(int(rle[i])):
                stroka_new.append(rle[i+1])

    stroka_new_str="".join(stroka_new)
    print('Распакованная строка: ',stroka_new_str)


