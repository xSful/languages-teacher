from gigachat import GigaChat
from dotenv import load_dotenv
import os

load_dotenv()

GIGACHAT_API_KEY = os.getenv("GIGACHAT_API_KEY")

giga = GigaChat(
   credentials=GIGACHAT_API_KEY,
   ca_bundle_file="russian_trusted_root_ca.cer",
   #verify_ssl_certs=False,
   scope="GIGACHAT_API_PERS",
   model="GigaChat",
)
response = giga.get_token()

print(response)
""" try:
    response = giga.chat("Привет! Как дела?")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Ошибка: {e}") """