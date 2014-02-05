import serial
port=8
ser=None
def setup(port=port):
    global ser
    ser=serial.Serial(port,baudrate=9600)