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


class ElectricalPowerSwitch:

    def __init__(self):
        self.light_bulb = LightBulb()
        self.on = False

    def press(self):
        if self.on:
            self.light_bulb.turn_off()
            self.on = False
        else:
            self.light_bulb.turn_on()
            self.on = True


if __name__ == '__main__':
    switch = ElectricalPowerSwitch()
    switch.press()
    switch.press()
