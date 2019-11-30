import cv2
import numpy as np
from PIL import Image
from PIL import ImageChops
from PIL import ImageOps
from matplotlib import pyplot as plt


img = cv2.imread("frame0.jpg", 0)
im = Image.open("frame0.jpg")
dims=im.size
x=dims[0]
y=dims[1]
c=0
a=1
b=12
block = cv2.imread("frame0_16_16.png",0)

#template = cv2.imread("frame0_15_14.png", 0)

w, h = block.shape[::-1]

method = eval("cv2.TM_CCOEFF")

res = cv2.matchTemplate(block, img, method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print res
print min_val, max_val, min_loc, max_loc

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img,top_left, bottom_right, 255, 2)

plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle(method)

plt.show()
