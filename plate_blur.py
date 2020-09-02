import numpy as np
import matplotlib.pyplot as plt
import cv2
%matplotlib inline


def blur_plate(img):
    plate_img = img.copy()
    roi = img.copy()
    plate_rectangle = plate.detectMultiScale(plate_img, scaleFactor=1.2, minNeighbors=5)
    for (x, y, w, h) in plate_rectangle:
        roi = roi[y:y+h, x:x+w]
        blur = cv2.medianBlur(roi, ksize=9)
        plate_img[y:y+h, x:x+w] = blur
    return plate_img


plate = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

img = cv2.imread('car_plate.jpg')

result = blur_plate(img)

cv2.namedWindow('Image')

while True:
    cv2.imshow('Image', result)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
