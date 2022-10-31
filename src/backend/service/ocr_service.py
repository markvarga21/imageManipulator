import pytesseract
import cv2
import numpy as np


def return_extracted_text_for_image(cv2_img) -> str:
    gray = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2GRAY)
    gray, img_bin = cv2.threshold(gray, 128, 255, cv2.THRESH_OTSU)
    gray_bitwise = cv2.bitwise_not(img_bin)
    kernel = np.ones((6, 6), np.uint8)
    dilated = cv2.dilate(gray_bitwise, kernel, cv2.BORDER_REFLECT)
    ret = pytesseract.image_to_string(dilated)
    return ret
