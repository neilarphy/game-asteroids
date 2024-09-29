import pygame
from constants import *
from player import Player

def main():
    print(f'Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        # Обработка событий, чтобы можно было выйти из игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)   
        screen.fill((0, 0, 0))
        player.draw(screen)
        # Обновление экрана
        pygame.display.flip()

        
        dt = clock.tick(60) / 1000
    
    pygame.quit()


if __name__ == "__main__":
    main()