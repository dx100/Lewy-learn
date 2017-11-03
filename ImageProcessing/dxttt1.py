# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from scipy import misc
import matplotlib.pyplot as plt
#%matplotlib inline

f = misc.face(gray=True)
#misc.imsave('face.png', f) # uses the Image module (PIL)



plt.imshow(f)
plt.show()

import numpy as np

face = misc.face(gray=True)
face[0, 40]

# Slicing
#face[10:13, 20:23]



#face[100:120] = 255

lx, ly = face.shape
X, Y = np.ogrid[0:lx, 0:ly]
mask = (X - lx / 2) ** 2 + (Y - ly / 2) ** 2 > lx * ly / 4
# Masks
face[mask] = 0
# Fancy indexing
#face[range(400), range(400)] = 255

plt.imshow(face,cmap=plt.cm.gray)
   

# Remove axes and ticks
plt.axis('off')
plt.contour(f, [190, 200]) 


# Geometrical transformations
import numpy as np
from scipy import ndimage

face = misc.face(gray=True)
lx, ly = face.shape
# Cropping
crop_face = face[lx // 4: - lx // 4, ly // 4: - ly // 4]
# up <-> down flip
flip_ud_face = np.flipud(face)
# rotation
rotate_face = ndimage.rotate(face, 45)
rotate_face_noreshape = ndimage.rotate(face, 45, reshape=False)

plt.figure(1)
plt.subplot(141)
plt.imshow(face, cmap=plt.cm.gray)
plt.axis('off')

plt.subplot(142)
plt.imshow(flip_ud_face, cmap=plt.cm.gray)
plt.axis('off')

plt.subplot(143)
plt.imshow(rotate_face, cmap=plt.cm.gray)
plt.axis('off')

plt.subplot(144)
plt.imshow(rotate_face_noreshape, cmap=plt.cm.gray)
plt.axis('off')

plt.show()

# image filter
from scipy import misc
face = misc.face(gray=True)
blurred_face = ndimage.gaussian_filter(face, sigma=3)
very_blurred = ndimage.gaussian_filter(face, sigma=5)

plt.figure(2)
plt.subplot(141)
plt.imshow(face, cmap=plt.cm.gray)
plt.axis('off')

plt.subplot(142)
plt.imshow(blurred_face, cmap=plt.cm.gray)
plt.axis('off')

plt.subplot(143)
plt.imshow(very_blurred, cmap=plt.cm.gray)
plt.axis('off')

plt.show()

# Display a number of images
def dxDisplay(nrows, ncols, imgs):
    """Display list of images in a grid fashion
    nrows: number of rows.
    ncols: number of columns.
    imgs:  list of images to be displayed."""
    
    ttt = str(10 * nrows + ncols)
    for i in range(nrows) :
        for j in range(ncols) :
            plt.subplot(ttt+str(j))
            plt.imshow(imgs[(i-1)*ncols + j], cmap=plt.cm.gray)
            plt.axis('off')
            
    plt.show()
    
# Denoising
from scipy import misc

f = misc.face(gray=True)
f = f[230:290, 220:320]
noisy = f + 0.4 * f.std() * np.random.random(f.shape)

