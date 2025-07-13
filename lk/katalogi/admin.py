from django.contrib import admin

from .models import Nomenklatura, GruppaNomenklatury, Kartinki

# Register your models here.
admin.site.register(Nomenklatura)
admin.site.register(GruppaNomenklatury)
admin.site.register(Kartinki)
