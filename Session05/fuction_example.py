# def say_hi():
#     print('hi')

# say_hi()

# def add_two_number(a,b):
#     if a > 0:
#         return a + b   
#     if a < 0:
#         return a - b
#     # print(a,b)
#     # print(x,y)
#     # # a = int(input('Nhập số thứ nhất: '))
#     # # b = int(input('Nhập số thứ hai: '))
#     return a + b

# print(add_two_number(50, 8))

# def abs_of_number(a):
#     if a > 0:
#         return a
#         print('Trị tuyệt đối là: ', a)
#     else:
#         return -a
#         print('Trị tuyệt đối là: ', -a)
#     print('Trị tuyệt đối là: ', a)

# x = abs_of_number(-12)
# tong = 12 + abs_of_number(-12)

# print(x)
# print(tong)

# def evaluate_of_number(a,b,c):
#     if c == '+':
#         return(a + b)
#     elif c == '-':
#         return(a-b)
#     elif c == '*':
#         return(a*b)
#     elif c == '/':
#         return(a/b)

# def eval_expression(s):
#     a = int(s[0])
#     b = int(s[2])
#     c = s[1]
#     return evaluate_of_number(a,b,c)

# while True:
#     s = input('Nhập biểu thức:')
#     print(eval_expression(s))

# # x = evaluate_of_number(1,3,'-')
# # print(x)

# n = 9
# la_so_nguyen_to = True
# for v in range(2,n):
#     if n % v == 0:
#         la_so_nguyen_to = False
# if la_so_nguyen_to:
#     print(n, 'là số nguyên tố')
# else:
#     print('')

def la_so_nguyen_to(n):
    for v in range(2,n):
        if n % v == 0:
            return False
    return True

for k in range(2,10000):
    if la_so_nguyen_to(k):
        print(k)
        
# if la_so_nguyen_to(113):
#     print('Là số nguyên tố')
# else:
#     print('Không là số nguyên tố')
# print(la_so_nguyen_to(113))