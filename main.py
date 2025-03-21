import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from shot import Shot

def main():

    print("Starting Asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    AsteroidField.containers = (updatable)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        updatable.update(dt)
        for ast in asteroids:
            if player.collision_detect(ast):
                print("Game over!")
                sys.exit()
        for thing in drawable:
            thing.draw(screen)

        for ast in asteroids:
            for shot in shots:
                if ast.collision_detect(shot):
                    ast.split()
                    shot.kill()



        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
