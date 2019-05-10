num = int(input('Enter a number: '))

for v in range(num // 2):
    print("x *",end=' ')
if num % 2 == 1:
    print('x')