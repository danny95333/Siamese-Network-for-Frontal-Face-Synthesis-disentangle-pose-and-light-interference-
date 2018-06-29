from PIL import Image
from pylab import *
import numpy as np

im = Image.open('200_01_01_051_10.png')
im = im.resize((96, 96), Image.BILINEAR)
# width, height = im.size
# print width,height
# 96x96
img = array(im)
imshow(img)

coordinate = ginput(300)
M = np.ones([96,96,3],int8)

for i in coordinate:
    y = int(i[0])
    x = int(i[1])
    M[x, y, 0] = 5
    M[x, y, 1] = 5
    M[x, y, 2] = 5
    # use print img[x, y, 0] & print img[1,60:90,:] to check
    # the pixel location and coordinate is inversed
    # coordinate(82,1) right top but pixel[1,82,:] means right top
np.save("mask_1", M)
print M
show()


