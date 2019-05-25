import requests
import bs4

# Lấy html từ trang s-cafe
data = requests.get(
    'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn')
html = data.content.decode()


# Tạo đối tượng soup để xử lý dữ liệu dạng html
soup = bs4.BeautifulSoup(html, "html.parser")

# Lấy source html
with open('hose.html','wt',encoding='utf-8') as f:
    f.write(data.content.decode())

# Liệt kê các data trong table
table = soup.find("table",id = "tableContent")
list_information = table.find_all("td",{"class":"b_r_c"})
print(list_information)

# # Tạo list để chứa các data
# list_result = []

# for v in list_information:
#     statistic = {} # Từng data là các dic
#     statistic['title'] = v.bold.text # lấy tiêu đề từng thông tin data
#     print(statistic)


