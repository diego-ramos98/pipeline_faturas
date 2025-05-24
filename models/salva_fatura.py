from imap_tools import MailBox,AND
import os
import tabula
from datetime import date
from pdf2image import convert_from_path
import pytesseract

class SalvaFatura:
    def __init__(self,email_remetente,data_envio,corpo_email_filtro,nome_fatura,meu_email,padrao_nome_fatura):
        self.email_remetente = email_remetente
        self.data_envio = data_envio
        self.corpo_email_filtro = corpo_email_filtro
        self.nome_fatura = nome_fatura
        self.meu_email = meu_email
        self.padrao_nome_fatura = padrao_nome_fatura
        self.ano_vigente = date.today().year
        self.mes_vigente = date.today().month

    

    def formatando_nome_anexo(self):
        nome_anexo = self.padrao_nome_fatura
        
        return nome_anexo
    

    def cria_caminho_para_salvar_arquivo(self):
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
                        with open(self.cria_caminho_para_salvar_arquivo(),"wb") as fatura_pdf:
                            fatura_pdf.write(info_anexo)
                          
                    


    def salva_csv(self,numero_da_pagina_com_tabela):
        tabula.convert_into(self.cria_caminho_para_salvar_arquivo(),f'./data_raw/csv/{self.nome_fatura}.csv',output_format='csv',pages=numero_da_pagina_com_tabela)



        


    def salva_txt(self,numero_da_pagina_com_tabela,senha):
        paginas = convert_from_path(self.cria_caminho_para_salvar_arquivo(),dpi=300, userpw=senha)
        imagem = paginas[numero_da_pagina_com_tabela]

        texto = pytesseract.image_to_string(imagem,lang='por')

        with open(f'data_raw/txt/fatura_{self.nome_fatura}.txt', 'w', encoding='utf-8') as file:
            file.write(texto)



        