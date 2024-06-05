from django.db import models

class Employee(models.Model):
    firstName = models.CharField(max_length = 20)
    lastName = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="images")
    designation = models.CharField(max_length=50)
    emailAddress = models.EmailField(max_length=50, unique=True)
    phoneNumber = models.CharField(max_length=10, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstName + " "+  self.lastName

