import serial
import time
import csv

Temp = []
Press1 = []
Press2 = []

arduinoPort = 'COM4'
arduinoBaud = '9600'


arduinoData = serial.Serial(arduinoPort,arduinoBaud)
time.sleep(2)

while True:
    while (arduinoData.inWaiting()==0):
        pass
    while True:
        if "#" in arduinoData.read().decode():
            arduinoString = arduinoData.readline(-1)
            dataArray = arduinoString.decode().split(',')
        
            T = dataArray[0].replace('#', '')
            P1 = dataArray[1]
            P2 = dataArray[2] 
        
            Temp.append(T)
            Press1.append(P1)
            Press2.append(P2)
            
            with open("test_data.csv","a",newline='') as f:
                writer = csv.writer(f,delimiter=";",quotechar='"', quoting=csv.QUOTE_ALL)
                writer.writerow([time.time(),T,P1,P2])
        else:
            True