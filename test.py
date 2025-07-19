from selenium import webdriver

# Mở trình duyệt Chrome
driver = webdriver.Chrome()

# Điều hướng đến Google
driver.get("https://www.google.com")

# In tiêu đề trang để kiểm tra
print("Opened page title:", driver.title)

# Đóng trình duyệt
driver.quit()
