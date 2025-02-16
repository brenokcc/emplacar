from slth import endpoints
from ..models import *

class Emplacamentos(endpoints.ListEndpoint[Emplacamento]):

    def get(self):
        return super().get().fields('estampador', 'operador', 'numero_placa', 'proprietario', 'modelo', 'cor').actions('emplacamento.cadastrar', 'emplacamento.editar')


class Cadastrar(endpoints.AddEndpoint[Emplacamento]):
    class Meta:
        verbose_name = 'Cadastrar Emplacamento'

    def get(self):
        return (
            super().get()
        )
    
class Editar(endpoints.EditEndpoint[Emplacamento]):
    class Meta:
        verbose_name = 'Editar Emplacamento'

    def get(self):
        return (
            super().get()
        )
