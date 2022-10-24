from PIL import ImageEnhance, ImageFilter, Image

from service.cleaner_service import delete_temp_files
from util.temp_file_creator import return_temp_file
from util.validator.validator import get_error_image_file, validate_new_value_for_retouch_type
from util.mapping.value_mapper import map_value, VALUES


def get_retouch_image_file(pillow_img, retouch_type, new_value):
    delete_temp_files('.jpeg')
    if not validate_new_value_for_retouch_type(retouch_type=retouch_type, new_value=new_value):
        error_message = f'Invalid {retouch_type} value: {new_value}\n' \
                        f'Valid range: [{VALUES[retouch_type].frontend_min}, {VALUES[retouch_type].frontend_max}]'
        return get_error_image_file(error_message)
    if retouch_type == 'brightness':
        enhancer = ImageEnhance.Brightness(pillow_img)
    elif retouch_type == 'contrast':
        enhancer = ImageEnhance.Contrast(pillow_img)
    elif retouch_type == 'color':
        enhancer = ImageEnhance.Color(pillow_img)
    elif retouch_type == 'sharpness':
        enhancer = ImageEnhance.Sharpness(pillow_img)
    elif retouch_type == 'blur':
        mapped_value = map_value(retouch_type, new_value)
        blured_image = pillow_img.filter(ImageFilter.GaussianBlur(mapped_value))
        temp_file = return_temp_file('.jpeg')
        blured_image.save(temp_file)
        return temp_file
    else:
        return f'Type {retouch_type} not recognised!'
    temp_file = return_temp_file('.jpeg')
    mapped_value = map_value(retouch_type, new_value)
    enhancer.enhance(mapped_value).save(temp_file)
    return temp_file


def retouch_image_all_in_one(pillow_image, values):
    delete_temp_files('.jpeg')
    for t in values.keys():
        v = float(values[t])
        if not validate_new_value_for_retouch_type(retouch_type=t, new_value=v):
            error_message = f'Invalid {t} value: {v}\n' \
                            f'Valid range: [{VALUES[t].frontend_min}, {VALUES[t].frontend_max}]'
            return get_error_image_file(error_message)

    mapped_brightness_value = map_value('brightness', float(values['brightness']))
    mapped_contrast_value = map_value('contrast', float(values['contrast']))
    mapped_color_value = map_value('color', float(values['color']))
    mapped_sharpness_value = map_value('sharpness', float(values['sharpness']))
    mapped_blur_value = map_value('blur', float(values['blur']))

    brightness_enhancer = ImageEnhance.Brightness(pillow_image)
    b_img = brightness_enhancer.enhance(mapped_brightness_value)

    contrast_enhancer = ImageEnhance.Contrast(b_img)
    contr_img = contrast_enhancer.enhance(mapped_contrast_value)

    color_enhancer = ImageEnhance.Color(contr_img)
    col_img = color_enhancer.enhance(mapped_color_value)

    sharpness_enhancer = ImageEnhance.Sharpness(col_img)
    sh_img = sharpness_enhancer.enhance(mapped_sharpness_value)

    blured_image = sh_img.filter(ImageFilter.GaussianBlur(mapped_blur_value))
    temp_file = return_temp_file('.jpeg')
    blured_image.save(temp_file)
    return temp_file


