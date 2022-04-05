import cv2
import numpy as np
from matplotlib import pyplot as plt
#%matplotlib inline
 




img = cv2.imread("D:/number/00.jpg")

cv2.rectangle(img, (5,5), (20,20), 255,5)
#imgcpy = cv2.cvtColor(imgcpy, cv2.COLOR_BGR2RGB)
plt.imshow(img, cmap = 'gray')
plt.show()
