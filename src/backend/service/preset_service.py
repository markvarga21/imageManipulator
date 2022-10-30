from dto.Preset import Preset
from repository.repository import persist_user_preset, is_user_present, get_user_presets_in_repository, \
    get_user_preset_for_user_and_name
from util.mapping.value_mapper import map_value_from_frontend_to_pillow

RETOUCH_TYPE_NAMES = ['userName', 'name', 'contrast', 'blur', 'sharpness', 'brightness', 'color']


def save_user_preset(preset_dict: dict) -> str:
    keys = preset_dict.keys()
    if len(keys) is 0:
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
    contrast = map_value_from_frontend_to_pillow('contrast', float(preset_dict['contrast']))
    blur = map_value_from_frontend_to_pillow('blur', float(preset_dict['blur']))
    brightness = map_value_from_frontend_to_pillow('brightness', float(preset_dict['brightness']))
    color = map_value_from_frontend_to_pillow('color', float(preset_dict['color']))
    sharpness = map_value_from_frontend_to_pillow('sharpness', float(preset_dict['sharpness']))

    pr = Preset(user=user_name, name=preset_name, contrast=contrast, brightness=brightness, sharpness=sharpness, color=color, blur=blur)
    return persist_user_preset(pr)


def get_presets_for_user_in_service(d: dict) -> list:
    keys = d.keys()
    if len(keys) is 0:
        return []
    if 'userName' not in keys:
        return []

    user_name = d['userName']
    return get_user_presets_in_repository(user_name)


def get_preset_for_user_in_service(d: dict) -> dict:
    keys = d.keys()
    if len(keys) is 0:
        return dict()
    if 'userName' not in keys:
        return dict()
    if 'presetName' not in keys:
        return dict()

    user_name = d['userName']
    preset_name = d['presetName']

    return get_user_preset_for_user_and_name(user_name, preset_name)
