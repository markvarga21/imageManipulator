import redis

from dto.Preset import Preset

redis_host = 'redis-13833.c293.eu-central-1-1.ec2.cloud.redislabs.com'
redis_port = 13833
redis_username = 'default'
redis_password = 'WKgodsiY9vEE5aYlfIv8VuVu5VKnbgQr'
USER_TABLE_NAME = 'USERS'
SESSIONS_TABLE_NAME = 'SESSIONS'
FORBIDDEN_WORDS_TABLE_NAME = 'FORBIDDEN_OBSCENE_WORDS'

rf = redis.Redis(host=redis_host,
                 port=redis_port,
                 username=redis_username,
                 password=redis_password,
                 decode_responses=True)


def persist_user_preset(preset: Preset) -> str:
    user_name = preset.user
    preset_name = preset.name
    if rf.sismember(f'{user_name}_PRESETS', preset_name):
        return f'Preset with name {preset_name} already exists for user {user_name}!'

    rf.sadd(f'{user_name}_PRESETS', preset_name)

    rf.hset(f'{user_name}_{preset_name}_PRESET', 'contrast', preset.contrast)
    rf.hset(f'{user_name}_{preset_name}_PRESET', 'brightness', preset.brightness)
    rf.hset(f'{user_name}_{preset_name}_PRESET', 'sharpness', preset.sharpness)
    rf.hset(f'{user_name}_{preset_name}_PRESET', 'color', preset.color)
    rf.hset(f'{user_name}_{preset_name}_PRESET', 'blur', preset.blur)

    return f'Persisted {preset_name} preset.'


def get_user_presets_in_repository(user_name: str) -> list:
    preset_names_for_user = rf.smembers(f'{user_name}_PRESETS')
    ret_ls = []
    for elem in preset_names_for_user:
        preset_dict = rf.hgetall(f'{user_name}_{elem}_PRESET')
        preset_dict['name'] = elem
        ret_ls.append(preset_dict)
    return ret_ls


def get_user_preset_for_user_and_name(user_name: str, preset_name: str) -> dict:
    return rf.hgetall(f'{user_name}_{preset_name}_PRESET')


def is_user_present(user_name: str) -> bool:
    return rf.sismember(USER_TABLE_NAME, user_name)


def register_user_in_repository(user_name: str) -> str:
    if rf.sismember(USER_TABLE_NAME, user_name):
        return f'Username: {user_name} already exists!'
    if user_name in rf.lrange(FORBIDDEN_WORDS_TABLE_NAME, 0, -1):
        return 'Username is forbidden or obscene!'
    rf.sadd(USER_TABLE_NAME, user_name)
    return f'User {user_name} registered successfully!'


def log_in_user_in_repository(user_name: str) -> str:
    if not is_user_present(user_name):
        return f'User {user_name} not exists!'
    if rf.sismember(SESSIONS_TABLE_NAME, user_name):
        return f'User {user_name} is already logged in!'

    rf.sadd(SESSIONS_TABLE_NAME, user_name)
    return f'User {user_name} logged in successfully!'


def logout_user_in_repository(user_name: str) -> str:
    if not is_user_present(user_name):
        return f'User {user_name} not exists!'
    if rf.scard(SESSIONS_TABLE_NAME) == 0:
        return 'Nobody is logged in. Please log in first before logout!'

    rf.srem(SESSIONS_TABLE_NAME, user_name)
    return f'User {user_name} logged out successfully!'
