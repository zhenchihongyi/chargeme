from django.db import models
from django.utils import timezone


class Order(models.Model):
    id=models.AutoField(primary_key=True,max_length=12)
    user_id = models.ForeignKey('auth.User')
    station_id_borrow = models.ForeignKey('Station', related_name='station_id_borrow')
    station_id_return = models.ForeignKey('Station', related_name='station_id_return', null=True)
    battery_id = models.IntegerField(null=True)
    start_time = models.DateTimeField(
            default=timezone.now)
    end_time = models.DateTimeField(null=True)
    price=models.PositiveIntegerField(null=True)
    memo = models.TextField(null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.id)


class Station(models.Model):
    id=models.IntegerField(primary_key=True)
    provider = models.CharField(max_length=30)
    model_name = models.CharField(max_length=30)
    contract_id = models.ForeignKey('Contract')

    def __str__(self):
        return str(self.id)


class Contract(models.Model):
    id = models.IntegerField(primary_key=True)
    location_id = models.ForeignKey('Location')
    contact_start_date = models.DateTimeField(null=True)
    contact_end_date = models.DateTimeField(null=True)
    Commission_rate=models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return str(self.id)


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    company_id = models.ForeignKey('Company')
    location_name= models.CharField(max_length=100)
    PIC = models.CharField(max_length=30)
    post_code = models.CharField(max_length=7)
    tel = models.CharField(max_length=12)
    address_country = models.CharField(max_length=30)
    address_prefecture = models.CharField(max_length=30)
    address_city = models.CharField(max_length=30)
    address_detail= models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=100)
    PIC = models.CharField(max_length=30)
    post_code = models.CharField(max_length=7)
    tel = models.CharField(max_length=12)
    address_country = models.CharField(max_length=30)
    address_prefecture = models.CharField(max_length=30)
    address_city = models.CharField(max_length=30)
    address_detail= models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)
