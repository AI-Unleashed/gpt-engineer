from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Snake:
    position: List[Tuple[int, int]]
    direction: Tuple[int, int]
    size: int

    def move(self):
        head_x, head_y = self.position[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.position.insert(0, new_head)
        self.position.pop()

    def grow(self):
        self.size += 1
        self.position.append(self.position[-1])

    def collides_with_itself(self) -> bool:
        return self.position[0] in self.position[1:]

    def collides_with_boundary(self, width: int, height: int) -> bool:
        head_x, head_y = self.position[0]
        return head_x < 0 or head_x >= width or head_y < 0 or head_y >= height
