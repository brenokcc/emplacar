from slth.application import Application


class ApiApplication(Application):
    def __init__(self):
        super().__init__()
        self.title = "Emplacar"
        self.subtitle = "Validação de Emplacamento Veicular"
        self.icon = "/static/images/logo.png"
        self.logo = "/static/images/logo.png"
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
            "clipboard-list:Tipos de Vículo": "tipoveiculo.tiposveiculo",
            "paintbrush:Cores": "cor.cores",
            "bookmark:Marcas": "marca.marcas",
            "car-side:Modelos": "modelo.modelos",
            "users-line:Pessoas": "pessoa.pessoas",
            "store-alt:Estampadores": "estampador.estampadores",
            "border-none:Emplacamentos": "emplacamento.emplacamentos",
            "sign-out:Sair": "auth.logout"
        })
