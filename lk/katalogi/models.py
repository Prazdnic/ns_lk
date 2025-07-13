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


def put_k_papke_kartinok(instance, filename):
    return 'nomenklatura_kartinki/{}/{}'.format(instance.nomenklatura.id, filename)

class Kartinki(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable=False)
    nomenklatura = models.ForeignKey(Nomenklatura, on_delete=models.PROTECT, null=True, blank = True, verbose_name="Номенклатура", related_name='product_images')
    kartinka = models.ImageField(verbose_name='Картинка', upload_to=put_k_papke_kartinok, default=None)

    def __str__(self):
        return '{} - {}'.format(self.nomenklatura, self.kartinka)
    
    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинка'