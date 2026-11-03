from django import forms

from . import models


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = ["nome"]

class TagForm(forms.ModelForm):
    class Meta:
        model = models.Tag
        fields = ("nome",)

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = models.Noticia
        fields = ["titulo", "texto", "categoria", "tags"]
