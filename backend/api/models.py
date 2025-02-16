from slth.db import models, role, meta
from slth.components import Image


class TipoVeiculo(models.Model):
    nome = models.CharField(verbose_name='Tipo de Veículo')

    class Meta:
        verbose_name = 'Tipo de Veículo'
        verbose_name_plural = 'Tipos de Veículo'

    def __str__(self):
        return self.nome


class Cor(models.Model):
    nome = models.CharField(verbose_name='Nome')

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cor'

    def __str__(self):
        return self.nome


class Marca(models.Model):
    nome = models.CharField(verbose_name='Nome')

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.nome


class Modelo(models.Model):
    nome = models.CharField(verbose_name='Nome')
    marca = models.ForeignKey(Marca, verbose_name='Marca', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def __str__(self):
        return '{}/{}'.format(self.nome, self.marca)


class Documento(models.Model):
    foto = models.ImageField(verbose_name='Foto', upload_to='images')
    verso = models.ImageField(verbose_name='Verso', upload_to='images', null=True, blank=True)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    def __str__(self):
        return f'Documento {self.id}'


class PessoaQuerySet(models.QuerySet):
    def all(self):
        return self


class Pessoa(models.Model):
    foto = models.ImageField(verbose_name='Foto de Perfil', upload_to='images', null=True, blank=True)
    cpf_cnpj = models.CharField(verbose_name='CPF/CNPJ')
    nome = models.CharField(verbose_name='Nome')
    documento = models.OneToOneField(Documento, verbose_name='Documento', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    objects = PessoaQuerySet()

    def __str__(self):
        return f'Pessoa {self.id}'
    
    def get_foto(self):
        return Image(self.foto)
    
    def get_documento(self):
        return Image(self.documento.foto) if self.documento_id else None


class Local(models.Model):
    nome = models.CharField(verbose_name='Nome')
    latitude = models.CharField(verbose_name='Latitulde')
    longitude = models.CharField(verbose_name='Longitude')

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locais'

    def __str__(self):
        return self.nome


class EstampadorQuerySet(models.QuerySet):
    def all(self):
        return self


class Estampador(models.Model):
    cnpj = models.CharField(verbose_name='CNPJ')
    nome = models.CharField(verbose_name='Nome')
    operadores = models.ManyToManyField(Pessoa, verbose_name='Operadores')
    locais_instalacao = models.OneToManyField(Local, verbose_name='Locais de Instalação')
    

    class Meta:
        verbose_name = 'Estampador'
        verbose_name_plural = 'Estampadores'

    objects = EstampadorQuerySet()

    def __str__(self):
        return self.nome



class Emplacamento(models.Model):

    def formfactory(self):
        return (
            super().formfactory()
            .fieldset('Dados Gerais', ('tipo_veiculo', ('data_inicio', 'data_conclusao')))
            .fieldset('Dados do Operador', (('estampador', 'operador'), 'foto_operador'))
            .fieldset('Geolocalização', ('latitude', 'longitude',))
            .fieldset('Dados do Veículo', (('numero_placa', 'cor', 'modelo'), 'zero_kilometro', 'proprietario:pessoa.cadastrar',))
            .fieldset('Chassi', ('numero_chassi', 'foto_chassi',))
            .fieldset('Fotos do Veículo', ('foto_dianteira', 'foto_traseira',))
            .fieldset('Fotos da Placa', ('foto_placa_dianteira', 'foto_placa_traseira', 'foto_segunda_placa_traseira'))
            .fieldset('Fotos do Descarte', ('foto_descarte_placa_dianteira', 'foto_descarte_placa_traseira', 'foto_descarte_segunda_placa_traseira'))
            .fieldset('Procuração', ('representante', 'foto_procuracao',))
        )
    
    tipo_veiculo = models.ForeignKey(TipoVeiculo, verbose_name='Tipo de Veículo', on_delete=models.CASCADE, null=True)
    data_inicio = models.DateTimeField(verbose_name='Data/Hora de Início', auto_created=True)
    data_conclusao = models.DateTimeField(verbose_name='Data/Hora de Conclusão', null=True)

    estampador = models.ForeignKey(Estampador, verbose_name='Estampador', on_delete=models.CASCADE)
    operador = models.ForeignKey(Pessoa, verbose_name='Operador', on_delete=models.CASCADE)
    foto_operador = models.ImageField(verbose_name='Foto do Operador', upload_to='images', null=True, blank=True)

    latitude = models.CharField(verbose_name='Latitulde', null=True)
    longitude = models.CharField(verbose_name='Longitude', null=True)

    numero_placa = models.CharField(verbose_name='Número do Placa')
    proprietario = models.ForeignKey(Pessoa, verbose_name='Proprietário', on_delete=models.CASCADE, related_name='p2')

    zero_kilometro = models.BooleanField(verbose_name="Zero Kilômetro", blank=True)
    cor = models.ForeignKey(Cor, verbose_name='Cor', on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, verbose_name='Modelo', on_delete=models.CASCADE)

    numero_chassi = models.CharField(verbose_name='Número do Chassi')
    foto_chassi = models.ImageField(verbose_name='Foto do Chassi', upload_to='images', null=True, blank=True)
    
    foto_dianteira = models.ImageField(verbose_name='Foto Dianteira', upload_to='images', null=True, blank=True)
    foto_traseira = models.ImageField(verbose_name='Foto Traseira', upload_to='images', null=True, blank=True)
    
    foto_placa_dianteira = models.ImageField(verbose_name='Foto da Placa Dianteira', upload_to='images', null=True, blank=True)
    foto_placa_traseira = models.ImageField(verbose_name='Foto da Placa Traseira', upload_to='images', null=True, blank=True)
    foto_segunda_placa_traseira = models.ImageField(verbose_name='Foto da Segunda Placa Traseira', upload_to='images', null=True, blank=True)

    foto_descarte_placa_dianteira = models.ImageField(verbose_name='Foto do Descarte da Placa Dianteira', upload_to='images', null=True, blank=True)
    foto_descarte_placa_traseira = models.ImageField(verbose_name='Foto do Descarte da Placa Traseira', upload_to='images', null=True, blank=True)
    foto_descarte_segunda_placa_traseira = models.ImageField(verbose_name='Foto do Descarte da Segunda Placa Traseira', upload_to='images', null=True, blank=True)

    representante = models.ForeignKey(Pessoa, verbose_name='Representante', on_delete=models.CASCADE, null=True, blank=True, related_name='p3')
    foto_procuracao = models.ImageField(verbose_name='Foto da Procuração', upload_to='images', null=True, blank=True)

    class Meta:
        verbose_name = 'Emplacamento'
        verbose_name_plural = 'Emplacamentos'

    def __str__(self):
        return 'Emplacamento {}'.format(self.id)
