from django.db import models


class pending(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_fulfilled=False)


class Order(models.Model):
    cus_name = models.TextField(max_length=400, null=False, default='Anonymous')
    cus_phone = models.CharField(max_length=500)
    cus_email = models.EmailField(max_length=500)
    cus_address = models.TextField(max_length=500)
    cus_city = models.CharField(max_length=500)
    cus_place = models.CharField(max_length=500, default="Not Know")
    cus_notes = models.TextField(max_length=2000)
    date_of_register = models.DateField(auto_now_add=True)
    is_fulfilled = models.BooleanField(default=False)

    objects = pending()
    all = models.Manager()
