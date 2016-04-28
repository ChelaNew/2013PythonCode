import wpilib


class MyRobot(wpilib.SampleRobot):
    def __init__(self):
        #initialize variables

    def disabled(self):
        #run when robot is disabled

    def autonomous(self):
        #run during autonomous period

    def operatorControl(self):
        #run during tele-op period

    def safeSleep(self, tinit, duration):
        #run when robot is sleeping


if __name__ == "__main__":
    wpilib.run(MyRobot)
