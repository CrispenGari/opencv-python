
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Read The image
image = cv2.imread('../images/8.jpg')
cv2.resize(image, (int(image.shape[1]* 0.1), int(image.shape[0]*.01)))
# Convert the image to GrayScale
gray_image = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)

# Apply Canny Edge to the gray image
image_canny = cv2.Canny(gray_image,170, 200)

# Find Contors on the canny Image
contours, new = cv2.findContours(image_canny.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# print(contours)

# Sort the contours in desc
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]

# Vars
licence_plate = None
x,y,w,h = None, None, None, None

for contour in contours:
    perimeter = cv2.arcLength(contour, closed=True)
    approx = cv2.approxPolyDP(contour, 0.01 * perimeter, closed=True)
    if len(approx) == 4:
        # A plate
        x, y, w, h = cv2.boundingRect(contour)
        # Gett the plate
        licence_plate = gray_image[y:y+h, x:x+w]
        break


cv2.rectangle(image, (x, y), (x+w, y+h), (0,255, 0), 2)
licence_plate = cv2.bilateralFilter(licence_plate, 11, 17, 17)
(thresh, licence_plate) = cv2.threshold(licence_plate, 150, 180, cv2.THRESH_BINARY)
# Show all images
allImages = np.vstack([image_canny, image_canny])
# Displaying The Image
cv2.imshow("Licence Plate", image)
# Extract The number Plate
plate_id = pytesseract.image_to_string(licence_plate)
print(plate_id)
cv2.waitKey(0)