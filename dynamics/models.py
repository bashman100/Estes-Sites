from django.db import models

# Create your models here.

# For priceing teirs
class Price(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_page = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=4)
    price_base = models.DecimalField(decimal_places=2, max_digits=6)
    num_page_max = models.DecimalField(decimal_places=0, max_digits=2)
    num_page_base = models.DecimalField(decimal_places=0, max_digits=2)
    is_dynamic = models.BooleanField()
    note = models.TextField()

    def __str__(self):
        return self.name

# For sites we have made
class Site(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(decimal_places=2, max_digits=6)
    price_teir = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    date_made = models.DateTimeField()
    note = models.TextField()

    def __str__(self):
        return self.names

# For our communication
class Note(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    creater = models.CharField(max_length=125)

    def __str__(self):
        return self.names
