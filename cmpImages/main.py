import numpy as np
import cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
original = cv.imread("img1.jpg")
duplicate = cv.imread("img1.jpg")

if original.shape == duplicate.shape:
    print("same size and channels number")
    diff = cv.subtract(original, duplicate)
    b, g, r = cv.split(diff)

    if cv.countNonZero(b) == 0 and cv.countNonZero(g) == 0 and cv.countNonZero(r) == 0:
        print("Exactly the same")
    else:
        print("Not the same")
else:
    print("Not same size or channels number")

