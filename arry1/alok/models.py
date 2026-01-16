from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

class AlokReview(models.Model):
    ALOK_TYPE = [
        ('B', 'BLACK'),
        ('W', 'WHITE'),
        ('CH', 'CHOCOLATE'),
    ]
    alok = models.ForeignKey(AlokVarity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now, null=True, blank=True)
    type = models.CharField(max_length=2, choices=ALOK_TYPE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.review[:20]}"
    
class AlokCertificate(models.Model):
    alok = models.ForeignKey(AlokVarity, on_delete=models.CASCADE, related_name='certificate')    
    certificate_number = models.CharField(max_length=100)
    issued_date= models.DateTimeField(default=timezone.now, null=True, blank=True)
    valit_untill= models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Certificate: {self.alok.name} - {self.certificate_number}"