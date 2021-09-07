from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='pic_img', default="")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.owner.username