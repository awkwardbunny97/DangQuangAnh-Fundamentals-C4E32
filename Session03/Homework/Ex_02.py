############## Kiểm tra đầu vào #################
num = int(input('Nhập số cần phân tích: '))
while True:
    if num < 0:
        num = int(input('Số vừa nhập phải lớn hơn 0, vui lòng nhập lại số cần phân tích: '))
    if num > 10000000:
        num = int(input('Số vừa nhập phải nhỏ hơn 1000000, vui lòng nhập lại số cần phân tích: '))
    else:
        break
print('Số cần phân tích là: ',num)

############# Tập hợp các số nguyên tố #################
i = 2
ds = []
while i < num:
    j = 2
    while j <= i // j:
        if i % j == 0:
            break
        j = j + 1
    else:
        ds.append(i)
    i = i + 1

############# Phân tích thành tích các số nguyên tố #################

ds_2 = []
v = 0
while num != 1:
    x = ds[v]
    if num % x == 0:
        num = num / x
        ds_2.append(x)
    else:
        v += 1
print('là tích các nguyên tố sau: ', ds_2)