from dto.ValueRange import ValueRange

CONTRAST_FRONTEND_MIN = -10
CONTRAST_FRONTEND_MAX = 10
CONTRAST_PILLOW_MAX = 2.0
CONTRAST_PILLOW_MIN = 0.5

COLOR_FRONTEND_MIN = -10
COLOR_FRONTEND_MAX = 10
COLOR_PILLOW_MAX = 2.0
COLOR_PILLOW_MIN = 0.5

BRIGHTNESS_FRONTEND_MIN = -10
BRIGHTNESS_FRONTEND_MAX = 10
BRIGHTNESS_PILLOW_MAX = 2.0
BRIGHTNESS_PILLOW_MIN = 0.5

SHARPNESS_FRONTEND_MIN = 0
SHARPNESS_FRONTEND_MAX = 20
SHARPNESS_PILLOW_MAX = 2.0
SHARPNESS_PILLOW_MIN = 0.5

BLUR_FRONTEND_MIN = 0
BLUR_FRONTEND_MAX = 20
BLUR_PILLOW_MAX = 2.0
BLUR_PILLOW_MIN = 0.0

VALUES = {
    'color': ValueRange(COLOR_FRONTEND_MIN, COLOR_FRONTEND_MAX, COLOR_PILLOW_MIN, COLOR_PILLOW_MAX),
    'contrast': ValueRange(CONTRAST_FRONTEND_MIN, CONTRAST_FRONTEND_MAX, CONTRAST_PILLOW_MIN, CONTRAST_PILLOW_MAX),
    'sharpness': ValueRange(SHARPNESS_FRONTEND_MIN, SHARPNESS_FRONTEND_MAX, SHARPNESS_PILLOW_MIN, SHARPNESS_PILLOW_MAX),
    'brightness': ValueRange(BRIGHTNESS_FRONTEND_MIN, BRIGHTNESS_FRONTEND_MAX, BRIGHTNESS_PILLOW_MIN, BRIGHTNESS_PILLOW_MAX),
    'blur': ValueRange(BLUR_FRONTEND_MIN, BLUR_FRONTEND_MAX, BLUR_PILLOW_MIN, BLUR_PILLOW_MAX)
}


def map_value_from_frontend_to_pillow(retouch_type: str, value: float) -> float:
    if value == 0 and retouch_type != 'blur':
        print(f'Old value: {value}, new value: {1}')
        return 1.0
    if value == 0 and retouch_type == 'blur':
        return 0.0
    new_value = map_ranges(value,
                           VALUES[retouch_type].frontend_min,
                           VALUES[retouch_type].frontend_max,
                           VALUES[retouch_type].pillow_min,
                           VALUES[retouch_type].pillow_max)
    return new_value


def map_value_from_pillow_to_frontend(retouch_type: str, value: float) -> float:
    if value == 0 and retouch_type != 'blur':
        print(f'Old value: {value}, new value: {1}')
        return 1.0
    if value == 0 and retouch_type == 'blur':
        return 0.0
    new_value = map_ranges(value,
                           VALUES[retouch_type].pillow_min,
                           VALUES[retouch_type].pillow_max,
                           VALUES[retouch_type].frontend_min,
                           VALUES[retouch_type].frontend_max)
    return new_value


def map_ranges(value: float, old_min: float, old_max: float, new_min: float, new_max: float) -> float:
    old_range = (old_max - old_min)
    new_range = (new_max - new_min)
    new_value = (((value - old_min) * new_range) / old_range) + new_min

    return new_value
