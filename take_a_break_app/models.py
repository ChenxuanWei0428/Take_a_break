from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"username: {self.username}, email: {self.email}, password: {self.password}"


class website(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return f"name: {self.name}, url: {self.url}"
