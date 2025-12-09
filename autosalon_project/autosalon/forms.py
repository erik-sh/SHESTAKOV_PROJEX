from django import forms
from .models import TestDriveRequest

class TestDriveForm(forms.ModelForm):
    class Meta:
        model = TestDriveRequest
        fields = ['car', 'name', 'phone', 'email', 'preferred_date', 'message']
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'car': 'Автомобиль для тест-драйва',
            'name': 'Ваше имя',
            'phone': 'Номер телефона',
            'email': 'Email',
            'preferred_date': 'Желаемая дата',
            'message': 'Дополнительная информация',
        }