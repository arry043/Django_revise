from django.db import models
from django.utils import timezone

# Create your models here.
class AlokVarity(models.Model):
    ALOK_TYPE = [
        ('B', 'BLACK'),
        ('W', 'WHITE'),
        ('CH', 'CHOCOLATE'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='alok_images/', null=True, blank=True)
    date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    type = models.CharField(max_length=2, choices=ALOK_TYPE, null=True, blank=True)


    def __str__(self):
        return self.name