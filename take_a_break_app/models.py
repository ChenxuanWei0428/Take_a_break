from django.db import models
from django.contrib.auth.models import User


class Websites(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return f"name: {self.name}, url: {self.url}"

class User_web(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="fav_webs")
    websites = models.ManyToManyField(Websites, blank=True)

    def __str__(self):
        return f"user: {self.user}, websites: {self.websites}"
