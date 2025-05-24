import dotenv
import os
from models.salva_fatura import SalvaFatura
from models.email_cliente import EmailCliente
from models.formata_data import FormataDatas
import re

def executa_extracao_itau(USUARIO,CHAVE):

    dotenv.load_dotenv()

    SENHA = os.getenv("SENHA")

    data = FormataDatas()
    data_formatada = data.data_formatada()
    ano_vigente = data.recupera_ano_vigente()
    mes_vigente = data.recupera_mes_vigente()


    email_cliente = EmailCliente(usuario=USUARIO,chave=CHAVE,servidor_email="imap.gmail.com",email_remetente="faturadigital@itau.com.br",corpo_email_filtro="Sua fatura foi fechada",data_formatada=data_formatada)

    

    meu_email = email_cliente.acessa_email()
    quantidade_emails_encontrados = email_cliente.retorna_quantidade_de_emails_com_filtro(meu_email)
    print(f"Quantidade de emails encontrados: {quantidade_emails_encontrados}")

    
    salva_fatura = SalvaFatura(email_remetente="faturadigital@itau.com.br",data_envio=data_formatada,corpo_email_filtro="Sua fatura foi fechada",nome_fatura=f"Itau_0{mes_vigente}-{ano_vigente}",meu_email=meu_email,padrao_nome_fatura=re.compile(rf'Fatura_VISA_(\d{{12}})_0{mes_vigente}-{ano_vigente}.pdf'))


    salva_fatura.salva_pdf()
    salva_fatura.salva_txt(numero_da_pagina_com_tabela=1,senha=SENHA)

 
