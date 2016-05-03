import wpilib


class MyRobot(wpilib.SampleRobot):

    def robotInit(self):
        print("initialize")

    def disabled(self):
        while self.isDisabled():
            print("disabled")

    def autonomous(self):
        while self.isAutonomous() and self.isEnabled():
            print("autonomous")

    def operatorControl(self):
        while self.isOperatorControl() and self.isEnabled():
            print("operator control")


    def safeSleep(self, tinit, duration):
        print("sleeping")


if __name__ == "__main__":
    wpilib.run(MyRobot)
