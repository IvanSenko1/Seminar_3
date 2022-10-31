# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def mult_two_num ():
    lst = list(map(int, input('Введите числа через запятую: ').split(',')))
    newlst = []
    for i in range((len(lst) + 1) // 2):
        newlst.append(lst[i] * lst[- 1 - i])
    print(f'Произведение пар чисел списка: {newlst}')

mult_two_num ()    