import cv2
import pygame

from ClassAbstractHardware import ClassAbstractHardware

class ClassGamePad(ClassAbstractHardware):

    def __init__(self):
        super().__init__() # call super class constructor
        self.axis0 = None
        self.axis1 = None

    def _connect(self, device):
        pygame.init()
        pygame.joystick.init()  # Initialize the joysticks.

        # Get count of joysticks.
        joystick_count = pygame.joystick.get_count()
        print('Number of joysticks ' + str(joystick_count))
        if joystick_count < 1:
            print('Did not find any joystick. Cannot connect!')
            return False

        # Assuming that we have only one joystick connected
        self.joystick = pygame.joystick.Joystick(device)

        # Get the name from the OS for the controller/joystick.
        name = self.joystick.get_name()
        print('Connected to joystick named ' + name)
        return True

    def _disconnect(self):
        pygame.quit()
        return True

    def _getData(self):
        self.axis0 = self.joystick.get_axis(0)
        self.axis1 = self.joystick.get_axis(1)
        pygame.event.pump()
        return True

    def _setData(self):
        print('Cannot write to camera!')
        return False
