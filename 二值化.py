import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('D:/number/10.png',0)
ret,thresh1 = cv2.threshold(img,220,255,cv2.THRESH_BINARY)

plt.imshow(thresh1,'gray')
plt.show()
cv2.imwrite("D:/number/123.jpg" ,thresh1)


#最好在jupyter 里面运行，这里不能很好的显示图片
