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


def map_contrast_value_to_pillow_value(value):
    if value == 0:
        print(f'Old value: {value}, new value: {1}')
        return 1.0
    new_value = map_value(value,
                          CONTRAST_FRONTEND_MIN,
                          CONTRAST_FRONTEND_MAX,
                          CONTRAST_PILLOW_MIN,
                          CONTRAST_PILLOW_MAX)

    print(f'Old value: {value}, new value: {new_value}')
    return new_value


def map_brightness_value_to_pillow_value(value):
    if value == 0:
        print(f'Old value: {value}, new value: {1}')
        return 1.0
    new_value = map_value(value,
                          BRIGHTNESS_FRONTEND_MIN,
                          BRIGHTNESS_FRONTEND_MAX,
                          BRIGHTNESS_PILLOW_MIN,
                          BRIGHTNESS_PILLOW_MAX)

    print(f'Old value: {value}, new value: {new_value}')
    return new_value


def map_color_value_to_pillow_value(value):
    if value == 0:
        print(f'Old value: {value}, new value: {1}')
        return 1.0
    new_value = map_value(value,
                          COLOR_FRONTEND_MIN,
                          COLOR_FRONTEND_MAX,
                          COLOR_PILLOW_MIN,
                          COLOR_PILLOW_MAX)

    print(f'Old value: {value}, new value: {new_value}')
    return new_value


def map_value(value, old_min, old_max, new_min, new_max):
    old_range = (old_max - old_min)
    new_range = (new_max - new_min)
    new_value = (((value - old_min) * new_range) / old_range) + new_min

    return new_value
