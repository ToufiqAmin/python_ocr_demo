from PIL import Image
from pytesseract import Output
import pytesseract
import numpy as np
import cv2

# program for testing Tesseract by using a simple image
file_name = 'image_1.jpg'
image1 = np.array(Image.open(file_name))
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(image1)

# im1 = Image.open(file_name)
# im1.show()

print("Text of Image No 01: "+text)

# program for noise image
file_name2 = 'image_2.jpg'
image2 = np.array(Image.open(file_name2))

norm_img = np.zeros((image2.shape[0], image2.shape[1]))
image2 = cv2.normalize(image2, norm_img, 0, 255, cv2.NORM_MINMAX)
image2 = cv2.threshold(image2, 100, 255, cv2.THRESH_BINARY)[1]
image2 = cv2.GaussianBlur(image2, (1, 1), 0)
text2 = pytesseract.image_to_string(image2)

# im2 = Image.open(file_name2)
# im2.show()
print("Text of Image No 02: "+text2)


# text localization & detection in ocr
image = cv2.imread(file_name)
results = pytesseract.image_to_data(image, 
output_type=Output.DICT)
print("The Dictionary of Image 01 is:\n", results)


for i in range(0, len(results['text'])):
   x = results['left'][i]
   y = results['top'][i]

   w = results['width'][i]
   h = results['height'][i]

   text = results['text'][i]
   conf = int(results['conf'][i])
   
   if conf > 70:
    text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, text, (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)

cv2.imshow("Show",image)
cv2.waitKey(0)