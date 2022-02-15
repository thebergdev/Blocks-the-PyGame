import pygame
import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

id = 2
payload = My_object(pygame.Rect(250+25/2, 750-25-25/2, 25, 25), (0, 0, 255), solid=False)
goal = My_object(pygame.Rect(750, 750-50, 50, 50), (0, 0, 255), solid=False)
objects = []

ground = My_object(pygame.Rect(0, 750, 1000, 250), (255, 255, 255))

objects.append(ground)

lvl = Level(id, payload, goal, objects)

with open("lvl" + str(id) + ".yml", "w+") as lvl_file:
    cfg = yaml.dump(lvl, lvl_file)