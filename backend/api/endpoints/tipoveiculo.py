from slth import endpoints
from ..models import *

class TiposVeiculo(endpoints.ListEndpoint[TipoVeiculo]):

    def get(self):
        return super().get().actions('tipoveiculo.cadastrar', 'tipoveiculo.editar')


class Cadastrar(endpoints.AddEndpoint[TipoVeiculo]):
    class Meta:
        verbose_name = 'Cadastrar TipoVeiculo'

    def get(self):
        return (
            super().get()
        )
    
class Editar(endpoints.EditEndpoint[TipoVeiculo]):
    class Meta:
        verbose_name = 'Editar TipoVeiculo'

    def get(self):
        return (
            super().get()
        )
