import io

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from .models import Pessoa, \
    Contato, \
    Documento, \
    Endereco, \
    Filiacao, \
    Militar, \
    Observacao
from .forms import PessoaForm, \
    ContatoForm, \
    DocumentoForm, \
    EnderecoForm, \
    FiliacaoForm, \
    MilitarForm, \
    ObservacaoForm


def home(request):
    return render(request, 'core/index.html')


#LIST
@login_required()
def list_dados(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/list_dados.html', {'pessoas': pessoas})


@login_required()
def list_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'core/list_contatos.html', {'contatos': contatos})


@login_required()
def list_documentos(request):
    documentos = Documento.objects.all()
    return render(request, 'core/list_documentos.html', {'documentos': documentos})


@login_required()
def list_enderecos(request):
    enderecos = Endereco.objects.all()
    return render(request, 'core/list_endereco.html', {'enderecos': enderecos})


@login_required()
def list_filiacoes(request):
    filiacoes = Filiacao.objects.all()
    return render(request, 'core/list_filiacao.html', {'filiacoes': filiacoes})


@login_required()
def list_militares(request):
    militares = Militar.objects.all()
    return render(request, 'core/list_militar.html', {'militares': militares})


@login_required()
def list_observacoes(request):
    militares = Militar.objects.all()
    observacoes = Observacao.objects.all()
    data = {'militares': militares, 'observacoes': observacoes}
    return render(request, 'core/list_observacao.html', data)


#READ
@login_required()
def read_pessoa(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/read_pessoa.html', data)


@login_required()
def read_endereco(request):
    enderecos = Endereco.objects.all()
    form = EnderecoForm()
    data = {'enderecos': enderecos, 'form': form}
    return render(request, 'core/read_endereco.html', data)


@login_required()
def read_contato(request):
    contatos = Contato.objects.all()
    form = ContatoForm()
    data = {'contatos': contatos, 'form': form}
    return render(request, 'core/read_contato.html', data)


@login_required()
def read_documento(request):
    documentos = Documento.objects.all()
    form = DocumentoForm()
    data = {'documento(s': documentos, 'form': form}
    return render(request, 'core/read_documento.html', data)


@login_required()
def read_filiacao(request):
    filiacoes = Filiacao.objects.all()
    form = FiliacaoForm()
    data = {'filiacoes': filiacoes, 'form': form}
    return render(request, 'core/read_filiacao.html', data)


@login_required()
def read_militar(request):
    militares = Militar.objects.all()
    form = MilitarForm()
    data = {'militares': militares, 'form': form}
    return render(request, 'core/read_militar.html', data)


@login_required()
def read_observacao(request):
    observacoes = Observacao.objects.all()
    form = ObservacaoForm()
    data = {'observacoes': observacoes, 'form': form}
    return render(request, 'core/read_observacao.html', data)


#CREATE
@login_required()
def create_pessoa(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_read_endereco')
    else:
        return redirect('core_read_pessoa')


@login_required()
def create_documento(request):
    form = DocumentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_read_filiacao')
    else:
        return redirect('core_read_documento')


@login_required()
def create_contato(request):
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_read_documento')
    else:
        return redirect('core_read_contato')


@login_required()
def create_filiacao(request):
    form = FiliacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_read_militar')
    else:
        return redirect('core_read_filiacao')


@login_required()
def create_endereco(request):
    form = EnderecoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_read_contato')
    else:
        return redirect('core_read_endereco')


@login_required()
def create_militar(request):
    form = MilitarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_read_pessoa')
    else:
        return redirect('core_read_militar')


@login_required()
def create_observacao(request):
    form = ObservacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_read_observacao')


#UPDATE
@login_required()
def list_update_pessoa(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/list_update_pessoa.html', {'pessoas': pessoas})


@login_required()
def update_observacao_militares(request):
    militares = Militar.objects.all()
    return render(request, 'core/update_observacao_militares.html', {'militares': militares})


@login_required()
def update_observacao_fatos(request, id):
    militares = Militar.objects.all()
    militar = Militar.objects.get(id=id)
    observacoes = Observacao.objects.filter(militar_id=id)
    data = {'observacoes': observacoes, 'militares': militares, 'militar': militar}
    return render(request, 'core/update_observacao_fatos.html', data)


@login_required()
def update_pessoa(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    objetos = Pessoa.objects.all()
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['objetos'] = objetos
    data['pessoa'] = pessoa
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'core/update_pessoa.html', data)
    else:
        return render(request, 'core/update_pessoa.html', data)


@login_required()
def update_documento(request, id):
    data = {}
    objetos = Documento.objects.all()
    documento = Documento.objects.get(id=id)
    form = DocumentoForm(request.POST or None, instance=documento)
    data['objetos'] = objetos
    data['documento'] = documento
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'core/update_documento.html', data)
    else:
        return render(request, 'core/update_documento.html', data)


@login_required()
def update_endereco(request, id):
    data = {}
    objetos = Endereco.objects.all()
    endereco = Endereco.objects.get(id=id)
    form = EnderecoForm(request.POST or None, instance=endereco)
    data['objetos'] = objetos
    data['endereco'] = endereco
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'core/update_endereco.html', data)
    else:
        return render(request, 'core/update_endereco.html', data)


@login_required()
def update_contato(request, id):
    data = {}
    objetos = Contato.objects.all()
    contato = Contato.objects.get(id=id)
    form = ContatoForm(request.POST or None, instance=contato)
    data['objetos'] = objetos
    data['contato'] = contato
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'core/update_contato.html', data)
    else:
        return render(request, 'core/update_contato.html', data)


