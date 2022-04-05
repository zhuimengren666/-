from selenium import webdriver
import time
from PIL import Image

file_name = "D:/number/20.png"

driver = webdriver.Chrome()
driver.get("https://jwch.fzu.edu.cn/login.htm")
driver.maximize_window()
time.sleep(2)

# 1.登录页面截图并保存在C:/test.png
driver.save_screenshot(file_name)
# 2.获取图片验证码坐标和尺寸
code_element = driver.find_element_by_xpath('//*[@id="yzm_pic"]')
left = code_element.location['x']     
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open(file_name)
# 3.截取图片验证码
img = im.crop((left, top, right, height))
# 4.截取的验证码图片保存为新的文件
img.save(file_name)
driver.close()
