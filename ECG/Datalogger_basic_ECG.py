import serial
import numpy as np
import matplotlib.pyplot as plt
from drawnow import drawnow
import time
import csv
import datetime
import keyboard

dataArray = np.zeros((2,), dtype=float)
Eletro = []
cnt = 0
e = 0
rodando = True

arduinoPort = 'COM4'
arduinoBaud = '9600'

arduinoData = serial.Serial(arduinoPort,arduinoBaud)
plt.ion()
time.sleep(2)

def makeFig():
    plt.ylim(0,10)
    plt.xlim(e,e+50)
    plt.grid(True)
    plt.title('ecg')
    plt.ylabel('')
    plt.xlabel('T(s)')
    plt.plot(Eletro,'ro-')
    plt.show(block=False)
    
while rodando:
    while (arduinoData.inWaiting()==0):
        pass
    while rodando:
        try:
            if keyboard.is_pressed('Esc'):
                rodando = False
            else:
                pass
        except:
            break
        if "#" in arduinoData.read().decode():
            arduinoString = arduinoData.readline(-1)
            dataArray = arduinoString.decode().split(',')
        
            ecg = dataArray[0].replace('#', '')
            a = float(ecg)       
            Eletro.append(a)
            
            with open("test_data.csv","a",newline='') as f:
                writer = csv.writer(f,delimiter=";",quotechar='"', quoting=csv.QUOTE_ALL)
                writer.writerow([str(datetime.datetime.now().strftime('%H:%M:%S.%f')),a])
            drawnow(makeFig)
            plt.pause(.000001)
            cnt=cnt+1
            if cnt>=50:
                e = e+1
                           
        else:
            True
    break