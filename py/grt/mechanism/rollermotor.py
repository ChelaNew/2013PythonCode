

class RollerMotor:

    raise_speed = 1
    roll_speed = 1

    def __init__(self, roller_motor, raiser_motor):
        self.roller_motor = roller_motor
        self.raiser_motor = raiser_motor


    def raiseUp(self, raise_speed):
        self.raiser_motor.set(raise_speed)

    def lower(self, raise_speed):
        self.raiser_motor.set(-raise_speed)

    def pickUp(self, roll_speed, raise_speed):
        self.raiser_motor.set(0.3 * -raise_speed)
        self.roller_motor.set(roll_speed)

    def spitOut(self, roll_speed, raise_speed):
        self.raiser_motor.set(0.3 * -raise_speed)
        self.roller_motor.set(-roll_speed)

