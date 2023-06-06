import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

# Image properties
desire_width = 1024
desire_height = 768
bit_depth = 10
max_pix_val = 1023
val_8_bit = 255

# Read the images
img1 = cv2.imread("input/cameraman.tif", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("input/mandi.tif", cv2.IMREAD_GRAYSCALE)
# take images to 10 bit range
img1 = img1 * (max_pix_val / val_8_bit)
img2 = img2 * (max_pix_val / val_8_bit)

# print image 1
plt.subplot(3, 2, 1)
plt.imshow(img1, cmap='gray', vmin=0, vmax=2 ** bit_depth - 1)
plt.title('Image 1 (Original)')
# print image 2
plt.subplot(3, 2, 2)
plt.imshow(img2, cmap='gray', vmin=0, vmax=2 ** bit_depth - 1)
plt.title('Image 2 (Original)')

# Resize the images to the desire resolution by ROTEM - 1024*768
img1_res = cv2.resize(img1, (desire_width, desire_height), interpolation=cv2.INTER_AREA)
img2_res = cv2.resize(img2, (desire_width, desire_height), interpolation=cv2.INTER_AREA)

# # Add Gaussian noise to the images
mean = 0
stddev = 180
# Create two noise images in 8 bit rang
noise1 = np.random.normal(mean, stddev, size=(desire_height, desire_width)).astype(np.uint8)
noise2 = np.random.normal(mean, stddev, size=(desire_height, desire_width)).astype(np.uint8)

# take the noise image to [0,1023]
noise1 = noise1 * (max_pix_val / val_8_bit)
noise2 = noise2 * (max_pix_val / val_8_bit)

image1_with_noise = np.clip(img1_res + noise1, 0, 2 ** bit_depth - 1)
image2_with_noise = np.clip(img2_res + noise2, 0, 2 ** bit_depth - 1)



# save noisy images in binary file
noisy_img_1 = "image_1_with_noise.bin"
with open(noisy_img_1, 'wb') as f_sum:
    f_sum.write(image1_with_noise.tobytes())

noisy_img_2 = "image_2_with_noise.bin"
with open(noisy_img_2, 'wb') as f_sum:
    f_sum.write(image2_with_noise.tobytes())

# # Display the images with noise
plt.subplot(3, 2, 3)
plt.imshow(image1_with_noise, cmap='gray', vmin=0, vmax=2 ** bit_depth - 1)
plt.title('Image 1 with noise ')

plt.subplot(3, 2, 4)
plt.imshow(image2_with_noise, cmap='gray', vmin=0, vmax=2 ** bit_depth - 1)
plt.title('Image 2 with noise ')

#
# # Create a new image as the sum of the two images with noise
# #sum not clip
sum_of_images_with_noise = image1_with_noise + image2_with_noise
# Display sum image
plt.subplot(3, 2, 5)
plt.imshow(sum_of_images_with_noise, cmap='gray', vmin=0, vmax=2 ** (bit_depth+1) - 1)
plt.title('Sum images with noise')
plt.tight_layout()
plt.show()
cv2.imwrite(r"output\sum.tif", np.uint8(sum_of_images_with_noise))

# # Save sum image to binary files
file_sum_of_images_with_noise = "output/sum_of_images_with_noise.bin"
with open(file_sum_of_images_with_noise, 'wb') as f_sum:
    f_sum.write(sum_of_images_with_noise.tobytes())
