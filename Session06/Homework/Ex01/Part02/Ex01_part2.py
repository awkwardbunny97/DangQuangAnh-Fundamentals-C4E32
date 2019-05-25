import requests
import bs4
import pyexcel
from youtube_dl import YoutubeDL

# Lấy html từ trang itunes
data = requests.get('https://www.apple.com/itunes/charts/songs/') 
html = data.content.decode()


options = {'default_search': 'ytsearch','max_downloads': 100}
dl = YoutubeDL(options)

# Tạo đối tượng soup để xử lý dữ liệu dạng html
soup = bs4.BeautifulSoup(html, "html.parser")

# Liệt kê các danh sách bài hát là các thẻ có thuộc tính class = 'li'
ds_cac_bai_nhac = soup.find("section",{"class":"section chart-grid"}).find_all("li")

# Tạo list để chứa các bài viết
ket_qua = []

for v in ds_cac_bai_nhac:
    ds_nhac = {}  # Từng bài hát là các dic
    ds_nhac['Rank'] = v.strong.text # Lấy thứ hạng bài hát
    ds_nhac['Name'] = v.h3.text # lấy tên bài hát
    ds_nhac['Artist'] = v.h4.text # lấy tên ca sỹ
    ket_qua.append(ds_nhac) # Thêm vào list
    dl.download([v.h3.string+""+v.h4.string]) #Đownload video

# ## In ra màn hình kết quả:
# for i in ket_qua:
#     print(i['Rank'],":",i['Name'],"-",i['Artist'])
 
# # Lưu list ket_qua ra file theo định dạng xlss
# pyexcel.save_as(records=ket_qua, dest_file_name="Itunes_top_songs.xlsx")