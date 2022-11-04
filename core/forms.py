from django import forms
from . import models

class CartaoForm(forms.ModelForm):
    class Meta:
        model = models.Cartao
        fields = ('nome', 'banco', 'numero', 'fechamento', 'vencimento')
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira o nome do cartão'
                }
            ),
            'banco': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira o banco do cartão'
                }
            ),
            'numero': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira o número do cartão'
                }
            ),
            'fechamento': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira o dia de fechamento'
                }
            ),
            'vencimento': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira o dia de vencimento'
                }
            ),
        }