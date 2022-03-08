import unittest
from unittest.mock import Mock

from codigo.hexagonal.app.domain.service import ElectricalPowerSwitch
from codigo.hexagonal.app.domain.switchable_repository import Switchable


class TestSwitchable(unittest.TestCase):
    def test_device_is_on(self):

        repository = Mock(spec=Switchable)
        service = ElectricalPowerSwitch(repository)

        # values returned by the repository
        repository.turn_on.return_value = True

        actual = service.press()
        expected = True
        self.assertEqual(expected, actual)

    def test_device_is_off(self):

        repository = Mock(spec=Switchable)
        service = ElectricalPowerSwitch(repository)

        # values returned by the repository
        repository.turn_on.return_value = True
        repository.turn_off.return_value = False

        service.press()
        actual = service.press()
        expected = False
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
