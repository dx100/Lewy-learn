#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 17:12:53 2018

@author: dx100
"""

import cv2
import numpy as np

# initialize the list of class labels MobileNet SSD was trained to
# detect, then generate a set of bounding box colors for each class
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt.txt', 
                               "MobileNetSSD_deploy.caffemodel")

# load the input image and construct an input blob for the image
# by resizing to a fixed 300x300 pixels and then normalizing it
# (note: normalization is done via the authors of the MobileNet SSD
# implementation)

cam = cv2.VideoCapture(0)


ret,image = cam.read()
cv2.namedWindow("test")

img_counter = 0
ret = False

# 1st read from the webcam, just to get the (h, w) values
while not ret :
    ret, frame = cam.read()
    
(h, w) = image.shape[:2]
cv2.imshow("test",image)

# now, in the webcam loop
running = True
while running:
    
    # Get a image from WebCam
    ret = False
    while ret ==  False:
        ret, image = cam.read()
        
    
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)


    # pass the blob through the network and obtain the detections and
    # predictions
    net.setInput(blob)
    detections = net.forward()
    
    # loop over the detections
    for i in np.arange(0, detections.shape[2]):
    	# extract the confidence (i.e., probability) associated with the
    	# prediction
    	confidence = detections[0, 0, i, 2]
    
    	# filter out weak detections by ensuring the `confidence` is
    	# greater than the minimum confidence
    	if confidence > 0.2:
    		# extract the index of the class label from the `detections`,
    		# then compute the (x, y)-coordinates of the bounding box for
    		# the object
    		idx = int(detections[0, 0, i, 1])
    		box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
    		(startX, startY, endX, endY) = box.astype("int")
    
    		# display the prediction
    		label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
    		print("[INFO] {}".format(label))
    		cv2.rectangle(image, (startX, startY), (endX, endY),
    			COLORS[idx], 2)
    		y = startY - 15 if startY - 15 > 15 else startY + 15
    		cv2.putText(image, label, (startX, y),
    			cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
            
    cv2.imshow("Output", image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        running = False
# show the output image

cam.release()
cv2.destroyAllWindows()

