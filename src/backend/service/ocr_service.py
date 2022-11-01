from tempfile import TemporaryFile

import pytesseract
import cv2
import numpy as np

from service.pdf_creator_service import save_pdf_file_in_output_folder


def return_extracted_text_for_image(cv2_img) -> str:
    gray = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2GRAY)
    gray, img_bin = cv2.threshold(gray, 128, 255, cv2.THRESH_OTSU)
    gray_bitwise = cv2.bitwise_not(img_bin)
    kernel = np.ones((6, 6), np.uint8)
    dilated = cv2.dilate(gray_bitwise, kernel, cv2.BORDER_REFLECT)
    ret = pytesseract.image_to_string(dilated)
    return ret


def save_pdf_for_cv2_image(cv2_img, r: int, g: int, b: int, size: int, user_name: str) -> str:
    text = return_extracted_text_for_image(cv2_img=cv2_img)
    path = save_pdf_file_in_output_folder(text=text, r=r, g=g, b=b, font_size=size, user_name=user_name)
    return path
