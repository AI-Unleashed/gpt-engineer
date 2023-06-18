import pygame

class GameView:
    def __init__(self, width: int, height: int, cell_size: int):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        pygame.init()
        self.screen = pygame.display.set_mode((width * cell_size, height * cell_size))
        pygame.display.set_caption("Snake")

    def draw(self, snake, food, score):
        self.screen.fill((0, 0, 0))

        for segment in snake.position:
            pygame.draw.rect(self.screen, (255, 255, 255), (*segment, self.cell_size, self.cell_size))

        pygame.draw.rect(self.screen, (255, 0, 0), (*food.position, self.cell_size, self.cell_size))

        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

        pygame.display.flip()
