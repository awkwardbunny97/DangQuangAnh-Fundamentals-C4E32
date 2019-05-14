######## Tiền tiết kiệm sau 9 năm #########
per = 0.065
bud = 21000000
total_per_year = bud * per
total = (bud + total_per_year) * 9
print ('Sau 9 năm anh có',total,'triệu trong tài khoản')

######## Sau bao lâu thì mua được nhà #########
bud = 21000000
per = 0.065
year = 0
while bud < 1200000000:
    bud = bud + bud * per
    year += 1
print('Sau',year,'năm thì anh mua được nhà')