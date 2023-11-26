import cv2
import matplotlib.pyplot as plt


def calculate_histogram(image):
    img = cv2.imread("museum.jpg", cv2.IMREAD_GRAYSCALE)

    x, y = img.shape

    histogram = [0] * 256
    for i in range(x):
        for j in range(y):
            pixel_value = img[i, j]
            histogram[pixel_value] += 1

    return histogram
