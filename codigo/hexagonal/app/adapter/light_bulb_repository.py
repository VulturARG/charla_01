from codigo.hexagonal.app.domain.switchable_repository import Switchable


class LightBulb(Switchable):
    def turn_on(self) -> bool:
        print("Connecting with the device...")
        print("The light is on")
        return True

    def turn_off(self) -> bool:
        print("The light is off")
        print("Disconnecting with the device...")
        return False
