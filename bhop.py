import pymem                   # pip install pymem
import pymem.process           # Устанавливается вместе с модулем 'pymem'
import requests                # pip install requests
from threading import Thread   # Модуль установлен по умолчанию
import keyboard                # pip install keyboard
import time                    # Модуль установлен по умолчанию


print ('>>> Запускается чит...')

# < Подключаемся к игре >

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

print ('')

# < Получаем оффсеты >
print ('>>> Получение оффсетов...')

offsets = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
response = requests.get(offsets).json()

dwLocalPlayer = int(response["signatures"]["dwLocalPlayer"])
dwForceJump = int(response["signatures"]["dwForceJump"])

m_fFlags = int(response["netvars"]["m_fFlags"])

print ('')
print ('>>> Запуск BunnyHop...')

# < Запускаем функцию >

def BunnyHop():
    while True:
        if pm.read_int(client + dwLocalPlayer):
            player = pm.read_int(client + dwLocalPlayer)
            force_jump = client + dwForceJump
            on_ground = pm.read_int(player + m_fFlags)

            if keyboard.is_pressed("space"):
                if on_ground == 257:
                    pm.write_int(force_jump, 5)
                    time.sleep(0.17)
                    pm.write_int(force_jump, 4)

# < Запускаем функцию в мультипоток >
Thread(target=BunnyHop).start()

print ('')
print ('>>> BunnyHop запущен.')