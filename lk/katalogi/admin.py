from django.contrib import admin

from .models import Nomenklatura, GruppaNomenklatury

# Register your models here.
admin.site.register(Nomenklatura)
admin.site.register(GruppaNomenklatury)
