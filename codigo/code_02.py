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
        print("The light is on")

    def turn_off(self):
        print("The light is off")


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


def main():
    switch = ElectricalPowerSwitch()
    switch.press()
    switch.press()


if __name__ == '__main__':
    main()


