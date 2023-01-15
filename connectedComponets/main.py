import cv2
import numpy as np

# Load the image and convert it to grayscale
image = cv2.imread("out1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

cv2.imshow('binary', binary)
# Detect the connected components in the binary image
_, labels, stats, centroids = cv2.connectedComponentsWithStats(binary)

# Select the component that represents the cross
for label in np.unique(labels):
    # Skip the background component
    if label == 0:
        continue

    # Extract the component from the image
    component = np.uint8(labels == label)

    # # Check if the component has four vertices
    # if np.sum(component[:, :-1] != component[:, 1:]) != 4:
    #     continue

    # Calculate the moments of the component
    M = cv2.moments(component)

    # Calculate the center of the component
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    # Draw the center of the component on the image
    cv2.circle(image, (cX, cY), 5, (255, 0, 0), -1)
    cv2.putText(image, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Show the image
cv2.imshow("Image", image)
cv2.waitKey()
cv2.destroyAllWindows()