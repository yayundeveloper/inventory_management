from django.contrib import admin
from .models import *

@admin.register(Pen, Notebook, Pencilcase)
class ViewAdmin(admin.ModelAdmin):
    pass
