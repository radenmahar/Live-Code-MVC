from django.contrib import admin
from .models import DaftarBarang
# Register your models here.

class DaftarBarangDisplay(admin.ModelAdmin):
    list_display = ['picture', 'nama', 'harga']

admin.site.register(DaftarBarang, DaftarBarangDisplay)
