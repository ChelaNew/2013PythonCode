from grt.mechanism.rollermotor import RollerMotor

class Pickup():

    def __init__(self, roller_motor, raiser_motor):
        self.roller_motor = roller_motor
        self.raiser_motor = raiser_motor

    def pickUp(self, roll_speed, raise_speed):
        RollerMotor.pickUp(roll_speed, raise_speed)

    def spitOut(self, roll_speed, raise_speed):
        RollerMotor.spitOut(roll_speed, raise_speed)