from slth import endpoints
from ..models import *

class Emplacamentos(endpoints.QuerySetEndpoint[Emplacamento]):

    def get(self):
        dados = {}
        dados.update(versao='1.0.0', emplacamentos=[])
        queryset = super().get()
        for obj in queryset:
            dados['emplacamentos'].append(obj.to_json())
        return dados

    def check_permission(self):
        return True
    

class Emplacamento(endpoints.InstanceEndpoint[Emplacamento]):

    def get(self):
        dados = {}
        dados.update(versao='1.0.0', emplacamento=self.instance.to_json(detalhar=True))
        return dados

    def check_permission(self):
        return True