from slth import endpoints
from ..models import *

class Pessoas(endpoints.ListEndpoint[Pessoa]):

    def get(self):
        return super().get().actions('pessoa.cadastrar', 'pessoa.editar')


class Cadastrar(endpoints.AddEndpoint[Pessoa]):
    class Meta:
        verbose_name = 'Cadastrar Pessoa'

    def get(self):
        return (
            super().get()
        )
    
class Editar(endpoints.EditEndpoint[Pessoa]):
    class Meta:
        verbose_name = 'Editar Pessoa'

    def get(self):
        return (
            super().get()
        )
