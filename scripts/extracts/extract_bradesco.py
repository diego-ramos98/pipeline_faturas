import dotenv
import os
from models.salva_fatura import SalvaFatura
from models.email_cliente import EmailCliente
from models.formata_data import FormataDatas
from datetime import date 
import re


def executa_extracao_bradesco(USUARIO,CHAVE):

    data = FormataDatas()
    ano_vigente = data.recupera_ano_vigente()
    mes_vigente = data.recupera_mes_vigente()
    

    email_cliente = EmailCliente(usuario=USUARIO,chave=CHAVE,servidor_email="imap.gmail.com",email_remetente="diego.ramos.fortunato@gmail.com",corpo_email_filtro="Fatura Bradesco",data_formatada=date(ano_vigente,mes_vigente,1))

    meu_email = email_cliente.acessa_email()
    quantidade_emails_encontrados = email_cliente.retorna_quantidade_de_emails_com_filtro(meu_email)
    print(f"Quantidade de emails encontrados: {quantidade_emails_encontrados}")
    



    salva_fatura = SalvaFatura(email_remetente="diego.ramos.fortunato@gmail.com",data_envio=date(ano_vigente,mes_vigente,1),corpo_email_filtro="Fatura Bradesco",nome_fatura=f"Bradesco_0{mes_vigente}-{ano_vigente}",meu_email=meu_email,padrao_nome_fatura=re.compile(rf'BradescoCartoes{ano_vigente}-0{mes_vigente}-(0[1-9]|[12][0-9]|3[01]).(\d{{6}}).pdf'))
          
                              
    salva_fatura.salva_pdf()
    salva_fatura.salva_csv('1')

