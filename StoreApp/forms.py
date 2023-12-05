from django import forms 

class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    telefone = forms.CharField()
    assunto = forms.CharField()
    mensagm = forms.CharField(widget=forms.Textarea)
