from werkzeug.security import safe_str_cmp
from app.models.User import UserModel


def authenticate_by_email(email, password):
    user = UserModel.find_by_email(email)
    if user and safe_str_cmp(user.password, password):
        return user


def authenticate_by_phone(phone, password):
    user = UserModel.find_by_phone(phone)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
