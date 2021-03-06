# Generated by Django 2.2.6 on 2019-11-03 19:27

from django.db import migrations
from faker import Faker
from django.utils import timezone
from bookings.models import User, Booking
import numpy as np
import datetime

faker = Faker()

def usersTableSeeder(apps, schema_editor):
    User = apps.get_model('bookings', 'User')

    for i in range(0, 5):
        user = User()
        user.first_name = faker.first_name()
        user.surename = faker.last_name()
        user.save()

def bookingsTableSeeder(apps, schema_editor):
    booking_name = ['Air Asia', 'Hotel Tentrem', 'Dufan']
    Booking = apps.get_model('bookings', 'Booking')

    for i in range(1, 6):
        for j in range(0, 3):
            booking = Booking()
            booking.name = booking_name[j]
            booking.type = j
            booking.time_begin = timezone.now()
            booking.time_end = timezone.now() + datetime.timedelta(days=np.random.randint(0, 2), hours=np.random.randint(0, 23))
            if(j!=0):
                booking.location = faker.address()
            else:
                booking.location = 'ID - JP'
            user = apps.get_model('bookings', 'User').objects.get(id=i)
            booking.user = user
            booking.save()

class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(usersTableSeeder),
        migrations.RunPython(bookingsTableSeeder),
    ]
