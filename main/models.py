from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


class User(models.Model):
    full_name = models.CharField(max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Номер телефона должен соответствовать формату: '+799999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return self.full_name


class Appointment(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    dt = models.DateField(null=True)
    tm = models.TimeField(null=True)

    def get_absolute_url(self):
        return reverse('appointment', kwargs={'appointment_id': self.pk})


class Schedule(models.Model):
    day_of_week_regex = RegexValidator(regex=r'^Понедельник|Вторник|Среда|Четверг|Пятница|Суббота|Воскресенье$')
    day_of_week = models.CharField(validators=[day_of_week_regex], max_length=11)
    time = models.TimeField()
    coach = models.ForeignKey('Coach', on_delete=models.SET_NULL, null=True)


class Coach(models.Model):
    full_name = models.CharField(max_length=255)

