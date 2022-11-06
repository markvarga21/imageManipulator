import cv2
import numpy as np
import uuid
import os
from PIL import Image

from service.cleaner_service import clean_back_remove_output_for_user


def remove_green_background(cv2_img, user_name: str) -> str:
    clean_back_remove_output_for_user(user_name=user_name)
    lab = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2LAB)
    a_channel = lab[:, :, 1]
    _, alpha = cv2.threshold(
        a_channel, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    b, g, r = cv2.split(cv2_img)
    rgba = [r, g, b, alpha]
    dst = cv2.merge(rgba, 4)

    save_id = uuid.uuid4()
    name = f'BACK_REMOVE_{user_name}_{save_id}.png'
    path = os.path.join('resources', 'output', name)

    cv2.imwrite(path, dst)
    return path


def remove_and_replace_background(cv2_img, pillow_background, user_name: str) -> str:
    path_for_png = remove_green_background(
        cv2_img=cv2_img, user_name=user_name)
    absolute_path = os.path.join(os.getcwd(), path_for_png)

    front_image = Image.open(absolute_path)
    front_image.convert('RGBA')
    pillow_background.convert('RGBA')
    # Calculate width to be at the center
    width = (pillow_background.width - front_image.width) // 2
    # Calculate height to be at the center
    height = (pillow_background.height - front_image.height) // 2

    pillow_background.paste(front_image, (width, height), front_image)

    save_id = uuid.uuid4()
    name = f'BACK_REMOVE_{user_name}_{save_id}.png'
    path = os.path.join('resources', 'output', name)

    pillow_background.save(path, format='png')
    return path
