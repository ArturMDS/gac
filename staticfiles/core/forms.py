from django.forms import ModelForm
from .models import Pessoa, \
    Filiacao, \
    Contato, \
    Documento, \
    Endereco, \
    Militar, \
    Observacao


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class FiliacaoForm(ModelForm):
    class Meta:
        model = Filiacao
        fields = '__all__'


class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'


class DocumentoForm(ModelForm):
    class Meta:
        model = Documento
        fields = '__all__'


class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'


class MilitarForm(ModelForm):
    class Meta:
        model = Militar
        fields = '__all__'


class ObservacaoForm(ModelForm):
    class Meta:
        model = Observacao
        fields = '__all__'

