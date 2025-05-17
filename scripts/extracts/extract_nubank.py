import dotenv
import os
from models.salva_fatura import SalvaFatura
from models.email_cliente import EmailCliente
from models.formata_data import FormataDatas
from datetime import date 
import re


if __name__ == "__main__":
    dotenv.load_dotenv()

    USUARIO = os.getenv('USUARIO')
    CHAVE  = os.getenv('CHAVE')

    data = FormataDatas()

    data_formatada = date(2025,4,1)
    ano_vigente = data.recupera_ano_vigente()
    mes_vigente = 4
    

    email_cliente = EmailCliente(usuario=USUARIO,chave=CHAVE,servidor_email="imap.gmail.com",email_remetente="todomundo@nubank.com.br",corpo_email_filtro="Sua fatura foi fechada",data_formatada=data_formatada)

    meu_email = email_cliente.acessa_email()
    quantidade_emails_encontrados = email_cliente.retorna_quantidade_de_emails_com_filtro(meu_email)
    print(f"Quantidade de emails encontrados: {quantidade_emails_encontrados}")
    



    salva_fatura = SalvaFatura(email_remetente="todomundo@nubank.com.br",data_envio=data_formatada,corpo_email_filtro="Sua fatura foi fechada",nome_fatura="Nubank",mes_vigente=mes_vigente,ano_vigente=ano_vigente,meu_email=meu_email,padrao_nome_fatura=re.compile(rf'Nubank_{(ano_vigente)}-0{(mes_vigente + 1)}-(0[1-9]|[12][0-9]|3[01]).pdf'))
                               
                              
    salva_fatura.salva_pdf()




    
    
