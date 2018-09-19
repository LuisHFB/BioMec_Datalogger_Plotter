import serial
import numpy as np
import matplotlib.pyplot as plt
from drawnow import drawnow
import time
import csv
import datetime
import keyboard

dataArray = np.zeros((2,), dtype=float)
dataArray2 = np.zeros((2,), dtype=float)
dataArray3 = np.zeros((2,), dtype=float)
Eletro = []
cnt = 0
e = 0
rodando = True
RR = 0
FC= 0

arduinoPort = 'COM3'
arduinoBaud = '19200'

arduinoData = serial.Serial(arduinoPort,arduinoBaud)
plt.ion()
time.sleep(2)

def makeFig():
    plt.ylim(0,500)
    plt.xlim(e,e+70)
    plt.grid(True)
    plt.title('ECG')
    plt.ylabel('')
    plt.xlabel('T(s)')
    plt.plot(Eletro,'ro-')
    plt.show(block=False)
    plt.text(0.3, 0.85, 'RR= '+ str(RR), fontsize=14, transform=plt.gcf().transFigure)
    plt.text(0.7, 0.85, 'FC= '+ str(FC), fontsize=14, transform=plt.gcf().transFigure)
    
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
        if "#" in arduinoData.read().decode('windows-1252'):
            arduinoString = arduinoData.readline(-1)
            dataArray = arduinoString.decode('windows-1252').split(',')
        
            ecg = dataArray[0].replace('#', '')
            a = float(ecg)       
            Eletro.append(a)
             
            with open("test_data.csv","a",newline='') as f:
                writer = csv.writer(f,delimiter=";",quotechar='"', quoting=csv.QUOTE_ALL)
                writer.writerow([str(datetime.datetime.now().strftime('%H:%M:%S.%f')),a])
                drawnow(makeFig)
                plt.pause(.000001)
                cnt=cnt+1
                if cnt>=70:
                    e = e+1
            
        elif "R" in arduinoData.read().decode('windows-1252'):
            arduinoString = arduinoData.readline(-1)
            dataArray2 = arduinoString.decode('windows-1252').split(',')
        
            RR = dataArray2[0].replace('R', '')

            
        elif "F" in arduinoData.read().decode('windows-1252'):
            arduinoString = arduinoData.readline(-1)
            dataArray3 = arduinoString.decode('windows-1252').split(',')
        
            FC = dataArray3[0].replace('F', '')
        
        else:
            True
    break