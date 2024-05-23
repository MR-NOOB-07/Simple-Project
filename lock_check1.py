# youtube channel > @mrnoob-07
# subscribe my YouTube channel 😄
import os, requests
uid = input(' UID > ')
url = f'https://graph.facebook.com/{uid}/picture?type=normal'
try:
    req = requests.get(url).text
    if 'Photoshop' in req:
        print(f'\033[1;32m LIVE UID {uid}')
    else:
        print(f'\033[1;31m DEAD UID {uid}')
except:pass
