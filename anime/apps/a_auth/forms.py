from django import forms

class SigninForm(forms.Form):
    username = forms.CharField(label = 'Имя пользователя', max_length = 255)
    password = forms.CharField(label = 'Пароль', max_length = 32, widget = forms.PasswordInput)

    username.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})

class SignupForm(forms.Form):
    username = forms.CharField(label = 'Имя пользователя', max_length = 255)
    password = forms.CharField(label = 'Пароль', max_length = 32, widget = forms.PasswordInput)
    re_password = forms.CharField(label = 'Пароль', max_length = 32, widget = forms.PasswordInput)
    first_name = forms.CharField(label = 'Имя', max_length = 255)
    last_name = forms.CharField(label = 'Фамилия', max_length = 255)

    username.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    re_password.widget.attrs.update({'class': 'form-control'})
    first_name.widget.attrs.update({'class': 'form-control'})
    last_name.widget.attrs.update({'class': 'form-control'})
