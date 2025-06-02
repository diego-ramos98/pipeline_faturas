from scripts.extracts import extract_nubank,extract_bradesco
import dotenv
import os

dotenv.load_dotenv()

USUARIO = os.getenv('USUARIO')
CHAVE  = os.getenv('CHAVE')



def main():
    try:
        extract_nubank.executa_extracao_nubank(USUARIO,CHAVE)
    except Exception  as e:
        print(f"Erro na extração dos dados da fatura do Nubank: {e}")

    try:
        extract_bradesco.executa_extracao_bradesco(USUARIO,CHAVE)
    except Exception as e:
        print(f"Erro na extração dos dados da fatura do Bradesco: {e}")



if __name__ == "__main__":
    main()



