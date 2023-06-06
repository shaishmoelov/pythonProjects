import cv2
import numpy as np
import pytesseract

def extract_text_from_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply image preprocessing for better text extraction
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Perform text extraction using Tesseract OCR
    text = pytesseract.image_to_string(thresh)

    # Print the extracted text
    print("Extracted Text:")
    print(text)

    # Show the original image
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Provide the path to the image containing the text
image_path = "D:\\beamlightimages\out\source.tif"
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
# Call the function to extract text from the image
extract_text_from_image(image_path)
