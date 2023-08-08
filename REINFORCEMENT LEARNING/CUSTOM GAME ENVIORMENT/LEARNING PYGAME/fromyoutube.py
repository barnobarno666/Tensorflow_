import pymunk 
import pygame
window=pygame.display.set_mode((600,600))
space=pymunk.Space()

class Ball(pygame.sprite.Sprite):
    def __init__(self, space, x, y, radius, image):
        super().__init__()
        self.space = space # pymunk.Space
        self.body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, radius)) # pymunk.Body
        self.body.position = x, y # initial position
        self.shape = pymunk.Circle(self.body, radius) # pymunk.Shape
        self.shape.elasticity = 0.9 # bounce factor
        self.space.add(self.body, self.shape) # add body and shape to space
        self.original_image = image # load image from file
        self.original_image = pygame.transform.smoothscale(self.original_image, (radius * 2, radius * 2)) # scale image to match shape size
        self.image = self.original_image # current image
        self.rect = self.image.get_rect(center=self.body.position) # current rect

    def update(self):
        # update image and rect according to body position and angle
        self.image = pygame.transform.rotate(self.original_image, -self.body.angle * 180 / 3.14)
        self.rect = self.image.get_rect(center=self.body.position)
        window.blit(self.image, self.rect)