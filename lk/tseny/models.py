from django.db import models
from katalogi.models import Nomenklatura

# Create your models here.
class Tseny(models.Model):
    nomenklatura = models.ForeignKey(Nomenklatura, on_delete=models.PROTECT, verbose_name="Номенклатура", related_name="products")
    tsena = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена", blank=True, default=0)

    def __str__(self):
        return f'{self.nomenklatura} - {self.tsena}'
    
    class Meta:
        verbose_name = "Прайс"
        verbose_name_plural = "Прайс"
        