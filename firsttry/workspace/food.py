import random
from dataclasses import dataclass

@dataclass
class Food:
    position: tuple[int, int]

    def generate_new_position(self, width: int, height: int):
        self.position = (random.randint(0, width - 1), random.randint(0, height - 1))
