######## Nhập dãy số ########

n = int(input('Nhập số phần tử: '))
ds = []

for i in range(n):
    so = int(input('Nhập số thứ '+ str(i) + ' : '))
    ds.append(so)

print('Dãy số vừa nhập là: ')

print(ds)

######## Tổng dãy số vừa nhập ########

print(sum(ds))