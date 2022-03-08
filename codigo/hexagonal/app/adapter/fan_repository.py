from codigo.hexagonal.app.domain.switchable_repository import Switchable


class Fan(Switchable):
    def turn_on(self) -> bool:
        print("Connecting with the device...")
        print("The fan is on")
        return True

    def turn_off(self) -> bool:
        print("The fan is off")
        print("Disconnecting with the device...")
        return False

