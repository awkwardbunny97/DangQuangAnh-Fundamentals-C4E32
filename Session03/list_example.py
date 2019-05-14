###########In ra day so##########

n = int(input('Nhap so phan tu: '))
ds = []

for i in range(n):
    so = int(input('Nhap so thu '+ str(i) + ' : '))
    ds.append(so)

print('Day so vua nhap la: ')

print(ds)

##########Trung binh cac phan tu chan############

tong_so_chan = 0
so_phan_tu_chan = 0

for v in ds:
    if v%2 == 0:
        print(v)
        tong_so_chan = tong_so_chan + v
        so_phan_tu_chan += 1

print('Trung binh cong cac phan tu chan: ',tong_so_chan/so_phan_tu_chan)