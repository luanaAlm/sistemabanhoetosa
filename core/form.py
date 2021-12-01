from django.forms import ModelForm
from .models import Pessoa, Animal, BanhoeTosa, Cadastro


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'


class BanhoeTosaForm(ModelForm):
    class Meta:
        model = BanhoeTosa
        fields = '__all__'


class CadastroForm(ModelForm):
    class Meta:
        model = Cadastro
        fields = '__all__'
