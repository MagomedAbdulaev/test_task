import json
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LoginPersonForm
from .models import *
from django.core.exceptions import ObjectDoesNotExist


@login_required
def home(request):

    user = Person.objects.get(id=request.user.id)
    clients = user.clients.all()

    context = {
        'title': 'Главная',
        'clients': clients,
    }

    return render(request, 'home.html', context)


def client_status_fetch(request):

    client_id = json.loads(request.body.decode())['client_id']
    status = json.loads(request.body.decode())['type']

    client = Client.objects.get(id=client_id)
    if status == 'at_work':
        client.status = 3
    elif status == 'deal_closed':
        client.status = 1
    elif status == 'reject':
        client.status = 2
    client.save()

    obj = {
        'status': 'ok'
    }

    return JsonResponse(obj)


def login_user(request):

    if request.method == 'POST':
        login_form = LoginPersonForm(request.POST)
        if login_form.is_valid():
            try:
                user = Person.objects.get(username=request.POST['username'])
                if check_password(request.POST['password'], user.password) or request.POST['password'] == user.password:  # Я поставил or потому-что пароль может быть хэширован, а может и нет. Check_password() хэширует и сравнивает
                    login(request, user)
                    return redirect('test_task_app:home')
                else:
                    login_form.add_error('password', 'Неверный пароль')
            except ObjectDoesNotExist:
                login_form.add_error('username', 'Пользователя с таким логином не существует')

    else:
        login_form = LoginPersonForm()

    context = {
        'title': 'Авторизация',
        'login_form': login_form,
    }

    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('test_task_app:login_user')
