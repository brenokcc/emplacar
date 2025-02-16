from slth.application import Application


class ApiApplication(Application):
    def __init__(self):
        super().__init__()
        self.title = "Emplacar"
        self.subtitle = "Validação de Emplacamento Veicular"
        self.icon = "/static/images/scan.png"
        self.logo = "/static/images/scan.png"
        self.groups.add(administrador='Administrador', operador= "Operador")
        self.dashboard.usermenu.add(
            "dev.icons", "user.users", "log.logs", "email.emails",
            "pushsubscription.pushsubscriptions", "job.jobs",
            "deletion.deletions", "auth.logout"
        )
        # self.menu.add({
        #     "users:Item 1": {
        #         "Item 1.1": {
        #             "Sair": "auth.logout"
        #         },
        #             "Sair": "auth.logout"
        #     },
        #     "Sair": "auth.logout"
        # })
        self.menu.add({
            "Tipos de Vículo": "tipoveiculo.tiposveiculo",
            "Cores": "cor.cores",
            "Marcas": "marca.marcas",
            "Modelos": "modelo.modelos",
            "Pessoas": "pessoa.pessoas",
            "Estampadores": "estampador.estampadores",
            "Emplacamentos": "emplacamento.emplacamentos",
            "Sair": "auth.logout"
        })
