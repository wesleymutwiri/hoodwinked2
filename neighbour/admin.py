from django.contrib import admin
from . import models

# Register your models here.


class neighbourMember(admin.TabularInline):
    model = models.HoodMember


admin.site.register(models.Neighbourhood)