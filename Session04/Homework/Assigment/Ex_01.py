############# Danh sách sinh viên ############
student_list = [
    {'name':'Nguyễn Văn A' , 'age':'21' , 'address':'Hà Nội' , 'math': 9 , 'physics': 8 , 'chemistry': 7 ,'phone': 12345},
    {'name':'Nguyễn Văn B' , 'age':'22' , 'address':'Hồ Chí Minhi' , 'math': 5 , 'physics': 6 , 'chemistry': 7 ,'phone': 6789},
    {'name':'Nguyễn Văn C' , 'age':'23' , 'address':'Dà Nẵng' , 'math': 1 , 'physics': 3 , 'chemistry': 5 ,'phone': 13579},
    {'name':'Nguyễn Văn D' , 'age':'24' , 'address':'Hòa Bình' , 'math': 2 , 'physics': 4 , 'chemistry': 6 ,'phone': 246810},
    {'name':'Nguyễn Văn E' , 'age':'25' , 'address':'Vinh' , 'math': 10 , 'physics': 1 , 'chemistry': 5 ,'phone': 987654321},
]

############# Điểm Trung Bình ############
for i in student_list:
    print('Điểm trung bình của',i['name'],'là',(i['math'] + i['physics'] + i['chemistry'])/3)

############# Sinh viên có điểm toán cao nhất ############
max_math_point = 0
name_list = []
for p in student_list:
    if p['math'] >= max_math_point:
        if p['math'] > max_math_point:
            name_list.clear()
        max_math_point = p['math']
        name_list.append(p['math'])
print(p['name'],'là sinh viên có điểm toán cao nhất')

############# Nhập một số điện thoại và in ra tên sinh viên ############
phone_number = input("Nhập số điện thoại cần tìm: ")
student_name = []
for v in student_list:
    if phone_number in v['phone']:
        phone_name = v["name"]
if phone_name == 0:
    print("Không ai có sđt này")
else:
    print("Số điện thoại",phone_number,"là của",phone_name)