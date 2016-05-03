from wpilib import Solenoid, Compressor, DriverStation, CANTalon


from grt.sensors.joystick import Attack3Joystick
from grt.sensors.xbox_joystick import XboxJoystick
from grt.sensors.xbox_joystick import XboxJoystick
from grt.sensors.joystick import Joystick
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.shooter import Shooter
from grt.mechanism.pickup import Pickup
from grt.mechanism.belts import Belts
from grt.mechanism.mechcontroller import MechController
from grt.mechanism.beltsmotor import BeltsMotor
from grt.sensors.dummy import Mimic

# DT Stuff

left_motor_front = CANTalon(1)
left_motor_back = CANTalon(2)
right_motor_front = CANTalon(3)
right_motor_back = CANTalon(4)

dt = DriveTrain(left_motor_front, left_motor_back, right_motor_front, right_motor_back,left_shifter=None,
                right_shifter=None, left_encoder=None, right_encoder=None)

ds = DriverStation.getInstance()

# Motor Assignments

flywheel_motor1 = CANTalon(5)
flywheel_motor2 = CANTalon(6)

roller_motor = CANTalon(7)
raiser_motor = CANTalon(8)

belts_motor = CANTalon(10)


# speeds
speed = 0
belt_speed = 0.5


shooter = Shooter(flywheel_motor1, flywheel_motor2, speed)
pickup = Pickup(roller_motor, raiser_motor)
belts = Belts(belt_speed)

joystick = Attack3Joystick(0)
xbox_controller = XboxJoystick(1)
mimic_joystick = Attack3Joystick(3)


mc = MechController(joystick, xbox_controller, pickup, shooter, belts, mimic_joystick)


