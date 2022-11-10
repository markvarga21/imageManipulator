from dto.Preset import Preset
from repository.repository import persist_user_preset, is_user_present, get_user_presets_in_repository, \
    get_user_preset_for_user_and_name
from util.mapping.value_mapper import map_value_from_frontend_to_pillow, map_value_from_pillow_to_frontend

RETOUCH_TYPE_NAMES = ['userName', 'name', 'contrast',
                      'blur', 'sharpness', 'brightness', 'color']


def save_user_preset(preset_dict: dict) -> str:
    keys = preset_dict.keys()
    if len(keys) == 0:
        return 'No keys present!'
    if 'name' not in keys:
        return 'Name not defined!'
    if 'userName' not in keys:
        return 'No userName parameter present!'

    for t in RETOUCH_TYPE_NAMES:
        if t not in keys:
            return f'{t} type is empty!'
    for t in keys:
        if t not in RETOUCH_TYPE_NAMES:
            return f'{t} retouch type is not supported!'

    user_name = str(preset_dict['userName'])

    if not is_user_present(user_name):
        return f'User {user_name} is not registered!'

    preset_name = str(preset_dict['name'])
    contrast = map_value_from_frontend_to_pillow(
        'contrast', float(preset_dict['contrast']))
    blur = map_value_from_frontend_to_pillow(
        'blur', float(preset_dict['blur']))
    brightness = map_value_from_frontend_to_pillow(
        'brightness', float(preset_dict['brightness']))
    color = map_value_from_frontend_to_pillow(
        'color', float(preset_dict['color']))
    sharpness = map_value_from_frontend_to_pillow(
        'sharpness', float(preset_dict['sharpness']))

    pr = Preset(user=user_name, name=preset_name, contrast=contrast,
                brightness=brightness, sharpness=sharpness, color=color, blur=blur)
    return persist_user_preset(pr)


def get_presets_for_user_in_service(d: dict) -> list:
    keys = d.keys()
    if len(keys) == 0:
        return []
    if 'userName' not in keys:
        return []

    user_name = d['userName']
    preset_dict_list = get_user_presets_in_repository(user_name=user_name)
    frontend_dict_list = []

    for preset in preset_dict_list:
        frontend_contrast = map_value_from_pillow_to_frontend(
            'contrast', float(preset['contrast']))
        frontend_brightness = map_value_from_pillow_to_frontend(
            'brightness', float(preset['brightness']))
        frontend_sharpness = map_value_from_pillow_to_frontend(
            'sharpness', float(preset['sharpness']))
        frontend_color = map_value_from_pillow_to_frontend(
            'color', float(preset['color']))
        frontend_blur = map_value_from_pillow_to_frontend(
            'blur', float(preset['blur']))

        frontend_dict = {
            'blur': round(frontend_blur, 1),
            'brightness': round(frontend_brightness, 1),
            'color': round(frontend_color, 1),
            'contrast': round(frontend_contrast, 1),
            'sharpness': round(frontend_sharpness, 1)
        }

        frontend_dict_list.append(frontend_dict)

    return frontend_dict_list


def get_preset_for_user_in_service(d: dict) -> dict:
    keys = d.keys()
    if len(keys) == 0:
        return dict()
    if 'userName' not in keys:
        return dict()
    if 'presetName' not in keys:
        return dict()

    user_name = d['userName']
    preset_name = d['presetName']

    preset_dict = get_user_preset_for_user_and_name(user_name, preset_name)
    frontend_contrast = map_value_from_pillow_to_frontend(
        'contrast', float(preset_dict['contrast']))
    frontend_brightness = map_value_from_pillow_to_frontend(
        'brightness', float(preset_dict['brightness']))
    frontend_sharpness = map_value_from_pillow_to_frontend(
        'sharpness', float(preset_dict['sharpness']))
    frontend_color = map_value_from_pillow_to_frontend(
        'color', float(preset_dict['color']))
    frontend_blur = map_value_from_pillow_to_frontend(
        'blur', float(preset_dict['blur']))

    frontend_dict = {
        'blur': round(frontend_blur, 1),
        'brightness': round(frontend_brightness, 1),
        'color': round(frontend_color, 1),
        'contrast': round(frontend_contrast, 1),
        'sharpness': round(frontend_sharpness, 1)
    }

    return frontend_dict
