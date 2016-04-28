

class BeltsMotor:

    def __init__(self, belts_motor, belt_speed):
        self.belts_motor = belts_motor
        self.belts_speed = belt_speed

    def moveUp(self, belt_speed):
        self.belts_motor.set(belt_speed)

    def moverDown(self, belt_speed):
        self.belts_motor.set(-belt_speed)

    def stopBelt(self):
        self.belts_motor.set(0)