from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.name

    
class Appointment(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    client_name = models.CharField(max_length=100)

    email = models.EmailField()

    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    notes = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.service.name}"