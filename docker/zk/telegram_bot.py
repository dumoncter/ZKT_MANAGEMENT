import requests
from zk import setings


def send_msg(text):
    token = setings.token
    chat_id = setings.chat_id
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print('Send message successful')
