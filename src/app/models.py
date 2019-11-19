from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Customer(models.Model):
    """Model definition for Customer."""
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=8)
    address= models.TextField(blank=True)
    
    class Meta:
        """Meta definition for Customer."""

        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.user.username

class Location(models.Model):
    """Model definition for Location."""
    name = models.CharField(max_length=50)
    address= models.TextField(blank=False)

    class Meta:
        """Meta definition for Location."""

        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.name

class Employee(models.Model):
    """Model definition for Employee."""
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    phone = models.CharField(max_length=8)
    address= models.TextField(blank=True)
    location = models.ForeignKey(Location,on_delete= models.PROTECT)
    class Meta:
        """Meta definition for Employee."""

        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.user.username

class Package(models.Model):
    """Model definition for Package."""
    code = models.CharField(max_length=13)
    sender = models.ForeignKey(Customer,on_delete= models.CASCADE)
    consignee = models.TextField(blank=False)
    destination = models.TextField(blank=False)
    phone = models.CharField(max_length=8)
    charge = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    charge_status = models.BooleanField(default=False)
    status = models.CharField(max_length=11)
    weight = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    note  = models.TextField(blank=True)
    employee = models.ForeignKey(Employee,on_delete= models.PROTECT)
    

    class Meta:
        """Meta definition for Package."""
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'

    def __str__(self):
        return self.code