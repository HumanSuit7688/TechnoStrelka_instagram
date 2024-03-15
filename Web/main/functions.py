from django.db import models
from main.models import User


def get_user(login):
    user = User.objects.get(login=login)
    nickname = user.nickname
    login = user.login
    password = user.password

    data = {"nickname": nickname, "login": login, "password": password}

    return data


def add_user(data):
    login = data.get("login")
    nickname = data.get("nickname")
    password = data.get("password")
    user = User.objects.create(login=login, nickname=nickname, password=password)
    user.save()


def update_user(login, data):
    new_login = data.get("login")
    nickname = data.get("nickname")
    password = data.get("password")

    if login is not None:
        User.objects.filter(login=login).update(login=new_login)
        User.save()

    if nickname is not None:
        User.objects.filter(login=login).update(nickname=nickname)
        User.save()

    if password is not None:
        User.objects.filter(login=login).update(password=password)
        User.save()


def delete_user(login):
    User.objects.get(login=login).delete()