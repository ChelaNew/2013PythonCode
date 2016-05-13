from grt.sensors.dummy import Mimic

class MechController:

    def __init__(self, joystick, xbox_controller, pickup, shooter, belts, mimic_joystick):

        self.belts = belts
        self.joystick = joystick
        self.xbox_controller = xbox_controller
        self.pickup = pickup
        self.shooter = shooter

        #This adds the listener to mimic joystick, mimic joystick class will then call when state changes
        mimic_joystick.add_listener(self._dummy_vision_listener)

    def _dummy_vision_listener(self, sensor, state_id, datum):
        print(state_id)
        if state_id == "button3":
            if datum:
                self.shooter.shoot(0.5)
                print("x")
        if state_id == "button2":
            if datum:
                self.shooter.stop()
                print("y")
        if state_id == "trigger":
            if datum:
                self.pickup.pickUp(0.5, 0.5)
                print("b")
        if state_id == "button4":
            if datum:
                self.pickup.stop()
                print("a")

    def _xbox_controller_listener(self, sensor, state_id, datum):
        if state_id == "x_button":
            if datum:
                self.shooter.shoot(0.5)
        if state_id == "y_button":
            if datum:
                self.shooter.stop()
        if state_id == "b_button":
            if datum:
                self.pickup.pickUp(0.5, 0.5)
        if state_id == "a_button":
            if datum:
                self.pickup.spitOut(0.5, 0.5)
        if state_id == "r_trigger":
            if datum:
                self.pickup.stop()
        if state_id == "l_trigger":
            if datum:
                self.belts.backwards()
        if state_id == "r_button":
            if datum:
                self.belts.stop()
        if state_id == "l_button":
            if datum:
                self.belts.forewards()

# def _driver_joystick_listener(self, sensor, state_id, datum):




