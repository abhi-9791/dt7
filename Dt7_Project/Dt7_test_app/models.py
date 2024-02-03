from django.db import models
class Contact_Us(models.Model):
    MARKETING_CHOICES = [
        ('sales', 'Sales'),
        ('careers', 'Careers'),
        ('others', 'Others'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    marketing = models.CharField(max_length=10, choices=MARKETING_CHOICES)
    message = models.TextField()

    def __str__(self):
        return self.name