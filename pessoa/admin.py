from django.contrib import admin
from .models import Pessoa, Contato

# método customuzado
@admin.action(description='Ativar todas as Pessoas')
def ativar_todos(modeladmin, request, queryset):
    queryset.update(ativo=True)

@admin.action(description='Desativar todas as Pessoas')
def desativar_todos(modeladmin, request, queryset):
    queryset.update(ativo=False)

# personalizando o django admin
class PessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'data_nascimento',
        'ativa'
    ]
    list_filter = [ # aba de filtro
        'ativa',
        'data_nascimento'
    ]
    search_fields = [ # campo de busca
        'nome_completo'
    ]   
    actions = [
        ativar_todos,
        desativar_todos    
    ]

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Contato)
