from django import forms
from .models import Candidate, Skill, Language, Hobby


class LoginForm(forms.Form):
    """Форма аутентификации"""
    username = forms.CharField(max_length=100, label='Имя пользователя')
    password1 = forms.CharField(max_length=100, label='Пароль')

    class Meta:
        fields = ['username', 'password1']


class CreateUserForm(forms.Form):
    """Форма регистрации"""
    username = forms.CharField(max_length=100, label='Имя ')
    surname = forms.CharField(max_length=100, label='Фамилия ')
    lastname = forms.CharField(max_length=100, label='Отчество ')
    password1 = forms.CharField(max_length=100, label='Пароль')
    skill = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), label='Навыки')
    language = forms.ModelMultipleChoiceField(queryset=Language.objects.all(), label='Языки')


class ChoiceHobbyform(forms.Form):
    """Форма выбора хобби"""
    hobby = forms.ModelMultipleChoiceField(queryset=Hobby.objects.all(), label='Выбрать Хобби', required=False)


class AddHobbyForm(forms.Form):
    """Форма добавления хобби"""
    hobby2 = forms.CharField(max_length=50, min_length=3, required=False, label='Добавить хобби')
