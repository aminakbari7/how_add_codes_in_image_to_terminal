import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
import numpy as np
im=cv2.imread('3.jpg')
scale_percent = 180 # percent of original size
width = int(im.shape[1] * scale_percent / 100)
height = int(im.shape[0] * scale_percent / 100)
dim = (width, height)
 
resized = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)
gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
enhanced_image = cv2.addWeighted(gray_image, 0.5, gray_image, 0, 30)
original_and_enhanced_image = np.hstack((gray_image, enhanced_image))
print(pytesseract.image_to_string(enhanced_image ))
cv2.imshow('result',enhanced_image)
cv2.waitKey(0)