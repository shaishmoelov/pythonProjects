import numpy as np
import cv2
import glob
# import yaml
#import pathlib

#
img1 = cv2.imread('images/pattern.png')
gray_img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


img2 = cv2.imread('images/resize_rotate2.png')
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

ret1, corners1 = cv2.findChessboardCorners(img1, (9,6), None)
ret2, corners2 = cv2.findChessboardCorners(img2, (9,6), None)


H, _ = cv2.findHomography(corners1, corners2)
print(H)
img1_warp = cv2.warpPerspective(img1, H, (img2.shape[1], img2.shape[0]))

cv2.imshow('first camera',img1)
cv2.waitKey(0)

cv2.imshow('second camera',img2)
cv2.waitKey(0)

cv2.imshow('align image',img1_warp)
cv2.waitKey(0)