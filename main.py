import cv2
import numpy as np
from PIL import Image
from PIL import ImageChops
from PIL import ImageOps
import image_slicer


vidcap = cv2.VideoCapture('airplane.MOV')
success,image = vidcap.read()
count = 0
success = True
while success:
    cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    #print('Read a new frame: ', success)

    im = Image.open("frame%d.jpg" % count)
    dims=im.size
    oldx=dims[0]
    oldy=dims[1]
    oldsize=(oldx,oldy)
    #print oldsize
    newx=oldx
    newy=oldy

    color = [0, 0, 0]
    top, bottom, left, right = [0]*4

    if oldx % 16 != 0:
        newx = oldx + (oldx%16)


    if oldy % 16 != 0:
        newy = oldy + (oldy%16)



    newsize=(newx,newy)
    #print newsize
    newim = Image.new("RGB", newsize)
    newim.paste(im, (((newsize[0]-oldsize[0])/2),(newsize[1]-oldsize[1])/2))
    #newim.show()
    newim.save("frame%d.jpg" % count)
    
    #image_slicer.slice("frame%d.jpg" % count, 256)

  
    count += 1

image_slicer.slice("frame0.jpg", 256)

count1=0
count2=0
#for i in range(0,count):
count3=1
img = cv2.imread("frame%d.jpg" % count3, 0)
im = Image.open("frame%d.jpg" % count3)
dims=im.size
x=dims[0]
y=dims[1]
if count1 <10 and count2 <10:       
    block = cv2.imread("frame%d_0%d_0%d.png" % count % count1 % count2,0)
elif count1 <10 and count2 >=10:
    block = cv2.imread("frame%d_0%d_%d.png" % count % count1 % count2,0)
elif count1 >=10 and count2 <10:
    block = cv2.imread("frame%d_%d_0%d.png" % count % count1 % count2,0)
elif count1 >=10 and count2 >=10:
    block = cv2.imread("frame%d_%d_%d.png" % count % count1 % count2,0)


w, h = block.shape[::-1]

method = eval("cv2.TM_CCOEFF")

res = cv2.matchTemplate(block, img, method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img,top_left, bottom_right, 255, 2)
img.paste(block, (0,0,block.width,block.height))

img.show()

'''plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle(method)

plt.show()'''    
    
    
