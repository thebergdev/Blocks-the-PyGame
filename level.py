class Level:
  def __init__(self, id, payload, goal, static):
      self.id = id
      self.payload = payload #rect
      self.goal = goal #rect
      self.static = static #list of rects
      #self.special = special #list of objects with rect and functions

class Static:
    def __init__(self, rect, color):
        self.rect = rect
        self.color = color

import pygame
import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

payload = pygame.Rect(250+25/2, 750-25-25/2, 25, 25)
goal = pygame.Rect(750, 750-50, 50, 50)
static = []

ground = Static(pygame.Rect(0, 750, 1000, 250), (255, 255, 255))

static.append(ground)

lvl1 = Level(1, payload, goal, static)

with open("lvl1.yml", "w+") as lvl_file:
    cfg = yaml.dump(lvl1, lvl_file)