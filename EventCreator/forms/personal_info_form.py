from django import forms


class PersonalInfoForm(forms.Form):
    p_first_name = forms.CharField(label="Имя", max_length=100)
    p_last_name = forms.CharField(label="Фамилия", max_length=100)
    p_phone = forms.CharField(label="Номер телефона", max_length=100)
    p_email = forms.EmailField(label="E-mail", max_length=100)
    event_time = forms.DateField(input_formats=['%Y-%m-%d'])
