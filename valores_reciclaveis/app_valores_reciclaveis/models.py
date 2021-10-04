from django.db import models
from django.db.models.aggregates import Avg, Max, Min

class Prestacao (models.Model):
    id_prestacao = models.BigIntegerField(blank=False)
    categoria = models.TextField(max_length=20, blank=False)  
    qte_mat_comercializado = models.DecimalField(decimal_places=2, blank=False)
    valor = models.DecimalField(decimal_places=2, blank=False)
    zona = models.TextField(max_length=10, blank=False)

class Visao_geral (models.Model):
    valor_minimo = Prestacao.objects.all().aggregate(Min('valor'))  # terá que mudar "all"
    valor_maximo = Prestacao.objects.get(filter=Prestacao.categoria).aggregate(Max('valor'))  # possibilidade
    valor_medio = Prestacao.objects.all().aggregate(Avg('valor'))
    categoria = Prestacao.categoria
    zona = Prestacao.zona
