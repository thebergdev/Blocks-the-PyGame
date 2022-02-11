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