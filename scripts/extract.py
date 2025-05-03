from imap_tools import MailBox,AND
from datetime import date
import os
import dotenv
import re

dotenv.load_dotenv()

def gera_chave_acesso():
    chave = os.getenv('ACESSO')
    return chave


def gera_usuario_acesso():
    usuario = os.getenv('USUARIO')
    return usuario



def acessa_email(usuario,chave):
    meu_email = MailBox("imap.gmail.com").login(usuario,chave)
    return meu_email


def pega_ano_vigente():
    ano_vigente = date.today().year
    return ano_vigente


def pega_mes_vigente():
    mes_vigente = date.today().month
    return mes_vigente


def formata_data_para_filtro(ano_vigente,mes_vigente):
    data = date(ano_vigente,mes_vigente,1)
    return data




def quantidade_emails_encontrados_com_filtro(meu_email,data):
    lista_emails = meu_email.fetch(AND(from_="todomundo@nubank.com.br",date_gte=data,body="Sua fatura foi fechada"),charset="UTF-8")

    quantidade_emails_encontrados = len(list(lista_emails))
    print(f"Quantidade de emails encontrados: {quantidade_emails_encontrados}")



def cria_caminho_salva_pdf(caminho,nome_arquivo):
    caminho = caminho
    nome_arquivo = nome_arquivo

    caminho_final = os.path.join(caminho,nome_arquivo)
    return caminho_final



def formatando_nome_anexo(ano_vigente,mes_vigente):
    nome_arquivo = re.compile(rf'Nubank_{(ano_vigente)}-0{(mes_vigente + 1)}-(0[1-9]|[12][0-9]|3[01]).pdf')
    print(nome_arquivo)
    return nome_arquivo



def transforma_anexo_em_pdf(nome_arquivo,meu_email,caminho):
    lista_emails = meu_email.fetch(AND(from_="todomundo@nubank.com.br",date_gte=data,body="Sua fatura foi fechada"),charset="UTF-8")
    
    for email in lista_emails:
        if len(email.attachments) > 0:
            for anexo in email.attachments:
                if nome_arquivo.search(anexo.filename):
                    info_anexo = anexo.payload
                    with open(caminho,"wb") as fatura_pdf:
                        fatura_pdf.write(info_anexo)

    

 



if __name__ == "__main__":
    chave       = gera_chave_acesso()
    usuario     = gera_usuario_acesso()
    meu_email   = acessa_email(usuario,chave)
    ano_vigente = pega_ano_vigente()
    mes_vigente = pega_mes_vigente()
    data        = formata_data_para_filtro(ano_vigente,mes_vigente)
    quantidade_emails_encontrados = quantidade_emails_encontrados_com_filtro(meu_email,data)
    caminho = cria_caminho_salva_pdf("../data_raw/","fatura.pdf")
    nome_arquivo = formatando_nome_anexo(ano_vigente,mes_vigente)
    transforma_anexo_em_pdf(nome_arquivo,meu_email,caminho)
    





    
