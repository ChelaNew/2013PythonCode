from grt.mechanism.rollermotor import RollerMotor

class Pickup():

    def __init__(self, roller_motor, raiser_motor):
        self.roller_motor = roller_motor
        self.raiser_motor = raiser_motor

    def pickUp(self, roll_speed, raise_speed):
        #RollerMotor.pickUp(roll_speed, raise_speed)
        self.raiser_motor.set(0.3 * -raise_speed)
        self.roller_motor.set(roll_speed)

    def spitOut(self, roll_speed, raise_speed):
        #RollerMotor.spitOut(roll_speed, raise_speed)
        self.raiser_motor.set(0.3 * -raise_speed)
        self.roller_motor.set(-roll_speed)

    def stop(self):
        self.raiser_motor.set(0)
        self.roller_motor.set(0)