from django.urls import path, re_path
from .views import home, \
    list_dados, list_filiacoes, list_enderecos, \
    list_documentos, list_contatos, list_militares, \
    list_observacoes, \
    read_pessoa, read_endereco, read_contato, \
    read_documento, read_filiacao, read_militar, \
    read_observacao, \
    create_pessoa, create_documento, create_contato, \
    create_endereco, create_filiacao, create_militar, \
    create_observacao, \
    update_pessoa, update_documento, update_contato, \
    update_endereco, update_filiacao, update_militar, \
    update_observacao, update_observacao_militares, update_observacao_fatos, \
    delete_pessoa, delete_documento, delete_contato, \
    delete_endereco, delete_filiacao, delete_militar, \
    delete_observacao, \
    list_update_pessoa, \
    Pdf

urlpatterns = [
    path('', home, name='core_home'),
    #LIST
    path('pessoa_dados/', list_dados, name='core_list_dados'),
    path('pessoa_endereco/', list_enderecos, name='core_list_enderecos'),
    path('pessoa_documento/', list_documentos, name='core_list_documentos'),
    path('pessoa_filiacao/', list_filiacoes, name='core_list_filiacoes'),
    path('pessoa_contato/', list_contatos, name='core_list_contatos'),
    path('pessoa_militar/', list_militares, name='core_list_militares'),
    path('observacoes/', list_observacoes, name='core_list_observacoes'),
    #READ
    path('pessoa_ler/', read_pessoa, name='core_read_pessoa'),
    path('documento_ler/', read_documento, name='core_read_documento'),
    path('filiacao_ler/', read_filiacao, name='core_read_filiacao'),
    path('endereco_ler/', read_endereco, name='core_read_endereco'),
    path('contato_ler/', read_contato, name='core_read_contato'),
    path('militar_ler/', read_militar, name='core_read_militar'),
    path('observacao_ler/', read_observacao, name='core_read_observacao'),
    #CREATE
    path('pessoa_novo/', create_pessoa, name='core_create_pessoa'),
    path('documento_novo/', create_documento, name='core_create_documento'),
    path('filiacao_novo/', create_filiacao, name='core_create_filiacao'),
    path('endereco_novo/', create_endereco, name='core_create_endereco'),
    path('contato_novo/', create_contato, name='core_create_contato'),
    path('militar_novo/', create_militar, name='core_create_militar'),
    path('observacao_novo/', create_observacao, name='core_create_observacao'),
    #UPDATE
    path('atualize/', list_update_pessoa,
         name='core_list_update_pessoa'),
    path('obs_militares/', update_observacao_militares,
         name='core_update_observacao_militares'),
    re_path(r'obs_fatos/(?P<id>\d+)/$', update_observacao_fatos,
            name='core_update_observacao_fatos'),
    re_path(r'^pessoa_update/(?P<id>\d+)/$', update_pessoa,
            name='core_update_pessoa'),
    re_path(r'^documento_update/(?P<id>\d+)/$', update_documento,
            name='core_update_documento'),
    re_path(r'^filiacao_update/(?P<id>\d+)/$', update_filiacao,
            name='core_update_filiacao'),
    re_path(r'^endereco_update/(?P<id>\d+)/$', update_endereco,
            name='core_update_endereco'),
    re_path(r'^contato_update/(?P<id>\d+)/$', update_contato,
            name='core_update_contato'),
    re_path(r'^militar_update/(?P<id>\d+)/$', update_militar,
            name='core_update_militar'),
    re_path(r'^observacao_update/(?P<id>\d+)/$', update_observacao,
            name='core_update_observacao'),
    #DELETE
    re_path(r'^pessoa_delete/(?P<id>\d+)/$', delete_pessoa,
            name='core_delete_pessoa'),
    re_path(r'^documento_delete/(?P<id>\d+)/$', delete_documento,
            name='core_delete_documento'),
    re_path(r'^filiacao_delete/(?P<id>\d+)/$', delete_filiacao,
            name='core_delete_filiacao'),
    re_path(r'^endereco_delete/(?P<id>\d+)/$', delete_endereco,
            name='core_delete_endereco'),
    re_path(r'^contato_delete/(?P<id>\d+)/$', delete_contato,
            name='core_delete_contato'),
    re_path(r'^militar_delete/(?P<id>\d+)/$', delete_militar,
            name='core_delete_militar'),
    re_path(r'^observacao_delete/(?P<id>\d+)/$', delete_observacao,
            name='core_delete_observacao'),
    re_path(r'^fatd/(?P<id>\d+)/$', Pdf.as_view(), name='fatd_pdf'),
]

