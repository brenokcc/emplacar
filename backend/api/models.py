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
        verbose_name_plural = 'Cores'

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
            .fieldset('Dados Gerais', (('estampador', 'autorizacao'), ('data_inicio', 'data_conclusao')))
            .fieldset('Dados do Operador', ('operador', 'foto_operador'),)
            .fieldset('Geolocalização', (('latitude', 'longitude'),))
            .fieldset('Dados do Veículo', (('numero_placa','tipo_veiculo'), ('cor', 'modelo'), 'zero_kilometro', 'proprietario:pessoa.cadastrar',))
            .fieldset('Chassi', ('numero_chassi', 'foto_chassi',))
            .fieldset('Fotos do Veículo', ('foto_dianteira', 'foto_traseira',))
            .fieldset('Fotos da Placa', ('foto_placa_dianteira', 'foto_placa_traseira', 'foto_segunda_placa_traseira'))
            .fieldset('Descarte', ('foto_boletim_ocorrencia', 'foto_descarte_placa_dianteira', 'foto_descarte_placa_traseira', 'foto_descarte_segunda_placa_traseira'))
            .fieldset('Procuração', ('representante', 'foto_procuracao',))
        ) if self.pk else (
            super().formfactory()
            .fieldset('Dados Gerais', (('estampador', 'autorizacao'),))
            .fieldset('Dados do Veículo', (('numero_placa','tipo_veiculo'), ('cor', 'modelo'), 'zero_kilometro', 'proprietario:pessoa.cadastrar',))
            .fieldset('Chassi', ('numero_chassi',))
            .fieldset('Procuração', ('representante',))
        )
    autorizacao = models.CharField(verbose_name='Autorização', null=True)
    tipo_veiculo = models.ForeignKey(TipoVeiculo, verbose_name='Tipo de Veículo', on_delete=models.CASCADE, null=True)
    data_inicio = models.DateTimeField(verbose_name='Data/Hora de Início', null=True, blank=True)
    data_conclusao = models.DateTimeField(verbose_name='Data/Hora de Conclusão', null=True, blank=True)

    estampador = models.ForeignKey(Estampador, verbose_name='Estampador', on_delete=models.CASCADE)
    operador = models.ForeignKey(Pessoa, verbose_name='Operador', on_delete=models.CASCADE, blank=True)
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

    foto_boletim_ocorrencia = models.ImageField(verbose_name='Foto do Boletim de Ocorrência', upload_to='images', null=True, blank=True)
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
    
    def to_json(self, detalhar=False):
        return dict(
            id=self.id,
            autorizacao=self.autorizacao,
            tipo_veiculo=self.tipo_veiculo.nome,
            data_inicio=self.data_inicio.isoformat(),
            data_conclusao=self.data_conclusao.isoformat() if self.data_conclusao else None,
            estampador=dict(
                nome=self.estampador.nome,
                cnpj=self.estampador.cnpj,
                
                locais_instalacao=[
                    dict(
                        nome=local.nome,
                        latitude=local.latitude,
                        longitude=local.longitude
                    ) for local in self.estampador.locais_instalacao.all()
                ],
                operadores=[
                    dict(
                        nome=operador.nome,
                        cpf=operador.cpf_cnpj,
                        foto=operador.foto.url
                    ) for operador in self.estampador.operadores.all()
                ]
            ),
            geolocalizacao=dict(
                latitude=self.latitude,
                longitude=self.longitude,
            ),
            operador=dict(
                nome=self.operador.nome,
                cpf=self.operador.cpf_cnpj,
                foto=self.operador.foto.url
            ),
            veiculo=dict(
                zero_kilometro=self.zero_kilometro,
                cor=self.cor.nome,
                marca=self.modelo.marca.nome,
                modelo=self.modelo.nome,
                chassi=dict(
                    numero=self.numero_chassi,
                    foto=self.foto_chassi.url if self.foto_chassi else None
                ),
                fotos=dict(
                    dianteira=self.foto_dianteira.url if self.foto_dianteira else None,
                    traseira=self.foto_traseira.url if self.foto_traseira else None,
                ),
                placa=dict(
                    numero=self.numero_placa,
                    fotos=dict(
                        dianteira=self.foto_placa_dianteira.url if self.foto_placa_dianteira else None,
                        traseira=self.foto_placa_traseira.url if self.foto_placa_traseira else None,
                        segunda_traseira=self.foto_segunda_placa_traseira.url if self.foto_segunda_placa_traseira else None
                    )
                ),
                proprietario=dict(
                    nome=self.proprietario.nome,
                    cpf_cnpj=self.proprietario.cpf_cnpj,
                    foto=self.proprietario.foto.url if self.proprietario.foto else None,
                    documento=dict(
                        frente=self.proprietario.documento.foto.url,
                        verso=self.proprietario.documento.verso.url if self.proprietario.documento.verso else None
                    ) if self.proprietario.documento else None
                ),
                procuracao=dict(
                    foto=self.foto_procuracao.url if self.foto_procuracao else None,
                    representante=dict(
                        nome=self.representante.nome,
                        cpf=self.representante.cpf_cnpj,
                    ),
                ),
                descarte=dict(
                    boletim_ocorrencia=self.foto_boletim_ocorrencia.url if self.foto_boletim_ocorrencia else None,
                    fotos=dict(
                        placa_dianteira=self.foto_descarte_placa_dianteira.url if self.foto_descarte_placa_dianteira else None,
                        placa_traseira=self.foto_descarte_placa_traseira.url if self.foto_descarte_placa_traseira else None,
                        placa_segunda_traseira=self.foto_descarte_segunda_placa_traseira.url if self.foto_descarte_segunda_placa_traseira else None
                    )
                )
            )
        ) if detalhar else dict(
            id=self.id,
            autorizacao=self.autorizacao,
            tipo_veiculo=self.tipo_veiculo.nome,
            data_inicio=self.data_inicio.isoformat(),
            data_conclusao=self.data_conclusao.isoformat() if self.data_conclusao else None,
            estampador=dict(
                nome=self.estampador.nome,
                cnpj=self.estampador.cnpj,
            ),
            veiculo=dict(
                zero_kilometro=self.zero_kilometro,
                cor=self.cor.nome,
                marca=self.modelo.marca.nome,
                modelo=self.modelo.nome,
                proprietario=dict(
                    nome=self.proprietario.nome,
                    cpf_cnpj=self.proprietario.cpf_cnpj,
                )
            )
        )
