from django import forms
from.models import Contact

class ContactForm(forms.Form):
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
        max_length=13,
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Telefone" 
                }
            )
        )

    subject = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control", 
                "placeholder": "Assunto"
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
        model = Contact
        fields = [
            'name',
            'email',
            'phone',
            'subject',
            'message'
        ]