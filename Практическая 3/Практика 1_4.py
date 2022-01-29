# -- coding: utf-8 --
def summ():
    sum = 0
    for i in range(int(input('Введите количество чисел N '))):
        sum += int(input('Введите количество целых чисел N '))
    return sum 

print('Сумма чисел равна',summ())