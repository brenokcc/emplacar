from slth import endpoints
from ..models import *

class Estampadores(endpoints.ListEndpoint[Estampador]):

    def get(self):
        return super().get().actions('estampador.cadastrar', 'estampador.editar')


class Cadastrar(endpoints.AddEndpoint[Estampador]):
    class Meta:
        verbose_name = 'Cadastrar Estampador'

    def get(self):
        return (
            super().get()
            .fieldset('Dados Gerais', (('cnpj', 'nome'), 'operadores:pessoa.cadastrar'))
            .fieldset('Locais de Instalação', ('locais_instalacao', ))
        )
    
class Editar(endpoints.EditEndpoint[Estampador]):
    class Meta:
        verbose_name = 'Editar Estampador'

    def get(self):
        return (
            super().get()
        )
