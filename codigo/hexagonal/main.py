from codigo.hexagonal.app.adapter.fan_repository import Fan
from codigo.hexagonal.app.adapter.light_bulb_repository import LightBulb
from codigo.hexagonal.app.domain.service import ElectricalPowerSwitch


def main():
    light_bulb = LightBulb()
    switch = ElectricalPowerSwitch(light_bulb)
    switch.press()
    switch.press()

    fan = Fan()
    switch = ElectricalPowerSwitch(fan)
    switch.press()
    switch.press()


if __name__ == '__main__':
    main()

