import cv2
import imutils
import pytesseract
from PIL import Image, ImageFilter

image = cv2.imread('imagens/OIP.jpeg')
cv2.imshow('original image', image)
cv2.waitKey(0)

resized_image = imutils.resize(image, width=500)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scale Image", gray_img)
cv2.waitKey(0)

smoother_img = cv2.bilateralFilter(gray_img, 11, 17, 17)
cv2.imshow("Smoother Image", smoother_img)
cv2.waitKey(0)

edged = cv2.Canny(gray_img, 180, 200)
cv2.imshow("Canny image", edged)
cv2.waitKey(0)

contour, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

image1 = image.copy()
cv2.drawContours(image1, contour, -1, (0,255,0), 3)
cv2.imshow("Canny after contouring", image1)
cv2.waitKey(0)

cnts = sorted(contour, key=cv2.contourArea, reverse=True)[:50]
numberPlateCont = None

count = 0
name = 1  # Initialize the 'name' variable

for i in cnts:
    perimeter = cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, 0.02 * perimeter, True)
    # Recorta a região da placa de carro
    if len(approx) == 4:
        numberPlateCont = approx
        x, y, w, h = cv2.boundingRect(i)
        crp_img = image[y:y+h, x:x+w]
        cv2.imwrite(str(name) + '.png', crp_img)
        name += 1

        # Show the cropped region
        cv2.imshow("Cropped Region", crp_img)
        cv2.waitKey(0)  # Wait for a key press to proceed to the next contour

        break
    
image_proc = cv2.cvtColor(crp_img, cv2.COLOR_BGR2GRAY)
cv2.imshow("pre-proc", image_proc)
cv2.waitKey(0)

_,bin = cv2.threshold(image_proc, 165, 255, cv2.THRESH_BINARY)
cv2.imshow("binario", bin)
cv2.waitKey(0)

config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 6'
text = pytesseract.image_to_string(bin, lang="eng", config= config)
print("Placa:", text)
cv2.waitKey(0)
cv2.destroyAllWindows()


