#!/usr/bin/env python3
import time

import serial

# --------------------------------
# Initialization
# --------------------------------

# configuration of the serial port
ser = serial.Serial()
ser.port = '/dev/ttyUSB0'
ser.baudrate = 9600
ser.parity = serial.PARITY_NONE
ser.stopbits  = 1
ser.bytesize = 8
ser.xonxoff = False
ser.rtscts = False
ser.dsrdtr = False
ser.timeout = 1

# open the port
ser.open()

# Set pan speed to 5000
msg_to_send = 'PS5000\n'
ser.write(msg_to_send.encode())

# --------------------------------
# Execution (in cycle)
# --------------------------------
def sendMsgToPTU(msg_to_send):
    msg_to_send += '\n'
    ser.write(msg_to_send.encode())
    print('Sending msg: ' + msg_to_send)
    time.sleep(0.02)
    msg_received = ser.read_until().decode()
    print('Received msg: ' + msg_received)
    return msg_received

while True:

    sendMsgToPTU('PP5000')
    sendMsgToPTU('TP500')
    time.sleep(5) # wait
    sendMsgToPTU('PP-5000')
    sendMsgToPTU('TP-2500')
    time.sleep(5) # wait


# --------------------------------
# Termination
# --------------------------------

ser.close()