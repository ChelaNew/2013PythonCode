
class DriveTrain:

    power = 1.0

    def __init__(self,left_motor_front, left_motor_back, right_motor_front, right_motor_back,left_shifter=None,
                 right_shifter=None,left_encoder=None, right_encoder=None):
        self.left_motor_front = left_motor_front
        self.left_motor_back = left_motor_back
        self.right_motor_front = right_motor_front
        self.right_motor_back = right_motor_back
        self.left_shifter = left_shifter
        self.right_shifter = right_shifter
        self.left_encoder = left_encoder
        self.right_encoder = right_encoder
        self.dt_left = self.left_motor_front = left_motor_back
        self.dt_right = self.right_motor_front = right_motor_back

    def set_left_motors(self, power):
        self.left_motor_front.set(power)
        self.left_motor_back.set(power)

    def set_right_motors(self, power):
        self.right_motor_front.set(power)
        self.right_motor_back.set(power)


