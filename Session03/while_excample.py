# while False:
#     print('hi')

# dem = 0
# while True:
#     print('hi',dem)

#     dem += 1
#     if dem >= 10:
#         break
# print('end')

p = input("Input your password: ")
while len(p) < 8:
    p = input("Not a valid password, re-enter new password: ")
print('Your password is:',p)

# per = 0.65
# bud = 21000000
# total = bud + bud*per
# for  i in range (9):
#     print (total)