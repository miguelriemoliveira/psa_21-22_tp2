from abc import ABC, abstractmethod


class ClassAbstractHardware(ABC):

    def __init__(self):
        self.is_connected = False

    def connect(self, device):
        if self.is_connected:
            print('Hardware already connected. Cannot reconnect!')
            return False

        if self._connect(device):
            self.is_connected = True
            return True
        else:
            return False

    @abstractmethod
    def _connect(self, device):
        return

    def disconnect(self):
        if not self.is_connected:
            print('Hardware already disconnected. Cannot disconnect!')
            return False

        if self._disconnect():
            self.is_connected = False
            return True
        else:
            return False

    @abstractmethod
    def _disconnect(self):
        return

    def getData(self):
        if not self.is_connected:
            print('Cannot get data. Hardware disconnected!')
            return False

        return self._getData()

    @abstractmethod
    def _getData(self):
        return

    def setData(self):
        if not self.is_connected:
            print('Cannot set data. Hardware disconnected!')
            return False

        return self._setData()

    @abstractmethod
    def _setData(self):
        return
