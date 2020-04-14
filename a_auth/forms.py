from django import forms

class SigninForm(forms.Form):
    username = forms.CharField(label = 'Имя пользователя', max_length = 255)
    password = forms.CharField(label = 'Пароль', max_length = 32, widget = forms.PasswordInput)

    username.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
