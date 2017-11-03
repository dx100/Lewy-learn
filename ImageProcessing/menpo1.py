#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:46:34 2017

@author: dx100
"""

import menpo.io as mio
img = mio.import_builtin_asset.lenna_png()
img_resized = img.resize((200, 200))
# methods in Menpo return modified copies - so img is unchanged by the resize call.
print(img)
print(img_resized)
# Output:
# 512W x 512H 2D Image with 3 channels
# 200W x 200H 2D Image with 3 channels

# If you don't need the intermediate copies, just chain methods back-to-back:
greyscale_vector = img.as_greyscale().resize((200, 200)).as_vector()
print(greyscale_vector)
# Outputs:
# [ 0.63622375  0.63370722  0.61733637 ...,  0.37906707  0.39924645]

import numpy as np
import os
import menpo.io as mio

images = list(mio.import_images(str(mio.data_dir_path()) + '/*'))
print('Found {} images'.format(len(images)))

# Grab the first image
img = images[0]

img.view_landmarks();

print('Is img landmarked?')
print(' - {}'.format(img.landmarks.has_landmarks))

print('How many landmark groups does it have?')
print(' - {}'.format(img.landmarks.n_groups))
    
print('What labels do these groups have?')
for g in img.landmarks.group_labels:
    print(' - {}'.format(g))
