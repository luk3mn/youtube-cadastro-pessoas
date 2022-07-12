from django import forms # para auxiliar na criação do usuário que interage com a model
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    # exibe o campo 'Data Nascimento' no formato de 'Date'
    data_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type":"date"}
        )
    )

    class Meta:
        model = Pessoa # para saber com qual model ele precisa fazer referencia
        fields = ['nome_completo', 'data_nascimento', 'ativa']