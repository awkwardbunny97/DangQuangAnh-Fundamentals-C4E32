# for i in [1 , 2 , 3]:
#     print('Hi',i)

# A = [1,2,3,4,5,6,7,8,9,10]
# for a in A:
#     if a % 2 == 1:
#         print(a)

# for k in range(10):
#     for v in range(k):
#         print(v, end=' ')
#     print()

num = int(input('nhap so: '))
total = 0
for i in range(num + 1):
    total = total + i
print('Tong day so la: ',total)
