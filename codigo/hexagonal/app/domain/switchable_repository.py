from abc import ABC, abstractmethod


class Switchable(ABC):

    @abstractmethod
    def turn_on(self) -> bool:
        """Turn on the element."""

    @abstractmethod
    def turn_off(self) -> bool:
        """Turn off the element."""
