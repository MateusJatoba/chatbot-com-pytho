import webbrowser
from time import sleep
from urllib.parse import quote
import pyautogui
from PIL import Image

lista_transmissao = [
    {
        'numero': 000000000, #Numero escolhido por vc
        'nome': "*******"  #Nome escolhido por vc
    },

    {
        'numero': 000000000, #Numero escolhido por vc
        'nome': "******"  #Nome escolhido por vc
    },

    {
        'numero': 000000000, #Numero escolhido por vc
        'nome': "*******"  #Nome escolhido por vc
    },

    {
        'numero': 000000000, #Numero escolhido por vc
        'nome': "********" #Nome escolhido por vc
    }
]

for contatos in lista_transmissao:

    mensagem = f"Olá, {contatos['nome']}. Essa mensagem foi gerada automaticamente, não fui eu que enviei"
    mensagem = quote(mensagem)

    telefone = contatos['numero']

    link = f'https://web.whatsapp.com/send?phone=55{telefone}&text={mensagem}'


    webbrowser.open(link)


    sleep(7)

    pyautogui.hotkey('enter')
    sleep(5)
    pyautogui.hotkey('ctrl', 'w')



