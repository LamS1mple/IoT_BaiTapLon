import serial
import time

arduino = serial.Serial(port='COM5',  baudrate=115200, timeout=.1)
arduino.readline()

def write_read(x):
    s = x +'\r'
    arduino.write(str(s).encode())
    time.sleep(0.05)
    data = arduino.readline()
    return  data


# while True:
#     value  = write_read('1').decode()
    
#     print(value.strip('\n') == "Mo1")
    # if value.decode() == "Mo1\n":
    #     print(1)
