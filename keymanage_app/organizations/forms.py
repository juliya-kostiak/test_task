from .models import Organization, Keys
from django.forms import ModelForm, TextInput, DateInput, CheckboxInput


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = ["name"]
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название',
            }),
        }


class KeysForm(ModelForm):
    class Meta:
        org = Organization.objects.all()
        model = Keys
        fields = ["key", "start_date", "end_date", "id_org", "block"]
        widgets = {
            'key': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ключ',
            }),
            'start_date': DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'end_date': DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'id_org': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите организацию-владельца',
            }),
            'block': TextInput(attrs={
                'type': 'checkbox',
            }),
        }


