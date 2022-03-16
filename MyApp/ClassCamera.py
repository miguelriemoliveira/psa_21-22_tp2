import cv2

from ClassAbstractHardware import ClassAbstractHardware

class ClassCamera(ClassAbstractHardware):

    def __init__(self):
        super().__init__() # call super class constructor
        self.image = None

    def _connect(self, device):
        self.video_capture = cv2.VideoCapture(device)  # define a video capture object
        return True

    def _disconnect(self):
        self.video_capture.release()
        return True

    def _getData(self):
        success, self.image = self.video_capture.read()  # Capture the video frame
        return success

    def _setData(self):
        print('Cannot write to camera!')
        return False
