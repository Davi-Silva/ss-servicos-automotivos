from django import forms
from.models import Quote

class QuoteForm(forms.ModelForm):
    fullname = forms.CharField(
        label="",
        widget=forms.TextInput(
                attrs={
                    "class": "form-control", 
                    "placeholder": "Nome"
                }
            )
        )

    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(
                attrs={
                    "class": "form-control", 
                    "placeholder": "Email"
                }
            )
        )


    phone  = forms.CharField(
        max_length=30,
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Telefone",
                "type": "number" 
                }
            )
        )

    vehicle_model = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control", 
                "placeholder": "Modelo do Veículo"
            }
        )
    )


    vehicle_location = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control", 
                "placeholder": "Localização do Veículo"
            }
        )
    )


    message = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "class": "form-control", 
                "placeholder": "Menssagem"
            }
        )
    )


    class Meta:
        model = Quote
        fields = [
            'fullname',
            'email',
            'phone',
            'vehicle_model',
            'vehicle_location',
            'message'
        ]