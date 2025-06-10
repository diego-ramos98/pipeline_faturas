import os
import findspark
from datetime import date

os.environ["SPARK_HOME"] = "/opt/spark/spark-3.5.5-bin-hadoop3"

findspark.init("/opt/spark/spark-3.5.5-bin-hadoop3")

from pyspark.sql import SparkSession

# Crie a SparkSession
spark = SparkSession.builder \
    .appName("Transformação de Faturas") \
    .master("local[*]") \
    .getOrCreate()

print(spark)


def lendo_csv():
    mes = date.today().month
    ano = date.today().year

    df_conta = spark.read.csv(f"../../data_raw/csv/Nubank_0{mes}-{ano}.csv")
    df_conta.show().limit(5)
    return df_conta

def cria_view(dataframe,nome_view):
    dataframe.createOrReplaceTempView('view_gastos')


def muda_nome_colunas(dataframe):
    dataframe = spark.sql('SELECT _c0 AS DATA_FATURA,_c1 AS ESTABELECIMENTO,_c2 AS PRECO FROM view_gastos')
    return dataframe

def exclui_valores_nulos(dataframe):
    dataframe = spark.sql("SELECT * FROM view_gastos WHERE ESTABELECIMENTO is not null")
    return dataframe


def formata_data(dataframe):
    dataframe = spark.sql("SELECT substring(DATA_FATURA,1,6) AS DATA_FATURA ,ESTABELECIMENTO,substring(PRECO,4,8) AS PRECO FROM view_gastos")

    dataframe = spark.sql('''
    SELECT 
        CONCAT(
           substring(DATA_FATURA, 1, 2),
            CASE substring(DATA_FATURA, 4, 3)
                WHEN 'JAN' THEN '01' 
                WHEN 'FEV' THEN '02' 
                WHEN 'MAR' THEN '03' 
                WHEN 'ABR' THEN '04'
                WHEN 'MAI' THEN '05' 
                WHEN 'JUN' THEN '06' 
                WHEN 'JUL' THEN '07' 
                WHEN 'AGO' THEN '08' 
                WHEN 'SET' THEN '09'
                WHEN 'OUT' THEN '10' 
                WHEN 'NOV' THEN '11'
                WHEN 'DEZ' THEN '12'
            END,
            year(current_date())
          
          ) AS DATA,
          ESTABELECIMENTO,
          PRECO
    FROM    view_gastos
       
        ''')

    dataframe = spark.sql('''
    SELECT 
        to_date(DATA, 'ddMMyyyy') AS DATA,
        ESTABELECIMENTO,
        PRECO
    FROM view_gastos
    ''')


    return dataframe


def formata_preco(dataframe):
    dataframe = spark.sql("SELECT DATA,ESTABELECIMENTO,replace(PRECO,',','.')  as PRECO FROM  view_gastos")
    dataframe = spark.sql("SELECT DATA,ESTABELECIMENTO,cast(PRECO as  decimal(10,2)) AS PRECO  FROM  view_gastos")

    return dataframe


def seperando_coluna_estabelecimento_parcela(dataframe):
    dataframe = spark.sql("""
    SELECT 
        DATA, 
        ESTABELECIMENTO,
        CASE 
            WHEN ESTABELECIMENTO LIKE '%Parcela%' 
            THEN SUBSTRING(ESTABELECIMENTO, -11)
            ELSE NULL
        END AS PARCELA,
        PRECO
    FROM view_gastos
    """)


    dataframe = spark.sql('''
            SELECT CASE 
                        WHEN ESTABELECIMENTO LIKE '%Parcela%' 
                        THEN SUBSTRING(ESTABELECIMENTO,1,POSITION('-' IN ESTABELECIMENTO)-1) 
                        ELSE ESTABELECIMENTO 
                    END AS ESTABELECIMENTO,
		            DATA,
                    PARCELA,
                    PRECO
            FROM 	view_gastos               
                ''')


    dataframe = spark.sql("SELECT ESTABELECIMENTO,DATA, SUBSTRING(PARCELA,9) AS PARCELA,SUBSTRING(PARCELA,-1) AS QUANTIDADE_PARCELAS,PRECO FROM view_gastos")

    return dataframe


    def adicionando_coluna(dataframe):
        dataframe = spark.sql("SELECT 'NUBANK' AS NOME_FATURA,ESTABELECIMENTO,DATA,CAST(SUBSTRING(PARCELA,1,1) AS INT) AS PARCELA,CAST(QUANTIDADE_PARCELAS AS INT),PRECO FROM view_gastos")


    


if __name__ == "__main__":
    df = lendo_csv()
    df.printSchema()







