from dto.Preset import Preset
from repository.preset_repository import persist_user_preset
from util.validator.validator import validate_new_value_for_retouch_type

RETOUCH_TYPE_NAMES = ['name', 'contrast', 'blur', 'sharpness', 'brightness', 'color']


def save_user_preset(preset_dict):
    keys = preset_dict.keys()
    if len(keys) is 0:
        return 'No keys present!'
    if 'name' not in keys:
        return 'Name not defined!'
    for t in RETOUCH_TYPE_NAMES:
        if t not in keys:
            return f'{t} type is empty!'
    for t in keys:
        if t not in RETOUCH_TYPE_NAMES:
            return f'{t} retouch type is not supported!'

    for t in RETOUCH_TYPE_NAMES[1:]:
        if not validate_new_value_for_retouch_type(t, float(preset_dict[t])):
            return f'Value {preset_dict[t]} for type {t} is invalid!'

    preset_name = preset_dict['name']
    contrast = float(preset_dict['contrast'])
    blur = float(preset_dict['blur'])
    brightness = float(preset_dict['brightness'])
    color = float(preset_dict['color'])
    sharpness = float(preset_dict['sharpness'])

    pr = Preset(contrast=contrast, brightness=brightness, sharpness=sharpness, color=color, blur=blur)
    persist_user_preset(pr)
    return f'Preset {preset_name}:\n{pr}\nsaved successfully!'
