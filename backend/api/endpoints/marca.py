from slth import endpoints
from ..models import *

class Marcas(endpoints.ListEndpoint[Marca]):

    def get(self):
        return super().get().actions('marca.cadastrar', 'marca.editar')


class Cadastrar(endpoints.AddEndpoint[Marca]):
    class Meta:
        verbose_name = 'Cadastrar Marca'

    def get(self):
        return (
            super().get()
        )
    
class Editar(endpoints.EditEndpoint[Marca]):
    class Meta:
        verbose_name = 'Editar Marca'

    def get(self):
        return (
            super().get()
        )
