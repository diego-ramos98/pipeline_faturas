from datetime import datetime,delta

class Fatura:
    def __init__(self,email_remetente,nome_fatura_fixo,data_envio):
        self.email_remetente = email_remetente
        self.nome_fatura = nome_fatura_fixo

    def gera_nome_fatura(self):
        nome_anexo = self.nome_fatura + 'oi' + '.pdf'
        return nome_anexo

 ##   def data_envio(data_envio):
