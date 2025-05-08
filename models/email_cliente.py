from imap_tools import MailBox,AND

class EmailCliente:
    def __init__(self,usuario,chave,servidor_email,email_remetente,corpo_email_filtro):
        self.usuario = usuario;
        self.chave  = chave
        self.servidor_email   = servidor_email

    def acessa_email(self,email):
        meu_email = MailBox(self.servidor_email).login(self.usuario,self.chave)
        return meu_email
    
    def retorna_quantidade_de_emails_com_filtro(self,email_remetente,corpo_email_filtro,data_formatada):
        lista_emails = self.acessa_email.fetch(AND(from_=email_remetente,date_gte=data_formatada,body=corpo_email_filtro),charset="UTF-8")
        
        quantidade_emails_encontrados = len(list(lista_emails))

        print(f"Quantidade de emails encontrados: {quantidade_emails_encontrados}")
        

