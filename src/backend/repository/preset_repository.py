import redis

redis_host = 'redis-13833.c293.eu-central-1-1.ec2.cloud.redislabs.com'
redis_port = 13833
redis_username = 'default'
redis_password = 'WKgodsiY9vEE5aYlfIv8VuVu5VKnbgQr'
USER_TABLE_NAME = 'USERS'
SESSIONS_TABLE_NAME = 'SESSIONS'

rf = redis.Redis(host=redis_host,
                 port=redis_port,
                 username=redis_username,
                 password=redis_password,
                 decode_responses=True)


def persist_user_preset(preset):
    print(f'Persisting {preset}')


def is_user_present(user_name):
    return rf.sismember(USER_TABLE_NAME, user_name)


def register_user_in_repository(user_name):
    if rf.sismember(USER_TABLE_NAME, user_name):
        return f'Username: {user_name} already exists!'
    rf.sadd(USER_TABLE_NAME, user_name)
    return f'User {user_name} registered successfully!'


def log_in_user_in_repository(user_name):
    if not is_user_present(user_name):
        return f'User {user_name} not exists!'
    if rf.sismember(SESSIONS_TABLE_NAME, user_name):
        return f'User {user_name} is already logged in!'

    rf.sadd(SESSIONS_TABLE_NAME, user_name)
    return f'User {user_name} logged in successfully!'


def logout_user_in_repository(user_name):
    if not is_user_present(user_name):
        return f'User {user_name} not exists!'
    if rf.scard(SESSIONS_TABLE_NAME) == 0:
        return 'Nobody is logged in. Please log in first before logout!'

    rf.srem(SESSIONS_TABLE_NAME, user_name)
    return f'User {user_name} logged out successfully!'
