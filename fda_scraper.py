import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL trang web chứa danh sách thực phẩm bị thu hồi
url = "https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts"

# Gửi request đến trang FDA
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Tìm các mục thu hồi trong trang
recalls = soup.find_all('div', class_='views-row')

# Tạo danh sách để lưu dữ liệu
data = []

# Duyệt qua từng mục thu hồi và trích xuất thông tin
for recall in recalls:
    title = recall.find('h3').text.strip() if recall.find('h3') else "No Title"
    date = recall.find('div', class_='views-field-field-publication-date').text.strip() if recall.find('div', class_='views-field-field-publication-date') else "No Date"
    summary = recall.find('div', class_='views-field-field-summary').text.strip() if recall.find('div', class_='views-field-field-summary') else "No Summary"
    link = 'https://www.fda.gov' + recall.find('a')['href'] if recall.find('a') else "No Link"
    
    data.append([date, title, summary, link])

# Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(data, columns=['Date', 'Product Name', 'Summary', 'Link'])

# Lưu vào file Excel
df.to_excel("FDA_Recalls.xlsx", index=False, engine='openpyxl')

print("✅ Dữ liệu đã được lưu vào file FDA_Recalls.xlsx")
