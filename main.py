# -*- coding: utf-8 -*-
import requests, json, schedule, threading
from random import randint, randrange
from json import load, loads
from time import sleep

with open("config.json", encoding='utf-8') as f: # cfg
         config = load(f)

print('Enter your authorization: ')
authorization = str(input()).rstrip().lstrip()

job_name = config["job_name"] 
min_price = config["min_price"] 
max_price = config["max_price"]
buy_slave = config["buy_slave"]
buy_fetter = config["buy_fetter"]

print(f'Job name: {job_name}')
print(f'Min price: {min_price}, max price: {max_price}')
print(f'Buy slave: {buy_slave}')
print(f'Buy fetter: {buy_fetter}')

def myProfile():
    global authorization
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/start'
    payload = {}
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    while 1:
        response = requests.request('GET', url, headers=headers, data=payload)
        if response.status_code == 200:
            break
    return response.json()

def userProfile(user_id):
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/user?id=' + str(user_id)
    payload = {}
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    while 1:
        response = requests.request('GET', url, headers=headers, data=payload)
        if response.status_code == 200:
            break
    return response.json()

def topUsers():
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/topUsers'
    payload = {}
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.request('GET', url, headers=headers, data=payload)
    return response.json()

def jobSlave(slave_id):
    global job_name
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/jobSlave'
    payload = json.dumps({'slave_id':slave_id, 
     'name':job_name[randrange(0, len(job_name))]})
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0', 
     'content-type':'application/json',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.request('POST', url, headers=headers, data=payload)
    if response.status_code == 422:
        print(f'Error when installing the job, possibly cooldown. Slave: {slave_id}')
    elif response.status_code == 200:
        print(f'Set job: {slave_id}') 
    else:
        print(f'Unknown error. Slave: {slave_id}')
    return response.json()

def buyFetter(slave_id):
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/buyFetter'
    payload = json.dumps({'slave_id': slave_id})
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0', 
     'content-type':'application/json',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.request('POST', url, headers=headers, data=payload)
    if response.status_code == 422:
        print(f'Error when buying fetter, possibly a cooldown. Slave: {slave_id}')
    elif response.status_code == 200:
        print(f'Buy fetter: {slave_id}') 
    else:
        print(f'Unknown error. Slave: {slave_id}')
    return response.json()

def buySlave(slave_id):
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/buySlave'
    payload = json.dumps({'slave_id': slave_id})
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0', 
     'content-type':'application/json',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.request('POST', url, headers=headers, data=payload)
    if response.status_code == 422:
        print(f'Error when buying slave, possibly a cooldown. Slave: {slave_id}')
    elif response.status_code == 200:
        print(f'Buy: {slave_id}') 
    else:
        print(f'Unknown error. Slave: {slave_id}')
    return response.json()

def slaveList(user_id):
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/slaveList?id=' + str(user_id)
    payload = {}
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.request('GET', url, headers=headers, data=payload)
    return response.json()['slaves']

def saleSlave(slave_id):
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/saleSlave'
    payload = json.dumps({'slave_id': slave_id})
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0', 
     'content-type':'application/json',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.request('POST', url, headers=headers, data=payload)
    return response.json()

def findSlave(slaves):
    for slave in slaves:
        schedule.run_pending()
        print('Slave:', str(slave['id']).replace('-',''))
        if int(slave['profit_per_min']) * 60 * int(slave['fetter_hour']) > int(slave['fetter_price']):
            if int(myProfile()['me']['balance']) >= int(slave['fetter_price']):
                if int(slave['fetter_to']) == 0:
                    if int(slave['price']) >= min_price:
                        if int(slave['price']) <= max_price:
                            sleep(randint(config["min_delay"],config["max_delay"]))
                            if buy_slave == True:
                               buySlave(int(str(slave['id']).replace('-','')))
                               sleep(randint(config["min_delay"],config["max_delay"]))
                               jobSlave(int(str(slave['id']).replace('-','')))
                               if buy_fetter == True:
                                  sleep(randint(config["min_delay"],config["max_delay"]))
                                  buyFetter(int(str(slave['id']).replace('-','')))
                                  
        if int(slave['slaves_count']) != 0:
            print('findSlave -> ' + str(slave['id']).replace('-',''))
            findSlave(slave['slaves'])

def Profile():
    print('Profile')
    me = myProfile()['me']
    if me['fetter_to'] != 0:
        if me['balance'] >= me['price']:
            if buy_slave == True:
                if int(slave['price']) >= min_price:
                        if int(slave['price']) <= max_price:
                           sleep(randint(config["min_delay"],config["max_delay"]))
                           buySlave(int(str(slave['id']).replace('-','')))
    me = myProfile()['me']
    slaves = myProfile()['slaves']
    for slave in slaves:
        print('Profile -> ' + str(slave['id']).replace('-',''))
        if slave['job']['name'] not in job_name:
            sleep(randint(config["min_delay"],config["max_delay"]))
            jobSlave(int(str(slave['id']).replace('-','')))

        if slave['profit_per_min'] * 60 * slave['fetter_hour'] > slave['fetter_price'] and me['balance'] >= slave['fetter_price'] and slave['fetter_to'] == 0:
            if buy_fetter == True:
                           sleep(randint(config["min_delay"],config["max_delay"]))
                           buyFetter(int(str(slave['id']).replace('-','')))

def ThreadProfile():
    my_thread = threading.Thread(target=Profile)
    my_thread.start()

me = myProfile()['me']
print('Your ID:', str(me['id']), 'Slaves:', str(me['slaves_count']), 'Profit:', str(me['slaves_profit_per_min']))
schedule.every(2).minutes.do(ThreadProfile)

while True:
    try:
        tops = list(topUsers()['list'])
        tops.reverse()
        for top in tops:
            print(top)
            findSlave(slaveList(int(top['id'])))

    except Exception as inst:
        try:
            print(type(inst))
            print(inst.args)
            print(inst)
        finally:
            inst = None
            del inst

