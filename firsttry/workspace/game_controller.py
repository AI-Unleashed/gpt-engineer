import pygame
from game_model import GameModel
from game_view import GameView

class GameController:
    def __init__(self):
        self.model = GameModel(20, 20)
        self.view = GameView(20, 20, 20)
        self.clock = pygame.time.Clock()

    def handle_key_press(self, key):
        if key == pygame.K_UP:
            self.model.snake.direction = (0, -1)
        elif key == pygame.K_DOWN:
            self.model.snake.direction = (0, 1)
        elif key == pygame.K_LEFT:
            self.model.snake.direction = (-1, 0)
        elif key == pygame.K_RIGHT:
            self.model.snake.direction = (1, 0)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    self.handle_key_press(event.key)
                    if event.key == pygame.K_r and self.model.game_over:
                        self.model.restart()

            self.model.update()
            self.view.draw(self.model.snake, self.model.food, self.model.snake.size)
            self.clock.tick(10)
