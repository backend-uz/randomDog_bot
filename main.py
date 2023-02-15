import requests
from time import sleep
TOKEN = "1950937652:AAEKFVSEwjT55RYro5X-3ILwKXnh_s6ThPU"

def getUpd():
    URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    r = requests.get(URL)
    resp = r.json()
    return resp['result']

def getLastUpd(result):
    response = result[-1]
    chat_id = response['message']['chat']['id']
    text = response['message']['text']
    update_id = response['update_id']
    message_id = response['message']['message_id']
    return chat_id, text, update_id, message_id

def sendPhoto(chat_id, photo):

    button1 = {'text':'Dog'}
    button2 = {'text':'Cat'}
    button3 = {'text':'Cow'}


    keyboard = [[button1,button2],[button3]]
    reply_markup = {'keyboard':keyboard, 'resize_keyboard': True}

    payload = {
        'chat_id':chat_id,
        'photo':photo,
        'reply_markup':reply_markup
    }    
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'

    r = requests.post(URL, json=payload)
    return r.json()

lastUpdId = -1

while True:
    result = getUpd()
    chat_id, text, update_id, message_id = getLastUpd(result)
    print(message_id)
    if text == 'Dog':
        r = requests.get('https://random.dog/woof.json')
        img_json = r.json()
        img = img_json['url']
    elif text == 'Cat':
        r = requests.get('https://aws.random.cat/meow')
        img_json = r.json()
        img = img_json['file']
    if update_id != lastUpdId:
        sendPhoto(chat_id, img)
        lastUpdId = update_id
    sleep(1)