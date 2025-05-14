from imap_tools import MailBox,AND
import os
import re

class SalvaFatura:
    def __init__(self,email_remetente,data_envio,corpo_email_filtro,caminho,nome_arquivo,mes_vigente,ano_vigente,meu_email,padrao_nome_fatura):
        self.email_remetente = email_remetente
        self.data_envio = data_envio
        self.corpo_email_filtro = corpo_email_filtro
        self.caminho = caminho
        self.nome_arquivo = nome_arquivo
        self.mes_vigente = mes_vigente
        self.ano_vigente = ano_vigente
        self.meu_email = meu_email
        self.padrao_nome_fatura = padrao_nome_fatura

    

    def cria_caminho_para_salvar_pdf(self):
        caminho_final = os.path.join(self.caminho,self.nome_arquivo)
        return caminho_final

    def formatando_nome_anexo(self):
        nome_anexo = self.padrao_nome_fatura
        
        return nome_anexo
    



    def salva_pdf(self):
        lista_emails = self.meu_email.fetch(AND(from_=self.email_remetente,date_gte=self.data_envio,body=self.corpo_email_filtro),charset="UTF-8")
        for email in lista_emails:
            print('oi-2')
            if len(email.attachments) > 0:
                for anexo in email.attachments:
                    print(anexo.filename)
                    print(self.formatando_nome_anexo())
                    if self.formatando_nome_anexo().search(anexo.filename):
                        info_anexo = anexo.payload
                        print(self.cria_caminho_para_salvar_pdf())
                        with open(self.cria_caminho_para_salvar_pdf(),"wb") as fatura_pdf:
                            fatura_pdf.write(info_anexo)


    