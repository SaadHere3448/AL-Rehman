from django.db import models


class All(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_hidden=False)


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='Product-Images')
    category = models.CharField(max_length=400)
    description = models.TextField(max_length=5000)
    code = models.CharField(max_length=200, default="000000")
    date = models.DateField(auto_now_add=True)
    is_hidden = models.BooleanField(default=False)

    objects = All()
    admin = models.Manager()
