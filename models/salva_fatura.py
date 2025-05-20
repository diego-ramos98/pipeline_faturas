from imap_tools import MailBox,AND
import os
import re

class SalvaFatura:
    def __init__(self,email_remetente,data_envio,corpo_email_filtro,nome_fatura,meu_email,padrao_nome_fatura):
        self.email_remetente = email_remetente
        self.data_envio = data_envio
        self.corpo_email_filtro = corpo_email_filtro
        self.nome_fatura = nome_fatura
        self.meu_email = meu_email
        self.padrao_nome_fatura = padrao_nome_fatura

    

    def formatando_nome_anexo(self):
        nome_anexo = self.padrao_nome_fatura
        
        return nome_anexo
    

    def cria_caminho_para_salvar_pdf(self):
        caminho_pasta_pdf = os.path.join("data_raw", "pdf")
        os.makedirs(caminho_pasta_pdf, exist_ok=True)

        nome_arquivo_pdf = f"fatura_{self.nome_fatura}.pdf"
        caminho_pdf = os.path.join(caminho_pasta_pdf, nome_arquivo_pdf)

        return caminho_pdf



    def salva_pdf(self):
        lista_emails = self.meu_email.fetch(AND(from_=self.email_remetente,date_gte=self.data_envio,body=self.corpo_email_filtro),charset="UTF-8")
        for email in lista_emails:
            if len(email.attachments) > 0:
                for anexo in email.attachments:
                    if self.formatando_nome_anexo().search(anexo.filename):
                        info_anexo = anexo.payload
                        with open(self.cria_caminho_para_salvar_pdf(),"wb") as fatura_pdf:
                            fatura_pdf.write(info_anexo)
                          
                    


    


