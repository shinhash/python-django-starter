from django.db import models
from third.utils import image_path_rename


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    password = models.CharField(max_length=20, default=None, null=True)
    image = models.ImageField("이미지", upload_to='images/', blank=True, null=True)
    image_origin_name = models.CharField(max_length=100, default=None, null=True)
    image_trance_name = models.CharField(max_length=100, default=None, null=True)
    image_view_path = models.CharField(max_length=100, default=None, null=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)