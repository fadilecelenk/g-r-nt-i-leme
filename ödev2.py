import cv2
import numpy as np


image = cv2.imread('resim.jpg')


hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])


mask = cv2.inRange(hsv, lower_red, upper_red)


result = cv2.bitwise_and(image, image, mask=mask)


cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", image)

cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
cv2.imshow("Result", result)


cv2.waitKey(0)
cv2.destroyAllWindows()
