from django.contrib import admin
from .models import Pessoa

# Register your models here.

admin.site.site_tetle = 'Administrador de grupos'
admin.site.index_title = 'Administrador de grupos'
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone", "cidade", "estado", "app", "grupo")
    prepopulated_fields = {
        "slug": ("nome",),
        }
    search_fields = ('nome', 'cidade', 'app', 'grupo',)
