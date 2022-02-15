#visualization class
import pygame
from my_object import My_object

class My_visual:
  def __init__(self, pygame, height, width, default_fill_color=(0, 0, 0)):
    self.pygame = pygame
    self.default_fill_color = default_fill_color

    self.screen = self.pygame.display.set_mode([height, width])
    self.screen.fill(self.default_fill_color)

  def fill(self, color=None):
    if color is None:
      color = self.default_fill_color
    self.screen.fill(color)

  def draw(self, object):
    self.pygame.draw.rect(self.screen, object.color, object.rect)

  def flip(self):
    self.pygame.display.flip()