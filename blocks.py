import cv2
import numpy as np
from PIL import Image
from PIL import ImageChops
from PIL import ImageOps
import image_slicer


#im = cv2.imread("frame0.jpg").astype(np.int8)
im = Image.open("frame1.jpg")
dims=im.size
oldx=dims[0]
oldy=dims[1]
oldsize=(oldx,oldy)
print oldsize
newx=oldx
newy=oldy

color = [0, 0, 0]
top, bottom, left, right = [0]*4

if oldx % 16 != 0:
    newx = oldx + (oldx%16)


if oldy % 16 != 0:
    newy = oldy + (oldy%16)



newsize=(newx,newy)
print newsize
newim = Image.new("RGB", newsize)
newim.paste(im, (((newsize[0]-oldsize[0])/2),(newsize[1]-oldsize[1])/2))
newim.show()
newim.save("expandFrame1.jpg")

image_slicer.slice('expandFrame0.jpg', 256)
