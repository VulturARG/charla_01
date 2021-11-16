class LightBulb:
    def turn_on(self):
        print("The light is on")

    def turn_off(self):
        print("The light is off")


class ElectricalPowerSwitch:

    def __init__(self, light_bulb: LightBulb) -> None:
        self.light_bulb = light_bulb
        self.on = False

    def press(self):
        if self.on:
            self.light_bulb.turn_off()
            self.on = False
        else:
            self.light_bulb.turn_on()
            self.on = True


def main():
    light_bulb = LightBulb()
    switch = ElectricalPowerSwitch(light_bulb)
    switch.press()
    switch.press()


if __name__ == '__main__':
    main()


