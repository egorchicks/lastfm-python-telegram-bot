import requests
from secret import LFTOKEN

url_recent = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks"
url_top = "http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks"
user = 'Exzotics'
limit = 12
api_key = LFTOKEN
format = 'json'

def get_recent(user):
    response = requests.get(
        url_recent,
        params={
            'user': user, 
            'limit': limit, 
            'api_key': api_key, 
            'format': format
        }
    )

    d = response.json()["recenttracks"]["track"]
    l = ''

    for i in range(limit):
        l += f'{d[i]["artist"]["#text"]} - {d[i]["name"]} \n'
    return l

def get_top(user):
    response = requests.get(
        url_top,
        params={
            'user': user, 
            'limit': limit, 
            'api_key': api_key, 
            'format': format
        }
    )

    d = response.json()["toptracks"]["track"]
    l = ''

    for i in range(limit):
        l += f'{d[i]["artist"]["name"]} - {d[i]["name"]} \n'
    return l

def get_week(user):
    response = requests.get(
        url_top,
        params={
            'user': user, 
            'limit': limit, 
            'api_key': api_key, 
            'format': format,
            'period': '7day'
        }
    )

    d = response.json()["toptracks"]["track"]
    l = ''

    for i in range(limit):
        l += f'{d[i]["artist"]["name"]} - {d[i]["name"]} \n'
    return l

def get_month(user):
    response = requests.get(
        url_top,
        params={
            'user': user, 
            'limit': limit, 
            'api_key': api_key, 
            'format': format,
            'period': '1month'
        }
    )

    d = response.json()["toptracks"]["track"]
    l = ''

    for i in range(limit):
        l += f'{d[i]["artist"]["name"]} - {d[i]["name"]} \n'
    return l

def get_year(user):
    response = requests.get(
        url_top,
        params={
            'user': user, 
            'limit': limit, 
            'api_key': api_key, 
            'format': format,
            'period': '12month'
        }
    )

    d = response.json()["toptracks"]["track"]
    l = ''

    for i in range(limit):
        l += f'{d[i]["artist"]["name"]} - {d[i]["name"]} \n'
    return l

if __name__ == '__main__':
    import sys
    user = ' '.join(sys.argv[1:])
    if not user:
        user = "Exzotics"

#print(get_recent(user))
print(get_top(user))

