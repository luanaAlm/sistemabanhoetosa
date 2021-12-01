from django.contrib import admin
from .models import Pessoa, Animal, BanhoeTosa, Login, Cadastro

# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Animal)
admin.site.register(BanhoeTosa)
admin.site.register(Login)
admin.site.register(Cadastro)
