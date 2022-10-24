from repository.preset_repository import register_user_in_repository, log_in_user_in_repository, \
    logout_user_in_repository


def register_user_in_service(user_dict):
    if not is_user_name_present(user_dict=user_dict):
        return 'Key \'userName\' not present in query parameters!'
    user_name = user_dict['userName']
    return register_user_in_repository(user_name)


def is_user_name_present(user_dict):
    return 'userName' in user_dict.keys()


def log_in_user_in_service(user_dict):
    if not is_user_name_present(user_dict=user_dict):
        return 'Key \'userName\' not present in query parameters!'
    user_name = user_dict['userName']
    return log_in_user_in_repository(user_name)


def logout_user_in_service(user_dict):
    if not is_user_name_present(user_dict=user_dict):
        return 'Key \'userName\' not present in query parameters!'
    user_name = user_dict['userName']
    return logout_user_in_repository(user_name)



