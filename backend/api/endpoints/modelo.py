from slth import endpoints
from ..models import *

class Modelos(endpoints.ListEndpoint[Modelo]):

    def get(self):
        return super().get().actions('modelo.cadastrar', 'modelo.editar')


class Cadastrar(endpoints.AddEndpoint[Modelo]):
    class Meta:
        verbose_name = 'Cadastrar Modelo'

    def get(self):
        return (
            super().get()
        )
    
class Editar(endpoints.EditEndpoint[Modelo]):
    class Meta:
        verbose_name = 'Editar Modelo'

    def get(self):
        return (
            super().get()
        )
