# person = [
#     ['Nguyễn Văn A',21,'Hà Nội'],
#     ['Nguyễn Văn B',22,'Hồ Chí Minh'],
#     ['Nguyễn Văn C',23,'Đà nẵng'],
# ]

# print(person[2][1])

# dic = {1:'abc'}

# person = {'name':'Nguyễn Văn a','age':21}
# person['address']

dic = {'mouse':'chuột','keyboard':'bàn phím','computer':'máy tính'}

while True:
    text = input('Mời bạn nhập từ cần tra: ')

    if text in dic:
        print(dic[text])

    else:
        print('Từ này không có trong từ điển')