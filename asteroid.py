from circleshape import CircleShape
import pygame
import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_ast1_angle = self.velocity.rotate(random_angle)
        new_ast2_angle = self.velocity.rotate(-random_angle)
        new_ast_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast1 = Asteroid(self.position[0], self.position[1], new_ast_radius)
        new_ast2 = Asteroid(self.position[0], self.position[1], new_ast_radius)
        new_ast1.velocity = new_ast1_angle * 1.2
        new_ast2.velocity = new_ast2_angle * 1.2
