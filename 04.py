#Задайте число N. Составьте список чисел Фибоначчи, N - количество чисел в списке

first = 1
sec = 1
print ('Введите количество чисел Фибоначчи: ')
n = int(input())
if (n == 1):
    print(1)
elif (n == 2):
    print(1, 1)
else:
    print(first, sec, end='')
    for i in range(2, n):
        first, sec = sec, first + sec
        print(sec, end=' ')     