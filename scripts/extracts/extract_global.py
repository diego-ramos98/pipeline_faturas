import dotenv
import os
from models.salva_fatura import SalvaFatura
from models.email_cliente import EmailCliente
from models.formata_data import FormataDatas
import re
from datetime import date


def executa_extracao_global(USUARIO,CHAVE):

    data = FormataDatas()
    ano_vigente = data.recupera_ano_vigente() 
    mes_vigente = data.recupera_mes_vigente() 


    email_cliente = EmailCliente(usuario=USUARIO,chave=CHAVE,servidor_email="imap.gmail.com",email_remetente="cobranca@globalcbb.org.br",corpo_email_filtro="Passando rapidinho para lembrar que seu boleto",data_formatada=date(ano_vigente,mes_vigente - 1,1))

    

    meu_email = email_cliente.acessa_email()
    quantidade_emails_encontrados = email_cliente.retorna_quantidade_de_emails_com_filtro(meu_email)
    print(f"Quantidade de emails encontrados: {quantidade_emails_encontrados}")


    salva_fatura = SalvaFatura(email_remetente="cobranca@globalcbb.org.br",data_envio=date(ano_vigente,mes_vigente - 1,1),corpo_email_filtro="Passando rapidinho para lembrar que seu boleto",nome_fatura="fatura_global.pdf",meu_email=meu_email,padrao_nome_fatura=re.compile(rf'Dircley-Fortunato-(\d{{7}}).pdf'))


    salva_fatura.salva_pdf()


  
 

 
