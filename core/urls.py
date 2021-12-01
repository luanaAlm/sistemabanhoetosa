from django.urls import path
from .views import index, cadastro, cadastro_novo
urlpatterns = [
    path("", index, name="index"),
    path("cadastro", cadastro, name="cadastro"),
    path('cadastro_novo/', cadastro_novo, name='cadastro_novo'),
]
