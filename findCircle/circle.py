import numpy as np
import cv2


# Param 1 will set the sensitivity; how strong the edges of the circles need to be. Too high and it won't detect
# anything, too low and it will find too much clutter. Param 2 will set how many edge points it needs to find to
# declare that it's found a circle. Again, too high will detect nothing, too low will declare anything to be a
# circle. The ideal value of param 2 will be related to the circumference of the circles.

def find_circles(image, center_threshold=100, dp=1, minDist=70, param1=160, param2=30, minRadius=350, maxRadius=500,
                 inner_circle_reduction=20):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # print(gray)

    # Apply a blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply the Hough Circle Transform
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist,
                               param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

    # print(circles)
    # Draw the detected circles on the original image
    final_circles = []
    mid_y, mid_x = gray.shape[0] // 2, gray.shape[1] // 2
    # best_circle = {"distance":1000}
    if circles is not None:
        circles = np.round(circles[0, :]).astype(int)
        # print(circles)
        # print("_"*10)
        for (x, y, r) in circles:
            new_dist = np.sqrt(((mid_x - x) ** 2) + ((mid_y - y) ** 2))
            # print(new_dist)
            if new_dist < center_threshold:
                final_circles.append({
                    "x": x,
                    "y": y,
                    "r": r
                })
        if len(final_circles) > 0:
            final_circles.sort(key=lambda k: np.pi * (k["r"] ** 2), reverse=True)
            final_circles[0]["r"] -= inner_circle_reduction
            # cv2.circle(image, (final_circles[0]["x"], final_circles[0]["y"]), final_circles[0]["r"], (0, 255, 0), 2)

            return final_circles[0]
        else:
            return None
    return None


def find_circle_and_apply_mask(src_image, dp=1, minDist=70, param1=160, param2=30, minRadius=350, maxRadius=500,
                               inner_circle_reduction=20):
    temp_imm = np.copy(src_image)
    # print(temp_imm)
    circle_data = find_circles(temp_imm, dp=dp, minDist=minDist, param1=param1, param2=param2, minRadius=minRadius,
                               maxRadius=maxRadius, inner_circle_reduction=inner_circle_reduction)
    if circle_data is None:
        return None, None, None
    # print(circle_data)
    mask = np.zeros(src_image.shape, dtype=np.uint8)
    cv2.circle(mask, (circle_data["x"], circle_data["y"]), circle_data["r"], (1, 1, 1), cv2.FILLED)
    temp_imm *= mask
    return temp_imm, mask * 255, circle_data


img = cv2.imread("D:\\beamlightimages\\barrel\data_22032023\canon\IMG\AAAAAB_S005_S001_T014\\00000002.tif")
ret, ret1, ret2 = find_circle_and_apply_mask(img)
cv2.imwrite("D:/beamlightimages/out.tif", ret)
