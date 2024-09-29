import pygame
from constants import *

def main():
    print(f'Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")


    running = True
    while running:
        screen.fill((0, 0, 0))

        # Обновление экрана
        pygame.display.flip()

        # Обработка событий, чтобы можно было выйти из игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



if __name__ == "__main__":
    main()