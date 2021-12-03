import requests
import time

#token robo
token = "1866900133:AAF2Ozmxpv1xtskGQqNAEz9kjBDQV5oiyEA"
update_id = "579477509"

#################################  APIS   #################################

def _get_message(update_id):
    url = 'https://api.telegram.org/bot{0}/getUpdates?offset={1}'.format(token, update_id)
    response = requests.get(url)
    response_json = response.json()
    last_updated_id = update_id
    for i in response_json['result']:
        try:
            first_name = i['message']['chat']['first_name']
            last_name = i['message']['chat']['last_name']
            chat_id = i['message']['chat']['id']
            last_updated_id = i['update_id']
            text = i['message']['text']
            #print (first_name, last_name, chat_id, update_id, text)
            if last_updated_id != update_id:
                Valida_Texto(text,chat_id,first_name)
        except:
            print("Caiu na excepetion --- ")
    return (last_updated_id)

def _send_message(text, chat_id):
    url = 'https://api.telegram.org/bot{0}/sendMessage'.format(token)
    data = {'chat_id':chat_id, 'text':text}
    response = requests.post(url, data=data)
    print(response.content)

def Valida_Texto(text,chat_id,nome):
    if text == "ingresso" or text == "Ingresso":
        _send_message("Ola "+nome+ " seja bem vindo ao TicketBot!! \n\nEstamos com os seguintes eventos, para escolher basta digitar o nome do evento. \n1 - Jogos\n2 - Shows\n", chat_id)
    elif text == "comprar" or text == "Comprar":
        _send_message("Sua compra foi realizada com sucesso!!!\nSeu ingresso chegará pelo seu e-mail!\nO TicketBot agradece pela preferência", chat_id)
    elif text == "Menu" or text == "menu":
        _send_message("Menu: \n\nEstamos com os seguintes eventos, para escolher basta digitar o nome do evento. \n1 - Jogos\n2 - Shows", chat_id)
    elif text == "Jogos" or text == "jogos":
        _send_message("Jogos\n\n basta digitar o nome do time o qual quer assistir:\n 1 - Corinthians vs São Paulo\n 2 - Santos vs Palmeiras\n 3 - Portuguesa vs Ceara\n 4 - Botafogo vs Flamengo", chat_id)
    elif text == "corinthians" or text == "Corinthians" or text == "são paulo" or text == "São Paulo":
        _send_message("Jogo Corinthians vs São Paulo\n\n Preço: R$ 40,00 (inteira) / R$ 20,00 (meia entrada com comprovante)\nLocal do jogo: Arena Corinthians\n\nBasta digitar 'comprar' para adquirir seu ingresso\n\n Para acessar o menu digite 'Menu'", chat_id)
    elif text == "santos" or text == "palmeiras":
        _send_message("Jogo Santos vs Palmeiras\n\n Preço: R$ 30,00 (inteira) / R$ 15,00 (meia entrada com comprovante)\nLocal do jogo: Estádio Urbano Caldeira\n\nBasta digitar 'comprar' para adquirir seu ingresso\n\n Para acessar o menu digite 'Menu'", chat_id)
    elif text == "Portuguesa" or text == "Ceara":
        _send_message("Jogo Portuguesa vs Ceara\n\n Preço: R$ 25,00 (inteira) / R$ 12,50 (meia entrada com comprovante)\nLocal do jogo: Estádio Canindé\n\nBasta digitar 'comprar' para adquirir seu ingresso\n\n Para acessar o menu digite 'Menu'", chat_id)
    elif text == "Botafogo" or text == "Flamengo":
        _send_message("Jogo Botafogo vs Flamengo\n\n Preço: R$ 20,00 (inteira) / R$ 10,00 (meia entrada com comprovante)\nLocal do jogo: Estádio Nilton Santos\n\nBasta digitar 'comprar' para adquirir seu ingresso\n\n Para acessar o menu digite 'Menu'", chat_id)
    elif text == "Shows":
        _send_message("Shows\n\n basta digitar o nome do Show o qual quer participar:\n 1 - Charlie Brown Jr\n 2 - Coldplay\n 3 - Metalica\n 4 - Wesley Safaďão\n 5 - Turma do Pagode", chat_id)
    elif text == "Charlie Brown Jr" or text == "charlie brown jr":
        _send_message("Show Charlie Brown Jr\n\n Preço: R$ 50,00 (inteira) / R$ 25,00 (meia entrada com comprovante + 1kg de alimento perecivel)\nLocal do Show: Caraguatatuba\n\nBasta digitar 'comprar' para adquirir seu ingresso\n\n Para acessar o menu digite 'Menu'", chat_id)
    elif text == "Coldplay" or text == "coldplay":
        _send_message("Show Coldplay\n\n Preço: R$ 200,00 (inteira) / R$ 100,00 (meia entrada com comprovante)\nLocal do Show: Allianz Parque\n\nBasta digitar 'comprar' para adquirir seu ingresso\n\n Para acessar o menu digite 'Menu'", chat_id)
    elif text == "Metalica" or text == "metalica":
        _send_message("Metalica\n\n Preço: R$ 150,00 (inteira) / R$ 75,00 (meia entrada com comprovante)\nLocal do Show: Sonora Garden\n\nBasta digitar 'comprar' para adquirir seu ingresso\n\n Para acessar o menu digite 'Menu'", chat_id)
    elif text == "Wesley Safaďão" or text == "wesley safaďão":
        _send_message("Wesley Safaďão\n\n Preço: R$ 100,00 (inteira) / R$ 50,00 (meia entrada com comprovante)\nLocal do Show: Anhembi Pavilhao 57\n\nBasta digitar 'comprar' para adquirir seu ingresso\n\n Para acessar o menu digite 'Menu'", chat_id)
    elif text == "Turma do Pagode" or text == "turma do pagode":
        _send_message("Turma do Pagode\n\n Preço: R$ 70,00 (inteira) / R$ 35,00 (meia entrada com comprovante)\nLocal do Show: Quadra Rosas de Ouro\n\nBasta digitar 'comprar' para adquirir seu ingresso\n\n Para acessar o menu digite 'Menu'", chat_id)
    else:
        _send_message("Oooi, sou o TicketBot\n\nPara mais informações digite 'Ingresso'", chat_id)

while True:
    update_id = _get_message(update_id)
  
    

            

      