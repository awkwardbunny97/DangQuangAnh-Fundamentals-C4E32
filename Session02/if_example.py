# age = 10
# if age < 18:
#     print('baby') 

# age = 10
# is_baby = age < 10
# print(is_baby)

# num = 101
# is_odd = num % 2 == 1
# print(is_odd)

# text = 'xin chao'
# text_is_not_empty = len(text) > 10
# print(text_is_not_empty)

# from math import *
# num = int(input('nhap so:'))
# print(abs(num))

# num = int(input('nhap so:'))
# if num > 0:
#     print('tri tuyet doi la:',num)
# else:
#     print('tri tuyet doi la:',-num)

# num = int(input('nhap so:'))
# if num > 0:
#     print('tri tuyet doi la:',num)
# elif num == 0:
#     print('la so khong')
# elif num == 1:
#     print('la so mot')    

year = int(input('nhap nam sinh: '))
age = int(2019-year)

if age > 18:
    print('Adult')
if 13 < age < 18:
    print('Teenager')
if age < 12:
    print('Baby')