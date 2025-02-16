from slth import endpoints
from ..models import *

class Cores(endpoints.ListEndpoint[Cor]):

    def get(self):
        return super().get().actions('cor.cadastrar', 'cor.editar')


class Cadastrar(endpoints.AddEndpoint[Cor]):
    class Meta:
        verbose_name = 'Cadastrar Cor'

    def get(self):
        return (
            super().get()
        )
    
class Editar(endpoints.EditEndpoint[Cor]):
    class Meta:
        verbose_name = 'Editar Cor'

    def get(self):
        return (
            super().get()
        )
