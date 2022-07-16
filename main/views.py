from django.http import HttpResponse
from django.shortcuts import render

from main.models import Schedule

menu = [
    {"title": 'Мои записи', "url_name": "user_appointments"},
    {"title": 'Регистрация'},
    {"title": 'Вход'}
]

def main(request):
    context = {
        "title": "Главная",
        "menu": menu
    }
    return render(request, "main/main.html", context=context)


def user_appointments(request):
    appointments = Schedule.objects.all()
    return render(request, "main/user_appointments.html", {"title": "Мои записи", "appointments": appointments})





def show_appointment(request, appointment_id):
    return HttpResponse(f"Запись с id = {appointment_id}")

