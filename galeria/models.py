from django.db import models

from datetime import datetime

from django.contrib.auth.models import User

class Fotografia(models.Model):

    opcoes_categoria = [
        ("NEBULOSA", "Nebulosa"),
        ("GALÁXIAS", "Galáxias"),
        ("ESTRELAS", "Estrelas"),
        ("PLANETAS", "Planetas")
    ]
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=opcoes_categoria, default="")
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d",blank=True)
    publicada = models.BooleanField(default=False)
    data_foto=  models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Space photos"

