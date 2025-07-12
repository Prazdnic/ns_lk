import uuid
from django.db import models

# Create your models here.
class GruppaNomenklatury(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # переопределяем id, чтобы был такого же формата, как в 1С
    naimenovanie = models.CharField(verbose_name="Наименование", max_length=250)
    roditel = models.ForeignKey('self', on_delete=models.CASCADE, null = True, blank = True, verbose_name="Родитель", related_name='group')

    def __str__(self):
        return f'{self.naimenovanie} - {self.roditel}'
    
    class Meta:
        verbose_name  = "Группа номенклатуры"
        verbose_name_plural  = "Группа номенклатуры"


class Nomenklatura(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    polnoe_naimenovanie = models.CharField(verbose_name="Наименование", max_length=250)
    roditel = models.ForeignKey(GruppaNomenklatury, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Родитель", related_name='products')

    def __str__(self):
        return self.polnoe_naimenovanie
    
    class Meta:
        verbose_name  = "Номенклатура"
        verbose_name_plural  = "Номенклатура"