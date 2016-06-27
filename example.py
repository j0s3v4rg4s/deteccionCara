import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

imagePath = sys.argv[1]
imagePath2 = sys.argv[2]

image = cv2.imread(imagePath)
image2 = cv2.imread(imagePath2)


im2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
im22 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

hist = cv2.calcHist([im2], [0, 1, 2], None, [8, 8, 8],[0, 256, 0, 256, 0, 256])
hist = cv2.normalize(hist).flatten()

hist2 = cv2.calcHist([im22], [0, 1, 2], None, [8, 8, 8],[0, 256, 0, 256, 0, 256])
hist2 = cv2.normalize(hist2).flatten()

for i in xrange(4):
    base_base = cv2.compareHist(hist,hist,i)
    base_half = cv2.compareHist(hist,hist2,i)
    print "Method: {0} -- base-base: {1} , base-half: {2}".format(i,base_base,base_half)
