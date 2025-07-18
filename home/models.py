# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Vehicle(models.Model):

    #__Vehicle_FIELDS__
    brand = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    chassis_number = models.CharField(max_length=255, null=True, blank=True)
    registration_number = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    engine_size = models.IntegerField(null=True, blank=True)
    fuel_type = models.CharField(max_length=255, null=True, blank=True)
    gearbox_type = models.CharField(max_length=255, null=True, blank=True)
    mileage = models.IntegerField(null=True, blank=True)
    panoramic_roof = models.BooleanField()
    purchase_price = models.IntegerField(null=True, blank=True)
    date_of_purchase = models.DateTimeField(blank=True, null=True, default=timezone.now)
    active = models.BooleanField()

    #__Vehicle_FIELDS__END

    class Meta:
        verbose_name        = _("Vehicle")
        verbose_name_plural = _("Vehicle")


class Rental(models.Model):

    #__Rental_FIELDS__
    customer_contact = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    daily_price = models.IntegerField(null=True, blank=True)
    commission_percent = models.IntegerField(null=True, blank=True)
    total_amount = models.IntegerField(null=True, blank=True)

    #__Rental_FIELDS__END

    class Meta:
        verbose_name        = _("Rental")
        verbose_name_plural = _("Rental")


class Expense(models.Model):

    #__Expense_FIELDS__
    vehicle = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    category = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)

    #__Expense_FIELDS__END

    class Meta:
        verbose_name        = _("Expense")
        verbose_name_plural = _("Expense")


class Maintenancerecord(models.Model):

    #__Maintenancerecord_FIELDS__
    mileage = models.IntegerField(null=True, blank=True)
    service_description = models.TextField(max_length=255, null=True, blank=True)
    cost = models.IntegerField(null=True, blank=True)

    #__Maintenancerecord_FIELDS__END

    class Meta:
        verbose_name        = _("Maintenancerecord")
        verbose_name_plural = _("Maintenancerecord")



#__MODELS__END
