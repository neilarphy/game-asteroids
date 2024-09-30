import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f'Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")
    clock = pygame.time.Clock()
    dt = 0
   
    g_updatable = pygame.sprite.Group()
    g_drawable = pygame.sprite.Group()
    g_asteroids = pygame.sprite.Group()

    Asteroid.containers = (g_asteroids, g_drawable, g_updatable)
    AsteroidField.containers = (g_updatable)
    Player.containers = (g_updatable, g_drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        # Обработка событий, чтобы можно было выйти из игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        
        for obj in g_updatable:
            obj.update(dt)

        for obj in g_drawable:
            obj.draw(screen)

        # Обновление экрана
        pygame.display.flip()

        
        dt = clock.tick(60) / 1000
    
    pygame.quit()


if __name__ == "__main__":
    main()