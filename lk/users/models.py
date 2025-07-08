import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


# переопределяем модель пользователя
class CustomUser(AbstractUser):
    COMPANY = 'COMP'
    PRIVATE_PERSON = 'PRIV'
    COMPANY_PRIVATE = [
        (COMPANY, 'Компания'),
        (PRIVATE_PERSON, 'Частное лицо')
    ]
    # в Часть 2. Настройка модели User он переопределил id, чтобы он был не числовой, а длинная ссылка, как в 1С
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(verbose_name='Наименование полное', max_length=250, unique=True, null=True, blank = True)
    status = models.CharField(verbose_name='Юр/физлицо', max_length=250, choices= COMPANY_PRIVATE, default=COMPANY)

