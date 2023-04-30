from .models import Homework, Feedback
from django import forms
from django.forms import ModelForm, TextInput, Textarea, Select, ClearableFileInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    # Форма авторизации пользователей
    username = forms.CharField(label='Username', max_length=10, widget=forms.TextInput(attrs={'class': 'authorization__form-input'}))
    password = forms.CharField(label='Password', max_length=128, widget=forms.PasswordInput(attrs={'class': 'authorization__form-input'}))


class UserRegisterForm(UserCreationForm):
    # Форма регистрации пользователей
    username = forms.CharField(label='Username', max_length=10, widget=forms.TextInput(attrs={'class': 'authorization__form-input'}))
    password1 = forms.CharField(label='Password', max_length=128, widget=forms.PasswordInput(attrs={'class': 'authorization__form-input'}))
    password2 = forms.CharField(label='Confirm password', max_length=128, widget=forms.PasswordInput(attrs={'class': 'authorization__form-input'}))
    email = forms.EmailField(label='Email', max_length=320, widget=forms.EmailInput(attrs={'class': 'authorization__form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class FeedbackForm(ModelForm):
    # Форма обратной связи
    class Meta:
        model = Feedback
        fields = ['feedback_name', 'feedback_email', 'feedback_message']

        widgets = {
            'feedback_name': TextInput(attrs={
                'class': 'block3__form-input',
                'id': 'feedback_name',
                'placeholder': 'Ваше имя'
            }),
            'feedback_email': TextInput(attrs={
                'class': 'block3__form-input',
                'id': 'feedback_email',
                'placeholder': 'Ваш E-mail'
            }),
            'feedback_message': Textarea(attrs={
                'class': 'block3__form-textarea',
                'id': 'feedback_message',
                'placeholder': 'Ваш вопрос',
                'cols': '30',
                'rows': '1',
            }),
        }


class HomeworkForm(ModelForm):
    # Форма прикрепления домашних заданий
    class Meta:
        model = Homework
        fields = ['homework_course', 'homework_lesson', 'homework_file']

        widgets = {
            'homework_course': Select(attrs={
                'class': 'form-select',
                'id': 'homework_course',
            }),
            'homework_lesson': Select(attrs={
                'class': 'form-select',
                'id': 'homework_lesson',
            }),
            'homework_file': ClearableFileInput(attrs={
                'class': 'file_input',
                'id': 'homework_file',
            }),
        }        