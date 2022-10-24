CONTRAST_FRONTEND_MIN = -10
CONTRAST_FRONTEND_MAX = 10
CONTRAST_PILLOW_MAX = 2.0
CONTRAST_PILLOW_MIN = 0.5


def map_contrast_value_to_pillow_value(value):
    if value == 0:
        return 1.0
    frontend_contrast_range = CONTRAST_FRONTEND_MAX - CONTRAST_FRONTEND_MIN
    pillow_contrast_range = CONTRAST_PILLOW_MAX - CONTRAST_PILLOW_MIN
    new_value = (((value - CONTRAST_FRONTEND_MIN) * pillow_contrast_range)
                 / frontend_contrast_range) + CONTRAST_PILLOW_MIN
    print(f'Old value: {value}, new value: {new_value}')
    return new_value
