from django.contrib import admin
from .models import PostoGrad, \
    Pessoa, \
    Filiacao, \
    Contato, \
    Documento, \
    Endereco, \
    Militar, \
    Subunidade, \
    Secao, \
    Qualificacao, \
    Observacao


class FiliacaoAdmin(admin.ModelAdmin):
    list_display = ('pessoa',
                    'nome_pai',
                    'nome_mae')


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'telefone', 'celular', 'email')


class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'rg', 'cpf', 'titulo_eleitor', 'cnh', 'cat_cnh')
    list_filter = ('cat_cnh', )


admin.site.register(PostoGrad)
admin.site.register(Subunidade)
admin.site.register(Secao)
admin.site.register(Qualificacao)
admin.site.register(Pessoa)
admin.site.register(Filiacao, FiliacaoAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Militar)
admin.site.register(Endereco)
admin.site.register(Observacao)

