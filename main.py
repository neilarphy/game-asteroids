import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shot

def display_game_over(screen):
    pygame.font.init()
    font = pygame.font.Font(None, 74)  # Используем шрифт по умолчанию
    text = font.render("Game Over", True, (255, 0, 0))  # Красный текст
    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

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
    g_shots = pygame.sprite.Group()

    Asteroid.containers = (g_asteroids, g_drawable, g_updatable)
    AsteroidField.containers = (g_updatable)
    Player.containers = (g_updatable, g_drawable)
    Shot.containers = (g_shots, g_drawable, g_updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    game_over = False

    while True:
        
        # Обработка событий, чтобы можно было выйти из игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if not game_over:
            screen.fill((0, 0, 0))

            for obj in g_updatable:
                obj.update(dt)
            for obj in g_drawable:
                obj.draw(screen)

            for obj in g_asteroids:
                if obj.is_colliding(player):
                    game_over = True
                    print("Game over!")
                    display_game_over(screen)
                for bullet in g_shots:
                    if obj.is_colliding(bullet):
                        obj.split()
                        bullet.kill()

        # Обновление экрана
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
    pygame.quit()


if __name__ == "__main__":
    main()