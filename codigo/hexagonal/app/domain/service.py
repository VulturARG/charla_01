from codigo.hexagonal.app.domain.switchable_repository import Switchable


class ElectricalPowerSwitch:

    def __init__(self, switchable: Switchable) -> None:
        self.switchable = switchable
        self.on = False

    def press(self) -> bool:
        if self.on:
            self.switchable.turn_off()
            self.on = False
        else:
            self.switchable.turn_on()
            self.on = True

        return self.on