@login_required()
def update_filiacao(request, id):
    data = {}
    objetos = Filiacao.objects.all()
    filiacao = Filiacao.objects.get(id=id)
    form = FiliacaoForm(request.POST or None, instance=filiacao)
    data['objetos'] = objetos
    data['filiacao'] = filiacao
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'core/update_filiacao.html', data)
    else:
        return render(request, 'core/update_filiacao.html', data)


@login_required()
def update_militar(request, id):
    data = {}
    objetos = Militar.objects.all()
    militar = Militar.objects.get(id=id)
    form = MilitarForm(request.POST or None, instance=militar)
    data['objetos'] = objetos
    data['militar'] = militar
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'core/update_militar.html', data)
    else:
        return render(request, 'core/update_militar.html', data)


@login_required()
def update_observacao(request, id):
    data = {}
    militares = Militar.objects.all()
    observacao = Observacao.objects.get(id=id)
    observacoes = Observacao.objects.filter(militar_id=observacao.militar_id)
    form = ObservacaoForm(request.POST or None, instance=observacao)
    data['observacoes'] = observacoes
    data['observacao'] = observacao
    data['militares'] = militares
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'core/update_observacao.html', data)
    else:
        return render(request, 'core/update_observacao.html', data)


#DELETE
@login_required()
def delete_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_read_pessoa')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': pessoa})


@login_required()
def delete_endereco(request, id):
    endereco = Endereco.objects.get(id=id)
    if request.method == 'POST':
        endereco.delete()
        return redirect('core_read_endereco')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': endereco})


@login_required()
def delete_contato(request, id):
    contato = Contato.objects.get(id=id)
    if request.method == 'POST':
        contato.delete()
        return redirect('core_read_contato')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': contato})


@login_required()
def delete_documento(request, id):
    documento = Documento.objects.get(id=id)
    if request.method == 'POST':
        documento.delete()
        return redirect('core_read_documento')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': documento})


@login_required()
def delete_filiacao(request, id):
    filiacao = Filiacao.objects.get(id=id)
    if request.method == 'POST':
        filiacao.delete()
        return redirect('core_read_filiacao')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': filiacao})


@login_required()
def delete_militar(request, id):
    militar = Militar.objects.get(id=id)
    if request.method == 'POST':
        militar.delete()
        return redirect('core_read_militar')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': militar})


@login_required()
def delete_observacao(request, id):
    observacao = Observacao.objects.get(id=id)
    if request.method == 'POST':
        observacao.delete()
        return redirect('core_update_observacao_militares')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': observacao})


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error redering PDF", status=400)


class Pdf(View):

    def get(self, request, id):
        observacao = Observacao.objects.get(id=id)
        objeto = Militar.objects.get(pessoa=observacao.militar.pessoa)
        params = {
            'observacao': observacao,
            'objeto': objeto,
            'request': request,
        }
        return Render.render('core/fatd.html', params, f'{objeto.pessoa} nr{observacao.id}')
