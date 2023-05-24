import numpy as np
import matplotlib.pyplot as plt

# Image properties
width = 1024
height = 768
bit_depth = 10

# Create two random images
image1 = np.random.randint(0, 2**bit_depth, size=(height, width), dtype=np.uint16)
image2 = np.random.randint(0, 2**bit_depth, size=(height, width), dtype=np.uint16)

# Add Gaussian noise to the images
mean = 0
stddev = 10

noise1 = np.random.normal(mean, stddev, size=(height, width)).astype(np.uint16)
noise2 = np.random.normal(mean, stddev, size=(height, width)).astype(np.uint16)

image1_with_noise = np.clip(image1 + noise1, 0, 2**bit_depth-1)
image2_with_noise = np.clip(image2 + noise2, 0, 2**bit_depth-1)

# Create a new image as the sum of the two images with noise
sum_of_images_with_noise = np.clip(image1_with_noise + image2_with_noise, 0, 2**bit_depth-1)

# Save images to binary files
file1 = "image1.bin"
file2 = "image2.bin"
file_sum_of_images_with_noise = "sum_of_images_with_noise.bin"

with open(file1, 'wb') as f1:
    f1.write(image1_with_noise.tobytes())

with open(file2, 'wb') as f2:
    f2.write(image2_with_noise.tobytes())

with open(file_sum_of_images_with_noise, 'wb') as f_sum:
    f_sum.write(sum_of_images_with_noise.tobytes())

# Display the images with noise
plt.subplot(2, 2, 1)
plt.imshow(image1, cmap='gray', vmin=0, vmax=2**bit_depth-1)
plt.title('Image 1 (Original)')

plt.subplot(2, 2, 2)
plt.imshow(image1_with_noise, cmap='gray', vmin=0, vmax=2**bit_depth-1)
plt.title('Image 1 with Noise')

plt.subplot(2, 2, 3)
plt.imshow(image2, cmap='gray', vmin=0, vmax=2**bit_depth-1)
plt.title('Image 2 (Original)')

plt.subplot(2, 2, 4)
plt.imshow(image2_with_noise, cmap='gray', vmin=0, vmax=2**bit_depth-1)
plt.title('Image 2 with Noise')

plt.tight_layout()
plt.show()
