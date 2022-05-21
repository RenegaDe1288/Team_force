from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.views import LogoutView
from .forms import CreateUserForm, LoginForm, AddHobbyForm, ChoiceHobbyform
from candidates.models import *


class CandidatesList(ListView):
    """Отображение списка кандидатов"""
    model = Candidate
    template_name = 'main.html'
    context_object_name = 'candidates'


def show_account(request):
    """Отображение данных кандидата"""
    if request.method == 'POST':
        data = request.POST
        user = Candidate.objects.get(name=request.user.username)
        if 'delete' in data:
            hobby = Hobby.objects.get(name__startswith=data['delete'])
            user.hobby.remove(hobby.id)
        elif 'choice' in data:
            new_form = ChoiceHobbyform(request.POST)
            new_form.get_context()
            new_hobby = new_form.cleaned_data.get('hobby')
            [user.hobby.add(Hobby.objects.get(name=title)) for title in new_hobby]
        elif 'add' in data:
            new_form = AddHobbyForm(request.POST)
            new_form.get_context()
            new_hobby = new_form.cleaned_data.get('hobby2')
            if Hobby.objects.filter(name=new_hobby):
                message = 'Данное хобби уже существует'
                return HttpResponse(message)
            elif new_hobby == '':
                message = 'Не введено хобби'
                return HttpResponse(message)
            new_hobby = Hobby.objects.create(name=new_hobby)
            user.hobby.add(new_hobby)
        return redirect('/account')
    else:
        if request.user.is_authenticated:
            user = Candidate.objects.get(name=request.user.username)
            form, form_2 = ChoiceHobbyform, AddHobbyForm
            return render(request, 'account.html', {'user': user, 'form2': form_2, 'form': form})
        else:
            redirect('/login')


def register_user(request):
    """Регистрация кандидата"""
    if request.method == 'POST':
        new_form = CreateUserForm(request.POST)
        new_form.get_context()
        name = new_form.cleaned_data.get('username')
        surname = new_form.cleaned_data.get('surname')
        lastname = new_form.cleaned_data.get('lastname')
        skill = new_form.cleaned_data.get('skill')
        language = new_form.cleaned_data.get('language')
        password = new_form.cleaned_data.get('password1')
        if new_form.is_valid():
            user = Candidate.objects.create(name=name, surname=surname, lastname=lastname)
            [user.skill.add(Skill.objects.get(name=title)) for title in skill]
            [user.language.add(Language.objects.get(name=title)) for title in language]
            user = User.objects.create(username=name, last_name=lastname, password=password)
            login(request, user)
            return redirect('/main')
        else:
            new_form.add_error('__all__', 'Ошибка регистрации')
            return redirect('/register')
    else:
        form = CreateUserForm
    return render(request, 'register.html', {'form': form})


def login_user(request):
    """вход в учетную запись кандидата"""
    if request.method == 'POST':
        user = LoginForm(request.POST)
        user.get_context()
        username = user.cleaned_data.get('username')
        user = User.objects.get(username=username)
        if user:
            login(request, user)
            return redirect('/main')
        else:
            message = 'Данный пользователь не обнаружен. Проверьте правильность заполнения формы'
            return HttpResponse(message)
    else:
        form = LoginForm
        return render(request, 'auth.html', {'form': form})


class Logout(LogoutView):
    """выход из учетной записи кандидата"""
    next_page = '/main'
