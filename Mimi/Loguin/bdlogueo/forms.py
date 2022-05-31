from django import forms

class altausuario(forms.Form):
    usuario=forms.CharField(max_length=40)
    contraseña=forms.CharField(max_length=40)
    oblea=forms.CharField(max_length=40)
    legajo=forms.CharField(max_length=7)
