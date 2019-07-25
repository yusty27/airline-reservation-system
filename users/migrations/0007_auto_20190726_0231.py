# Generated by Django 2.2 on 2019-07-25 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0002_travelling_flight_image'),
        ('users', '0006_auto_20190726_0218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='booked',
        ),
        migrations.CreateModel(
            name='BookingBy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline.Booking')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]