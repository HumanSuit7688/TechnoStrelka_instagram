from django.db import models
from models import User


def get_user(id):
    user = User.objects.get(id=id)
    nickname = user.nickname
    login = user.login
    password = user.password

    data = {"nickname": nickname, "login": login, "password": password}

    return data


def add_user(data):
    login = data.get("login")
    nickname = data.get("nickname")
    password = data.get("password")

    User.objects.create(login=login, nickname=nickname, password=password)
    User.save()


def update_user(id, data):
    login = data.get("login")
    nickname = data.get("nickname")
    password = data.get("password")

    if login is not None:
        User.objects.filter(id=id).update(login=login)
        User.save()

    if nickname is not None:
        User.objects.filter(id=id).update(nickname=nickname)
        User.save()

    if password is not None:
        User.objects.filter(id=id).update(password=password)
        User.save()


def delete_user(id):
    User.objects.get(id=id).delete()