import cv2
import numpy as np

# Create an image with a white background
image = 255 * np.ones((256, 256, 3), dtype=np.uint8)

# Define the starting and ending coordinates of the line
start = (804, 20)
end = (804, 2000)

# Define the color and thickness of the line
color = (0, 0, 0) # black
thickness = 1

# Use cv2.line() to draw the line
cv2.line(image, start, end, color, thickness, shift=3)

# color = (0, 255, 0) # green
# cv2.line(image, start, end, color, thickness, shift=0)




# Show the image
cv2.imshow("Line", image)
cv2.waitKey(0)
cv2.destroyAllWindows()