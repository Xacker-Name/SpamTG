from telethon import TelegramClient, events, sync
import os
import time
import config
from config import *
namber = 0



client = TelegramClient('session_name', config.api_id, config.api_hash)

client.start()
os.system('cls' if os.name == 'nt' else 'clear')




print("""
Скрипт был исправлен t.me/Xacker_Name
Так же поситите магазин t.me/eze_pokupka3_BOT


 [1] Бесконечный флуд 
 [2] Флуд с указанным количеством сообщений
 [3] Флуд с списком пользователей
""")


a = input(' Выберите способ флуда:')

if a == "1":
    print(" ")
    print(" ")
    idp = input("Введите nick через @ человека: ")
    mes = input("Текст сообщения: ")
    client.start()
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Спам начат!')
    print('Телеграм канал: https://t.me/Skript_Browser_Automation_Studio')
    print('Добавил дополнения к срипту https://t.me/Xacker_Name')
    print('Спасибо что используешь мои скрипты)')
    while True:

       client.send_message(idp, mes,)
       namber = namber +1
       print([namber], "Сообщение отправлено ему", idp, "Подпишись https://t.me/Skript_Browser_Automation_Studio") 
       time.sleep(0.5)
       
       

     

elif a == "2":
    print(" ")
    print(" ")  
    px = int(input(" Cообщений: "))
    idp = input(" Введите nick через @ человека: ")
    mes = input(" Текст сообщения: ")
    

    client.start()
    os.system('cls' if os.name == 'nt' else 'clear')
    

    print('Спам начат!')
    print('Телеграм канал: https://t.me/Skript_Browser_Automation_Studio')
    print('Добавил дополнения к срипту https://t.me/Xacker_Name')
    print('Спасибо что используешь мои скрипты)')
    for i in range(px):
        client.send_message(idp, mes,)
        namber = namber +1
        print([namber], "Сообщение отправлено ему", idp, "Подпишись https://t.me/Skript_Browser_Automation_Studio") 
        time.sleep(0.5)      

elif a == "3":
    print(" ")
    print(" ")  
    px = int(input(" Cообщений: "))
    print("""
     [1] 2 чата 
     [2] 3 чата     
     [3] 4 чата
""")
    nn = input(" Выберите способ: ")
    if nn == "1":  
        idp = input(" Введите nick через @ первого человека: ")
        idg = input(" Введите nick через @ второго человека: ")
        mes = input(" Текст сообщения: ")
        client.start()
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Спам начат!')
        print('Телеграм канал: https://t.me/Skript_Browser_Automation_Studio')
        print('Добавил дополнения к срипту https://t.me/Xacker_Name')
        print('Спасибо что используешь мои скрипты)')
        for i in range(px):
            client.send_message(idp, mes);
            namber = namber +1 
            print([namber], "Сообщение отправлено ему", idp, "Подпишись https://t.me/Skript_Browser_Automation_Studio")             
            time.sleep(0.5)
            client.send_message(idg, mes); 
            print([namber], "Сообщение отправлено ему", idg, "Подпишись https://t.me/Skript_Browser_Automation_Studio") 
            time.sleep(0.5)
           
    elif nn == "2":  
        idp = input(" Введите nick через @ первого человека: ")
        idg = input(" Введите nick через @ второго человека: ")
        idh = input(" Введите nick через @ третьего человека: ")
        mes = input(" Текст сообщения: ")
        client.start()
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Спам начат!')
        print('Телеграм канал: https://t.me/Skript_Browser_Automation_Studio')
        print('Добавил дополнения к срипту https://t.me/Xacker_Name')
        print('Спасибо что используешь мои скрипты)')
        
        for i in range(px):
            client.send_message(idp, mes);
            namber = namber +1
            print([namber], "Сообщение отправлено ему", idp, "Подпишись https://t.me/Skript_Browser_Automation_Studio") 
            time.sleep(0.5)
            client.send_message(idg, mes);
            print([namber], "Сообщение отправлено ему", idg, "Подпишись https://t.me/Skript_Browser_Automation_Studio") 
            time.sleep(0.5)
            client.send_message(idh, mes); 
            print([namber], "Сообщение отправлено ему", idh, "Подпишись https://t.me/Skript_Browser_Automation_Studio") 
            time.sleep(0.5)

    elif nn == "3":  
        idp = input(" Введите nick через @ первого человека: ")
        idg = input(" Введите nick через @ второго человека: ")
        idh = input(" Введите nick через @ третьего человека: ")
        ida = input(" Введите nick через @ четвёртого человека: ")
        mes = input(" Текст сообщения: ")
        client.start()
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Спам начат!')
        print('Телеграм канал: https://t.me/Skript_Browser_Automation_Studio')
        print('Добавил дополнения к срипту https://t.me/Xacker_Name')
        print('Спасибо что используешь мои скрипты)')
        
        for i in range(px):
            client.send_message(idp, mes); 
            namber = namber +1
            print([namber], "Сообщение отправлено ему", idp, "Подпишись https://t.me/Skript_Browser_Automation_Studio") 
            time.sleep(0.5)
            client.send_message(idg, mes); 
            print([namber], "Сообщение отправлено ему", idg, "Подпишись https://t.me/Skript_Browser_Automation_Studio") 
            time.sleep(0.5)
            client.send_message(idh, mes); 
            print([namber], "Сообщение отправлено ему", idh, "Подпишись https://t.me/Skript_Browser_Automation_Studio") 
            time.sleep(0.5)
            client.send_message(ida, mes); 
            print([namber], "Сообщение отправлено ему", ida, "Подпишись https://t.me/Skript_Browser_Automation_Studio") 
            time.sleep(0.5)
else:
    print(" Нету такого ")