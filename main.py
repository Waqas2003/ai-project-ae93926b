# file: snakegame/requirements.txt
pygame

# file: snakegame/.gitignore
__pycache__/
venv/

# file: snakegame/snakegame/__init__.py

# file: snakegame/snakegame/models.py
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class SnakeGameModel:
    def __init__(self):
        self.snake_position = [(100, 100), (90, 100), (80, 100)]
        self.apple_position = (200, 200)
        self.direction = Direction.RIGHT
        self.score = 0

    def move_snake(self):
        if self.direction == Direction.UP:
            new_head = (self.snake_position[0][0], self.snake_position[0][1] - 10)
        elif self.direction == Direction.DOWN:
            new_head = (self.snake_position[0][0], self.snake_position[0][1] + 10)
        elif self.direction == Direction.LEFT:
            new_head = (self.snake_position[0][0] - 10, self.snake_position[0][1])
        elif self.direction == Direction.RIGHT:
            new_head = (self.snake_position[0][0] + 10, self.snake_position[0][1])

        self.snake_position.insert(0, new_head)

        if self.snake_position[0] == self.apple_position:
            self.score += 1
        else:
            self.snake_position.pop()

    def change_direction(self, direction):
        if direction == Direction.UP and self.direction != Direction.DOWN:
            self.direction = direction
        elif direction == Direction.DOWN and self.direction != Direction.UP:
            self.direction = direction
        elif direction == Direction.LEFT and self.direction != Direction.RIGHT:
            self.direction = direction
        elif direction == Direction.RIGHT and self.direction != Direction.LEFT:
            self.direction = direction

    def check_collision(self):
        if (self.snake_position[0][0] >= 800 or self.snake_position[0][0] < 0 or
            self.snake_position[0][1] >= 600 or self.snake_position[0][1] < 0):
            return True
        for block in self.snake_position[1:]:
            if self.snake_position[0] == block:
                return True
        return False

# file: snakegame/snakegame/views.py
import pygame
from .models import SnakeGameModel, Direction

class SnakeGameView:
    def __init__(self, model):
        self.model = model
        self.pygame = pygame
        self.pygame.init()
        self.screen = self.pygame.display.set_mode((800, 600))
        self.pygame.display.set_caption('Snake Game')
        self.clock = self.pygame.time.Clock()

    def draw_snake(self):
        for position in self.model.snake_position:
            self.pygame.draw.rect(self.screen, (0, 255, 0), self.pygame.Rect(position[0], position[1], 10, 10))

    def draw_apple(self):
        self.pygame.draw.rect(self.screen, (255, 0, 0), self.pygame.Rect(self.model.apple_position[0], self.model.apple_position[1], 10, 10))

    def draw_score(self):
        font = self.pygame.font.Font(None, 36)
        text = font.render(f'Score: {self.model.score}', True, (0, 0, 0))
        self.screen.blit(text, (10, 10))

    def handle_events(self):
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.pygame.quit()
                quit()
            elif event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_UP:
                    self.model.change_direction(Direction.UP)
                elif event.key == self.pygame.K_DOWN:
                    self.model.change_direction(Direction.DOWN)
                elif event.key == self.pygame.K_LEFT:
                    self.model.change_direction(Direction.LEFT)
                elif event.key == self.pygame.K_RIGHT:
                    self.model.change_direction(Direction.RIGHT)

    def run(self):
        while True:
            self.handle_events()
            self.model.move_snake()
            if self.model.check_collision():
                break
            self.screen.fill((255, 255, 255))
            self.draw_snake()
            self.draw_apple()
            self.draw_score()
            self.pygame.display.update()
            self.clock.tick(10)

# file: snakegame/snakegame/main.py
from .views import SnakeGameView
from .models import SnakeGameModel

def main():
    model = SnakeGameModel()
    view = SnakeGameView(model)
    view.run()

if __name__ == '__main__':
    main()

# file: snakegame/run.py
import snakegame.snakegame.main

snakegame.snakegame.main.main()