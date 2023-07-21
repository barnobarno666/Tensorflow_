import pygame
import pymunk
from pymunk.body import Body
import pymunk.pygame_util
from random import randint

pygame.init()

WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))


def draw(space, window, draw_options):
    window.fill((255, 255, 255))
    space.debug_draw(draw_options)
    pygame.display.update()


def create_boundaries(space, width, height):
    rects = [
        [(width / 2, height - 10), (width, 20)],
        [(width / 2, 10), (width, 20)],
        [(10, height / 2), (20, height)],
        [(width - 10, height / 2), (20, height)],
    ]

    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 1
        shape.friction = 0.5
        space.add(body, shape)


class Ball(pygame.sprite.Sprite):
    def __init__(self, space, x, y, radius, image_path):
        super().__init__()
        self.space = space
        self.body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, radius))
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = 0.9
        self.space.add(self.body, self.shape)

        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.smoothscale(self.original_image, (radius * 2, radius * 2))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=self.body.position)

    def update(self):
        self.image = pygame.transform.rotate(self.original_image, -self.body.angle * 180 / 3.14)
        self.rect = self.image.get_rect(center=self.body.position)


def run(window, width, height):
    run = True
    clock = pygame.time.Clock()
    fps = 60

    space = pymunk.Space()
    space.gravity = (0, 98)

    boundaries = create_boundaries(space, width, height)

    draw_options = pymunk.pygame_util.DrawOptions(window)

    image_path = "enemy.png"
    ball = Ball(space, 100, 200, 50, image_path)
    sprites = pygame.sprite.Group()
    sprites.add(ball)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for ball in sprites:
            ball.update()

        window.fill((255, 255, 255))
        sprites.draw(window)
        pygame.display.update()
        
        space.step(1 / fps)
        
        draw(space, window, draw_options)
        clock.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)
