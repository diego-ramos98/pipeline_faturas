from datetime import date

class FormataDatas:

    def __init__(self):
        self.ano_vigente = date.today().year
        self.mes_vigente = date.today().month


    def data_formatada(self):
        data = date(self.ano_vigente,self.mes_vigente,1)
        return data
        

    def recupera_ano_vigente(self):
         return  self.ano_vigente

    def recupera_mes_vigente(self):
        return self.mes_vigente