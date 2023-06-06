import cv2
import numpy as np

def find_middle_barrel_connected(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray.tif', gray)
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imwrite('blurred.tif', blurred)
    # Perform edge detection using the Canny algorithm
    edges = cv2.Canny(blurred, 50, 150)
    cv2.imwrite('edges.tif', edges)
    # Perform connected component analysis on the edge image
    _, labels, stats, _ = cv2.connectedComponentsWithStats(edges)

    # Find the connected component with the required size
    required_size = max(image.shape[:2]) // 4
    for stat in stats[1:]:
        if stat[4] > np.pi * (required_size / 2) ** 2:
            center = (stat[0] + stat[2] // 2, stat[1] + stat[3] // 2)
            radius = max(stat[2] // 2, stat[3] // 2)
            if radius > required_size:
                cv2.rectangle(image, (stat[0], stat[1]), (stat[0] + stat[2], stat[1] + stat[3]), (0, 0, 255), 2)
                break

    return image

# Example usage for connected component-based method
image = cv2.imread('00000001.tif')
result_connected = find_middle_barrel_connected(image)

# Display the result image with connected component-based method
cv2.imshow('Result (Connected Component)', result_connected)
cv2.imwrite('out.tif', result_connected)
cv2.waitKey(0)
cv2.destroyAllWindows()
