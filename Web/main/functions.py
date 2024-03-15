from django.db import models
from django.contrib.auth.models import User


def get_user(username):
    user = User.objects.get(username=username)
    first_name = user.first_name
    username = user.username
    password = user.password

    data = {"first_name": first_name, "username": username, "password": password}

    return data


def add_user(data):
    username = data.get("username")
    first_name = data.get("first_name")
    password = data.get("password")
    user = User.objects.create(username=username, first_name=first_name, password=password)
    user.save()


def update_user(username, data):
    new_username = data.get("username")
    first_name = data.get("first_name")
    password = data.get("password")

    if username is not None:
        User.objects.filter(username=username).update(username=new_username)
        User.save()

    if first_name is not None:
        User.objects.filter(username=username).update(first_name=first_name)
        User.save()

    if password is not None:
        User.objects.filter(username=username).update(password=password)
        User.save()


def delete_user(username):
    User.objects.get(username=username).delete()