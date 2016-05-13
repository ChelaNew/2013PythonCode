from grt.mechanism.flywheels import Flywheel

class Shooter:

    def __init__(self, flywheel_motor1, flywheel_motor2, speed):
        self.flywheel_motor1 = flywheel_motor1
        self.flywheel_motor2 = flywheel_motor2

    def shoot(self, speed):
        self.flywheel_motor1.set(speed)
        self.flywheel_motor2.set(speed)

    def stop(self):
        self.flywheel_motor1.set(0)
        self.flywheel_motor2.set(0)

    def check_speed(self, speed):
        return self.flywheel_motor1.at_speed, self.flywheel_motor2.at_speed

