from abc import ABC, abstractmethod


class Switchable(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("Connecting with the device...")
        print("The light is on")

    def turn_off(self):
        print("The light is off")
        print("Disconnecting with the device...")


class Fan(Switchable):
    def turn_on(self):
        print("Connecting with the device...")
        print("The fan is on")

    def turn_off(self):
        print("The fan is off")
        print("Disconnecting with the device...")


class ElectricalPowerSwitch:

    def __init__(self, switchable: Switchable) -> None:
        self.switchable = switchable
        self.on = False

    def press(self):
        if self.on:
            self.switchable.turn_off()
            self.on = False
        else:
            self.switchable.turn_on()
            self.on = True


if __name__ == '__main__':
    light_bulb = LightBulb()
    switch = ElectricalPowerSwitch(light_bulb)
    switch.press()
    switch.press()

    fan = Fan()
    switch = ElectricalPowerSwitch(fan)
    switch.press()
    switch.press()
