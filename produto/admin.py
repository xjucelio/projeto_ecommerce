from django.contrib import admin # type: ignore

from produto.models import Produto, Variacao

class VariacaoInLine(admin.TabularInline):
    model = Variacao
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_curta', 'get_preco_formatado', 'get_preco_promocional_formatado']
    inlines = [VariacaoInLine]


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)
