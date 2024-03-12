from django.db import models

class User(models.Model):
    nickname = models.CharField(blank=False, max_length=75, null=False)
    login = models.CharField(blank=False, max_length=100, unique=True, null=False)
    password = models.CharField(blank=False, max_length=50, null=False)


    def __str__(self):
        return f'{self.login}'


