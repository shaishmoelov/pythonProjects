import cv2


img = cv2.imread('images/pattern.png')
img_resized = cv2.resize(img, (900,300), interpolation = cv2.INTER_AREA)

(h, w) = img_resized.shape[:2]
(cX, cY) = (w //2, h//2)

M = cv2.getRotationMatrix2D((cX, cY), 4, 1.0)
img_resized_rotate = cv2.warpAffine(img_resized, M, (w, h))
cv2.imwrite('resize_rotate2.png', img_resized_rotate)