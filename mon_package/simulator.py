from dataclasses import dataclass

from .boat import Boat

@dataclass
class Simulator:
    nom: str
    boat: Boat

    def __str__(self):

        return f"Je suis un {self.__class__.__name__}, je simule {self.boat}"

