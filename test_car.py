import keyboard
import serial
import time


#### Must be change to suitable port [Bluetooth Outgoing]
ser = serial.Serial("COM5", 9600, timeout = 1)

print('connected')
st = 0.2    # Sleep Time

while(True):
    if keyboard.is_pressed('w'):
        print("forward")
        ser.write(b'1')
        time.sleep(st)
    elif keyboard.is_pressed('s'):
        print("backward")
        ser.write(b'2')
        time.sleep(st)
    elif keyboard.is_pressed('a'):
        print("left")
        ser.write(b'3')
        time.sleep(st)
    elif keyboard.is_pressed('d'):
        print("right")
        ser.write(b'4')
        time.sleep(st)
    elif keyboard.is_pressed('i'):
        print("Straight Speed Up")
        ser.write(b'5')
        time.sleep(st)
    elif keyboard.is_pressed('k'):
        print("Straight Speed Down")
        ser.write(b'6')
        time.sleep(st)
    elif keyboard.is_pressed('o'):
        print("Turn Speed Up")
        ser.write(b'7')
        time.sleep(st)
    elif keyboard.is_pressed('l'):
        print("Turn Speed Down")
        ser.write(b'8')
        time.sleep(st)
    else:
        print('nope')
        ser.write(b'0')
        time.sleep(st)
