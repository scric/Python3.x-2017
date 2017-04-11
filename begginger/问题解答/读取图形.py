import cv2
import numpy as np

img = cv2.imread('C:\Penguins.jpg')
cv2.imshow("Penguins", img)
cv2.waitKey(10000)