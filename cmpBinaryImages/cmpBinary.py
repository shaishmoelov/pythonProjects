import numpy as np

# Image properties
width = 1024
height = 768
bit_depth = 10

#To do:
#read 2 images in gray scale
#add noises
#change to binary foramt
#sum up 2 images
#write binary sum image to right path for compart



# Function to load a binary image
def load_binary_image(filename):
    with open(filename, 'rb') as file:
        image = np.frombuffer(file.read(), dtype=np.uint16)
    return image

# Function to check if two images are equal per pixel
#in matrix not in vector - reshape
def check_image_equality(image1, image2):
    if image1.shape != image2.shape:
        return False
    return np.array_equal(image1, image2)

# Load the binary images
cpp_sum = r"G:\My Drive\myProject\cppProjects\cppProjects\sumOfImages\sumOfImages\sum_of_images.bin"
python_sum = r"G:\My Drive\myProject\pythonProjectss\pythonProjectss\createImages\output\sum_of_images_with_noise.bin"

cpp_sum_img = load_binary_image(cpp_sum)
python_sum_img = load_binary_image(python_sum)

# Check if the images are equal per pixel
equal_per_pixel = check_image_equality(cpp_sum_img, python_sum_img)

# Display the result
if equal_per_pixel:
    print("The images are equal per pixel.")
else:
    print("The images are not equal per pixel.")
