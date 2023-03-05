from django.db import models


class PostoGrad(models.Model):
    rank = models.CharField(max_length=40)

    def __str__(self):
        return self.rank


class Subunidade(models.Model):
    nome = models.CharField(max_length=80)

    def __str__(self):
        return self.nome


class Secao(models.Model):
    nome = models.CharField(max_length=80)

    def __str__(self):
        return self.nome


class Qualificacao(models.Model):
    qm = models.CharField(max_length=80)

    def __str__(self):
        return self.qm


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=250)
    nome_guerra = models.CharField(max_length=80)
    data_nasc = models.DateField()
    posto_grad = models.ForeignKey(PostoGrad, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_guerra


class Filiacao(models.Model):
    nome_pai = models.CharField(max_length=250, null=True, blank=True)
    nome_mae = models.CharField(max_length=250)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome_guerra


class Contato(models.Model):
    telefone = models.CharField(max_length=20, null=True, blank=True)
    celular = models.CharField(max_length=20)
    email = models.EmailField(max_length=150, null=True, blank=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome_guerra


class Documento(models.Model):
    rg = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15)
    titulo_eleitor = models.CharField(max_length=50)
    cnh = models.CharField(max_length=20, null=True, blank=True)
    cat_cnh = models.CharField(max_length=1, null=True, blank=True)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome_guerra


class Endereco(models.Model):
    logadouro = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    bairro = models.CharField(max_length=80)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=80)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome_guerra


class Militar(models.Model):
    identidade = models.CharField(max_length=15)
    numero = models.CharField(max_length=8, blank=True, null=True)
    subunidade = models.ForeignKey(Subunidade, on_delete=models.PROTECT)
    secao = models.ForeignKey(Secao, on_delete=models.PROTECT)
    qualificacao = models.ForeignKey(Qualificacao, on_delete=models.PROTECT)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.PROTECT)

    def __str__(self):
        return self.pessoa.nome_guerra


class Observacao(models.Model):
    positiva = 'FO+'
    negativa = 'FO-'
    neutra = 'N'
    Observacao_choices = [
        (positiva, 'Positiva'),
        (negativa, 'Negativa'),
        (neutra, 'Neutra'),
    ]
    tipo = models.CharField(
        max_length=3,
        choices=Observacao_choices,
        default=neutra,
    )
    relato_fato = models.TextField(max_length=300)
    militar = models.ForeignKey(Militar, on_delete=models.PROTECT)

    def __str__(self):
        return self.militar.pessoa.nome_guerra

