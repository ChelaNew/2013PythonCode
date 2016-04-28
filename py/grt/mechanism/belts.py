from grt.mechanism.beltsmotor import BeltsMotor

class Belts:

    def __init__(self,belt_speed):
        self.belt_speed = belt_speed

    def forewards(self,belt_speed):
        BeltsMotor.moveUp(belt_speed)

    def backwards(self,belt_speed):
        BeltsMotor.moverDown(belt_speed)

    def stop(self, belt_speed):
        BeltsMotor.stopBelt(belt_speed)
