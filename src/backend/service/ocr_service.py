from tempfile import TemporaryFile

import pytesseract
import cv2
import numpy as np

import uuid

import os

from service.cleaner_service import delete_temp_files, clean_output_for_user
from service.doc_creator import save_doc_file_in_output_folder
from service.pdf_creator import save_pdf_file_in_output_folder


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


def save_text_for_cv2_image(cv2_img, user_name: str) -> str:
    clean_output_for_user(user_name=user_name)
    save_id = uuid.uuid4()
    name = f'OCR_{user_name}_{save_id}.txt'
    path = os.path.join('resources', 'output', name)
    text = return_extracted_text_for_image(cv2_img=cv2_img)
    print(path)
    with open(path, 'w') as f:
        f.write(text)
    return path


def save_doc_for_cv2_image(cv2_img, font_size: int, user_name: str) -> TemporaryFile:
    delete_temp_files('.doc')
    text = return_extracted_text_for_image(cv2_img=cv2_img)
    path = save_doc_file_in_output_folder(text=text, font_size=font_size, user_name=user_name)
    return path
