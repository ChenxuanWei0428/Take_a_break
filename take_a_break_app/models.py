from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"username: {self.username}, email: {self.email}, password: {self.password}"

class websites(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return f"name: {self.name}, url: {self.url}"

class user_web(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="fav_webs")
    websites = models.ForeignKey(websites, on_delete=models.CASCADE)

    def __str__(self):
        return f"user: {self.user}, websites: {self.websites}"
