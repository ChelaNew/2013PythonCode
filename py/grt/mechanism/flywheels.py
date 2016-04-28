import wpilib


class Flywheel:

    speed = 0

    def __init__(self, flywheel_motor1, flywheel_motor2):
        self.flywheel_motor1 = flywheel_motor1
        self.flywheel_motor2 = flywheel_motor2

    def setSpeed(self, speed):
        self.flywheel_motor1.set(speed)
        self.flywheel_motor1.set(speed)

    def stopSpinning(self):
        self.flywheel_motor1.set(0)
        self.flywheel_motor2.set(0)