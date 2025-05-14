import dotenv
import os
from models.salva_fatura import SalvaFatura
from models.email_cliente import EmailCliente
from models.formata_data import FormataDatas
import re

if __name__ == "__main__":
    dotenv.load_dotenv()
    
    USUARIO = os.getenv('USUARIO')
    CHAVE  = os.getenv('CHAVE')

    data = FormataDatas()
    data_formatada = data.data_formatada()
    ano_vigente = data.recupera_ano_vigente()
    mes_vigente = data.recupera_mes_vigente()


    email_cliente = EmailCliente(usuario=USUARIO,chave=CHAVE,servidor_email="imap.gmail.com",email_remetente="faturadigital@itau.com.br",corpo_email_filtro="Sua fatura foi fechada",data_formatada=data_formatada)

    

    meu_email = email_cliente.acessa_email()
    quantidade_emails_encontrados = email_cliente.retorna_quantidade_de_emails_com_filtro(meu_email)
    print(f"Quantidade de emails encontrados: {quantidade_emails_encontrados}")
    

    print("oi")

    salva_fatura = SalvaFatura(email_remetente="faturadigital@itau.com.br",data_envio=data_formatada,corpo_email_filtro="Sua fatura foi fechada",caminho="../data_raw/pdf/",nome_arquivo="fatura_itau.pdf",mes_vigente=mes_vigente,ano_vigente=ano_vigente,meu_email=meu_email,padrao_nome_fatura=re.compile(rf'Fatura_VISA_(\d{{12}})_0{mes_vigente}-{ano_vigente}\.pdf'))



    salva_fatura.salva_pdf()

 
#Fatura_VISA_100054690261_02-2025.pdf