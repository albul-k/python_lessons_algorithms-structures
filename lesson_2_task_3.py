'''
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
Например, если введено число 3486, надо вывести 6843.
'''

num_inp = input('Введите число: ')
num_rev = ''
for i in num_inp[::-1]:
    num_rev += i
print(num_rev)
