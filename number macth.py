import cv2
import numpy as np
from matplotlib import pyplot as plt
#%matplotlib inline
 
# 定义显示图片的函数，避免重复代码
def cv2_show(name,img):
    cv2.imshow(name, img)
cv2.waitKey()
cv2.destroyAllWindows()
methods = [cv2.TM_SQDIFF_NORMED,cv2.TM_CCORR_NORMED,cv2.TM_CCOEFF_NORMED]
template = cv2.imread("D:/number/123.jpg")
cv2.imshow("template",template)
img = cv2.imread("D:/number/00.jpg")
cv2.imshow("img",img)
h,w = template.shape[:2]
res = cv2.matchTemplate(img, template, methods[2])
min_val, max_val,min_loc, max_loc = cv2.minMaxLoc(res)
print(min_val,max_val,min_loc,max_loc)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] +h)
imgcpy = img.copy()
cv2.rectangle(imgcpy, top_left, bottom_right, 0,1)
imgcpy = cv2.cvtColor(imgcpy, cv2.COLOR_BGR2RGB)
plt.imshow(imgcpy, cmap = 'gray')
plt.show()




##--------------1--------------
##min_val 6.713293259963393e-05　　　　#标准差越小，匹配效果越好
##max_val 0.6963181495666504
##min_loc (180, 90)
##max_loc (478, 235)
##--------------1--------------
##
##--------------3--------------
##min_val 0.7413668632507324
##max_val 0.9770615100860596　　　　#相关性越接近一，匹配效果越好
##min_loc (496, 85)
##max_loc (180, 90)
##--------------3--------------
##
##--------------5--------------
##min_val -0.43208545446395874
##max_val 0.8136414289474487　　　　#相关性越接近一，匹配效果越好
##min_loc (871, 75)
##max_loc (180, 90)

##关于参数 method：
##CV_TM_SQDIFF平方差匹配法：该方法采用平方差来进行匹配；最好的匹配值为0；匹配越差，匹配值越大。
##CV_TM_CCORR相关匹配法：该方法采用乘法操作；数值越大表明匹配程度越好。
##CV_TM_CCOEFF相关系数匹配法：1表示完美的匹配；-1表示最差的匹配。
##CV_TM_SQDIFF_NORMED归一化平方差匹配法
##CV_TM_CCORR_NORMED归一化相关匹配法
##CV_TM_CCOEFF_NORMED归一化相关系数匹配法
