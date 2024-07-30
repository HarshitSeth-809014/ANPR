import serial
from time import sleep

print("Connecting to Arduino....")
arduinoData = serial.Serial('COM4', 19200)

def set_barrier():
    arduinoData.write("GON\r".encode())
    sleep(1)
    arduinoData.write("OPEN\r".encode())

    arduinoData.write("GOF\r".encode())
    pass
    

def check_barrier_button():
    data = ""
    while True: 
        arduinoData.write("RON\r".encode())
        while(arduinoData.inWaiting() > 0):
            data = arduinoData.readline()
            data = str(data, 'utf-8')
            if(data.startswith("B")):
                arduinoData.write("ROF\r".encode())
                set_barrier()
                break
        if(data.startswith("B")):
            break    


def check_image_button():
    while True:
        while(arduinoData.inWaiting() > 0):
            data = arduinoData.readline()
            data = str(data, 'utf-8')
            if(data.startswith("I")):
                return True
