import time

import serial
from ClassAbstractHardware import ClassAbstractHardware


class PanTilt():
    def __init__(self):
        self.pan = None
        self.tilt = None


class PositionSpeed():
    def __init__(self):
        self.position = PanTilt()
        self.speed = PanTilt()


class ClassPTU(ClassAbstractHardware):

    def __init__(self):
        super().__init__()  # call super class constructor
        self.goal = PositionSpeed()
        self.current = PositionSpeed()
        self.previous_msg = ''

    def _connect(self, device):
        self.serial = serial.Serial()  # configuration of the serial port
        self.serial.port = device
        self.serial.baudrate = 38400
        self.serial.parity = serial.PARITY_NONE
        self.serial.stopbits = 1
        self.serial.bytesize = 8
        self.serial.xonxoff = False
        self.serial.rtscts = False
        self.serial.dsrdtr = False
        self.serial.timeout = 1
        self.serial.open()  # open the port

        msg_to_send = 'ED\n'
        self.serial.write(msg_to_send.encode())
        msg_to_send = 'TS2000\n'
        self.serial.write(msg_to_send.encode())

        return True

    def _disconnect(self):
        self.serial.close()
        return True

    def _getData(self):

        msg_to_send = 'PP\n'
        self.serial.write(msg_to_send.encode())
        msg_to_send = 'TP\n'
        self.serial.write(msg_to_send.encode())
        msg_to_send = 'PS\n'
        self.serial.write(msg_to_send.encode())
        msg_to_send = 'TS\n'
        self.serial.write(msg_to_send.encode())

        time.sleep(0.01)

        data_received = self.serial.read_all().decode()
        # print('data received:\n' + data_received + '\n\n')

        data_received = self.previous_msg + data_received



        msgs_received = data_received.split('\n')
        self.previous_msg = msgs_received[-1]
        # print('msgs received:\n' + str(msgs_received) + '\n\n')

        for msg_received in msgs_received:
            msg_received = msg_received.strip('\r')
            # print('Analysing msg_received: ' + msg_received)

            if 'Current Pan position is' in msg_received:
                # print('This is a pan position msg')
                self.current.position.pan =  self.findNumberInText(msg_received)

            elif 'Current Tilt position is' in msg_received:
                # print('This is a tilt position msg')
                self.current.position.tilt = self.findNumberInText(msg_received)

            elif 'Target Pan speed is' in msg_received:
                # print('This is a pan speed msg')
                self.current.speed.pan =  self.findNumberInText(msg_received)

            elif 'Target Tilt speed is' in msg_received:
                # print('This is a tilt speed msg')
                self.current.speed.tilt = self.findNumberInText(msg_received)


        print('Current ptu state:')
        print('current.position.pan = ' + str(self.current.position.pan))
        print('current.position.tilt = ' + str(self.current.position.tilt))
        print('current.speed.pan = ' + str(self.current.speed.pan))
        print('current.speed.tilt = ' + str(self.current.speed.tilt))

        return True


    def findNumberInText(self, text):
        # print('text to find number: ' + text)
        words = text.split(' ')
        # print('words:' + str(words))

        for word in words:

            try:
                number = int(word)
                # print('word ' + word  + ' is a number!')
                return number
            except:
                # print('word ' + word  + ' is NOT a number!')
                pass

        return None

    def _setData(self):
        msg_to_send = 'PP' +  str(self.goal.position.pan) + '\n'
        self.serial.write(msg_to_send.encode())
        msg_to_send = 'TP' +  str(self.goal.position.tilt) + '\n'
        self.serial.write(msg_to_send.encode())

        return False
