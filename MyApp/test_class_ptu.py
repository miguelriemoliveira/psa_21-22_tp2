#!/usr/bin/env python3
import time
from ClassPTU import ClassPTU
# --------------------------------
# Initialization
# --------------------------------

ptu = ClassPTU()
ptu.connect('/dev/ttyUSB0')

# --------------------------------
# Execution (in cycle)
# --------------------------------
# def sendMsgToPTU(msg_to_send):
#     msg_to_send += '\n'
#     ser.write(msg_to_send.encode())
#     print('Sending msg: ' + msg_to_send)
#     time.sleep(0.02)
#     msg_received = ser.read_until().decode()
#     print('Received msg: ' + msg_received)
#     return msg_received

while True:

    ptu.goal.position.pan = -5000
    ptu.goal.position.tilt = 1500
    ptu.setData()
    for i in range(0,50):
        ptu.getData()
        time.sleep(0.1) # wait

    time.sleep(5) # wait

    ptu.goal.position.pan = 5000
    ptu.goal.position.tilt = -1500
    ptu.setData()
    for i in range(0,50):
        ptu.getData()
        time.sleep(0.1) # wait
    time.sleep(5) # wait


# --------------------------------
# Termination
# --------------------------------

