from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image
import cv2

file_name = "D:/number/ver_code/test.png"

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


length_b = [0,17,51,68]
length_e = [17,34,66,82]
num = []
ver_num = []
img = cv2.imread("D:/number/ver_code/test.png",0)
methods = [cv2.TM_SQDIFF_NORMED,cv2.TM_CCORR_NORMED,cv2.TM_CCOEFF_NORMED,cv2.TM_CCOEFF_NORMED]

address = 'D:/number/{h}.jpg'
height = len(img)
width = len(img[0])
#print('图片大小%d, %d'%(width, height))
n=0

while n<=3: 
    # 对图片进行裁剪
    img2 = img[0:35, length_b[n]:length_e[n]]
    ret,thresh1 = cv2.threshold(img2,220,255,cv2.THRESH_BINARY)
    cv2.imwrite(address.format(h=n+10) ,thresh1)
    n=n+1
cv2.waitKey(0)
n=0
tem=0
while n<=3:
  template = cv2.imread(address.format(h=n+10))  
  while tem<=8:
    img = cv2.imread(address.format(h=tem))
    res = cv2.matchTemplate(img, template, methods[3])
    min_val,max_val,min_loc, max_loc = cv2.minMaxLoc(res)
    num.append(max_val)
    tem=tem+1
  ver_num.append(num.index(max(num)))
  num=[]
  n=n+1
  tem=0
  
ver_code = (ver_num[0]+ver_num[2])*10+ver_num[1]+ver_num[3]

driver.find_element_by_xpath('//*[@id="UserName"]').send_keys("112001133")
driver.find_element_by_xpath('//*[@id="passWord"]').send_keys("20021228ym")
driver.find_element_by_xpath('//*[@id="Verifycode"]').send_keys(ver_code)
time.sleep(2) 
driver.find_element_by_xpath('//*[@id="Verifycode"]').send_keys(Keys.ENTER)

time.sleep(2) 

#裁剪后直接进行二值化//*[@id="Verifycode"]
# 进行存储处理后的图片
##cv2.imwrite('D:/number/3.jpg',img2)
 
#  裁剪后的图片大小
##height=len(img2)
##width = len(img2[0])
##print('图片大小%d, %d'%(width, height))
##print('图片size',img2.size)
##print('图片dtype',img2.dtype)
 
 
##cv2.imshow("green.png",img)
##cv2.imshow("green.jpg",img2)
 

