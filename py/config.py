from wpilib import Solenoid, Compressor, DriverStation, CANTalon


from grt.sensors.joystick import Attack3Joystick
from grt.mechanism.drivecontroller import ArcadeDriveController
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
from wpilib import Talon
from grt.core import SensorPoller


# DT Stuff

left_motor_front = Talon(4)
left_motor_back = Talon(3)
right_motor_front = Talon(1)
right_motor_back = Talon(2)

dt = DriveTrain(left_motor_front, left_motor_back, right_motor_front, right_motor_back,left_shifter=None,
                right_shifter=None, left_encoder=None, right_encoder=None)

# initialize driver station
ds = DriverStation.getInstance()

# Motor Assignments

flywheel_motor1 = Talon(9)
flywheel_motor2 = Talon(10)

roller_motor = Talon(7)
raiser_motor = Talon(8)

# belts_motor = Talon(?) not connected


# speeds
speed = 0
belt_speed = 0.5


shooter = Shooter(flywheel_motor1, flywheel_motor2, speed)
pickup = Pickup(roller_motor, raiser_motor)
belts = Belts(belt_speed)

joystick = Attack3Joystick(0)
xbox_controller = XboxJoystick(1)
mimic_joystick = Attack3Joystick(3)

hid_sp = SensorPoller((joystick, xbox_controller,mimic_joystick))

ac = ArcadeDriveController(dt, joystick)
mc = MechController(joystick, xbox_controller, pickup, shooter, belts, mimic_joystick)




