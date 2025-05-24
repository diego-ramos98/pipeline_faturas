from scripts.extracts import extract_itau,extract_nubank
import dotenv
import os

dotenv.load_dotenv()

USUARIO = os.getenv('USUARIO')
CHAVE  = os.getenv('CHAVE')
USUARIO_SEGUNDO_EMAIL = os.getenv('USUARIO_SEGUNDO_EMAIL')
CHAVE_SEGUNDO_EMAIL   = os.getenv('CHAVE_SEGUNDO_EMAIL')


def main():
    try:
        extract_itau.executa_extracao_itau(USUARIO,CHAVE)
    except Exception  as e:
        print(f"Erro na extração dos dados da fatura do Itau: {e}")


    try:
        extract_nubank.executa_extracao_nubank(USUARIO,CHAVE)
    except Exception  as e:
        print(f"Erro na extração dos dados da fatura do Nubank: {e}")



if __name__ == "__main__":
    main()



