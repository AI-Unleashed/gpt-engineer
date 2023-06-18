from snake import Snake
from food import Food

class GameModel:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.snake = Snake([(width // 2, height // 2)], (1, 0), 3)
        self.food = Food((width // 2 + 3, height // 2))
        self.game_over = False

    def update(self):
        if self.game_over:
            return

        self.snake.move()

        if self.snake.collides_with_itself() or self.snake.collides_with_boundary(self.width, self.height):
            self.game_over = True
            return

        if self.snake.position[0] == self.food.position:
            self.snake.grow()
            self.food.generate_new_position(self.width, self.height)

    def restart(self):
        self.snake = Snake([(self.width // 2, self.height // 2)], (1, 0), 3)
        self.food = Food((self.width // 2 + 3, self.height // 2))
        self.game_over = False
