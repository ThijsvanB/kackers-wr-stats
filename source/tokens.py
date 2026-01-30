import requests
from requests.auth import HTTPBasicAuth

def get_ticket():
    basic = HTTPBasicAuth("vanberkelthijs2@gmail.com","g,W[$93852]HMUMR")
    print(basic)

    url = "https://public-ubiservices.ubi.com/v3/profiles/sessions"
    headers = {"Content-Type": "application/json", "Ubi-AppId":"86263886-327a-4328-ac69-527f0d20a237", "User-Agent":"ThijsvanB"}

    x = requests.post(url, headers=headers, auth=basic)

    print("Request ticket: ", x)

    print(x.text)

    if(x.status_code != 200):
        return -1

    return x.text.split('"')[7]

def get_Live_API_token(ticket):
    url = "https://prod.trackmania.core.nadeo.online/v2/authentication/token/ubiservices"

    headers = {"Content-Type": "application/json", "Authorization": "ubi_v1 t=" + ticket, "User-Agent":"ThijsvanB"}
    body = {"audience": "NadeoLiveServices"}

    x = requests.post(url, headers = headers, json=body)

    print("Request live token: ", x)
    return [x.text.split('"')[3], x.text.split('"')[7]]

def get_Core_API_token(ticket):
    url = "https://prod.trackmania.core.nadeo.online/v2/authentication/token/ubiservices"

    headers = {"Content-Type": "application/json", "Authorization": "ubi_v1 t=" + ticket, "User-Agent":"ThijsvanB"}
    body = {"audience": "NadeoServices"}

    x = requests.post(url, headers = headers, json=body)

    print(x)
    return [x.text.split('"')[3], x.text.split('"')[7]]

def getCoreTokenFromFile():
    f = open("CoreToken.txt")
   
    lines = f.readlines()
    
    f.close()

    return [lines[0][:-1], lines[1]]

def getLiveTokenFromFile():
    f = open("LiveToken.txt")
   
    lines = f.readlines()
    
    f.close()

    return [lines[0][:-1], lines[1]]

def saveCoreTokenToFile(coreToken):
    f = open("CoreToken.txt", "w+")

    f.write(coreToken[0])
    f.write('\n')
    f.write(coreToken[1])

    f.close()

def saveLiveTokenToFile(liveToken):
    f = open("LiveToken.txt", "w+")

    f.write(liveToken[0])
    f.write('\n')
    f.write(liveToken[1])

    f.close()

def refresh_tokens(refreshToken):
    url = "https://prod.trackmania.core.nadeo.online/v2/authentication/token/refresh"

    headers = {"Content-Type": "application/json", "Authorization": "nadeo_v1 t=" + refreshToken, "User-Agent":"ThijsvanB"}
    
    x = requests.post(url, headers = headers)

    print(x)
    return [x.text.split('"')[3], x.text.split('"')[7]]

def get_new_tokens():
    ticket = get_ticket()
    liveToken = get_Live_API_token(ticket)
    coreToken = get_Core_API_token(ticket)

    saveCoreTokenToFile(coreToken)
    saveLiveTokenToFile(liveToken)

def ret_new_tokens():
    ticket = get_ticket()
    liveToken = get_Live_API_token(ticket)
    coreToken = get_Core_API_token(ticket)

    return [liveToken, coreToken]