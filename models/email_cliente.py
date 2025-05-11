from imap_tools import MailBox,AND

class EmailCliente:
    def __init__(self,usuario,chave,servidor_email,email_remetente,corpo_email_filtro,data_formatada):
        self.usuario = usuario;
        self.chave  = chave
        self.servidor_email   = servidor_email
        self.email_remetente = email_remetente
        self.corpo_email_filtro = corpo_email_filtro
        self.data_formatada = data_formatada

    def acessa_email(self):
        meu_email = MailBox(self.servidor_email).login(self.usuario,self.chave)
        return meu_email
    
    def retorna_quantidade_de_emails_com_filtro(self,meu_email):
        lista_emails = meu_email.fetch(AND(from_=self.email_remetente,date_gte=self.data_formatada,body=self.corpo_email_filtro),charset="UTF-8")
        
        return len(list(lista_emails))
    

   
        

