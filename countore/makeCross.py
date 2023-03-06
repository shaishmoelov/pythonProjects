import cv2
import numpy as np

# Create a blank image with a white background
image = np.ones((1013, 1040, 3), dtype=np.uint8)
image[:] = (0, 0, 0)

height = 1013
width = 1040
i=0
j=0
# Draw the lines of the cross
for i in range(height):
    for j in range(width):

        cv2.line(image, (50, 100), (150, 100), (255, 255, 255), 2)
        cv2.line(image, (100, 50), (100, 150), (255, 255, 255), 2)

        cv2.line(image, (350, 100), (450, 100), (255, 255, 255), 2)
        cv2.line(image, (400, 50), (400, 150), (255, 255, 255), 2)


# Display the image
cv2.imwrite('out1.jpg', image)