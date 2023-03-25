import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import apiData

load_dotenv()

url = requests.get("https://weather.com/es-AR/tiempo/hoy/l/d833bc28b0a3859e74294bedd408efea8bc9f2a22d9ebc3bcb815c922ee5f788")
soup = BeautifulSoup(url.content, "html.parser")

result = soup.find("span", class_="CurrentConditions--tempValue--MHmYY").getText()

print(result)

def telegram_bot_sendtext(bot_message):
    
    bot_token = apiData.token
    bot_chatID = apiData.api_id  
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

test = telegram_bot_sendtext(f"La temperatura actual en la Ciudad de Buenos Aires es de ${result}")
print(test)