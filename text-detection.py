import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread("image.jpg")
img = cv2.resize(img, None, fx=0.25, fy=0.25)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(img)
print(text)

cv2.imshow("Img", img)
cv2.waitKey(0)