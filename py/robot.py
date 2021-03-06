import wpilib
import time
import threading
from queue import Queue
from wpilib import Preferences


class MyRobot(wpilib.SampleRobot):
    def __init__(self):
        super().__init__()

        import config
        self.hid_sp = config.hid_sp
        self.ds = config.ds


    def disabled(self):
        while self.isDisabled():
            tinit = time.time()
            self.hid_sp.poll()
            self.safeSleep(tinit, .04)

    def autonomous(self):
        pass

    def operatorControl(self):

        while self.isOperatorControl() and self.isEnabled():
            tinit = time.time()
            self.hid_sp.poll()
            self.safeSleep(tinit, .04)

    def safeSleep(self, tinit, duration):
        tdif = .04 - (time.time() - tinit)
        if tdif > 0:
            time.sleep(tdif)
        if tdif <= 0:
            print("Code running slowly!")


if __name__ == "__main__":
    wpilib.run(MyRobot)
