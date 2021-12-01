from django.db import models
from cpf_field.models import CPFField
from django.contrib.auth.models import User

# Create your models here.


class Pessoa (models.Model):
    ID_Pessoa = models.AutoField(primary_key=True, null=False)
    nome = models.CharField(max_length=30, null=False)
    sobrenome = models.CharField(
        max_length=100, null=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    numero_cpf = CPFField('CPF', max_length=14, null=False,
                          unique=True)

    def __str__(self):
        return self.nome


class BanhoeTosa (models.Model):
    SERVIÇOS_CHOICES = (
        ("Banho", "Banho"),
        ("Banho e Tosa Higienica", "Banho e Tosa Higienica"),
        ("Bannho e Tosa", "Bannho e Tosa"),
    )
    ID_BanhoeTosa = models.AutoField(primary_key=True, null=False)
    servicos = models.CharField(max_length=100, choices=SERVIÇOS_CHOICES)

    def __str__(self):
        return self.BanhoeTosa


class Animal(models.Model):
    RAÇA_ANIMAL_CHOICES = (
        ("Pastor Alemao", "Pastor Alemao"),
        ("Fila Brasileiro", "Fila Brasileiro"),
        ("Pincher", "Pincher"),
    )
    ANIMAL_SEXO_CHOICES = [
        ("MACHO", "MACHO"),
        ("FEMEA", "FEMEA"),
    ]
    nome_animal = models.CharField(max_length=30, null=False)
    Raca_Animal = models.CharField(max_length=100, choices=RAÇA_ANIMAL_CHOICES)
    sexo_Animal = models.CharField(max_length=100, choices=ANIMAL_SEXO_CHOICES)

# herança


class Cadastro(Pessoa, Animal, BanhoeTosa):
    ID_Cadastro = models.AutoField(primary_key=True, null=False)


class Login (models.Model):
    ID_longin = models.AutoField(primary_key=True, null=False)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.usuario
