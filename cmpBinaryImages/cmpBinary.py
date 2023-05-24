import numpy as np

# Image properties
width = 1024
height = 768
bit_depth = 10

# Function to load a binary image
def load_binary_image(filename):
    with open(filename, 'rb') as file:
        image = np.frombuffer(file.read(), dtype=np.uint16)
    return image

# Function to check if two images are equal per pixel
def check_image_equality(image1, image2):
    if image1.shape != image2.shape:
        return False
    return np.array_equal(image1, image2)

# Load the binary images
file1 = "sum_of_images_with_noise_from_python.bin"
file2 = "sum_of_images_from_cpp.bin"

image1 = load_binary_image(file1)
image2 = load_binary_image(file2)

# Check if the images are equal per pixel
equal_per_pixel = check_image_equality(image1, image2)

# Display the result
if equal_per_pixel:
    print("The images are equal per pixel.")
else:
    print("The images are not equal per pixel.")
