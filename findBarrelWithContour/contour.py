import cv2
import numpy as np

def find_middle_barrel_contour(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray.tif', gray)
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imwrite('blurred.tif', blurred)
    # Perform edge detection using the Canny algorithm
    edges = cv2.Canny(blurred, 50, 150)
    cv2.imwrite('edges.tif', edges)
    # Find contours in the edge image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the circle with the required size
    required_size = max(image.shape[:2]) // 4
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > np.pi * (required_size / 2) ** 2:
            ((x, y), radius) = cv2.minEnclosingCircle(contour)
            if radius > required_size:
                cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 0), 2)
                break

    return image

# Example usage for contour-based method
image = cv2.imread('00000001.tif')
result_contour = find_middle_barrel_contour(image)

# Display the result image with contour-based method
cv2.imshow('Result (Contour)', result_contour)
cv2.imwrite('out.tif', result_contour)
cv2.waitKey(0)
cv2.destroyAllWindows()
