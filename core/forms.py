from django import forms
from django.core.mail.message import EmailMessage
from django.forms import ModelForm

from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=16, min_length=4, required=True)
    email = forms.EmailField(label='E-mail', max_length=26)
    assunto = forms.CharField(label='assunto', max_length=100)
    mensagem = forms.CharField(label='mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='E-mail enviado pelo sistema django2',
            body= conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br',],
            headers={'Reply-To': email}
        )
        mail.send()

    def save(self):
        pass #criado hoje , conectado com a views form.save() ,obs se der ruim delete essa linha
                #e seja feliz , pos nem tudo e pra ficar mesmo !


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']
