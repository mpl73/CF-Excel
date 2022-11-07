import requests
import os

url = 'http://192.168.33.100:8000'
        
while(True):
    try:
        status = requests.get(url).status_code
        print(f"O servidor está disponível | {status}.")
    except:
        print("O servidor está indisponível | 0")
        os.system('D:')
        os.system('cd D:\Heroku\cf-excel')
        os.system('python manage.py runserver 192.168.33.100:8000')
