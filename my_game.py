#game logic class

from my_visual import My_visual
import pygame
import yaml

class My_game:
    def __init__(self):
        self.running = False

        try:
            from yaml import CLoader as Loader, CDumper as Dumper
        except ImportError:
            from yaml import Loader, Dumper

        # Open config.yml
        with open("config.yml", "r") as config_file:
            cfg = yaml.load(config_file, Loader=Loader)

        # Use cfg
        self.HEIGHT = cfg["height"]
        self.WIDTH = cfg["width"]
        self.LEVEL = cfg["level"]
        self.PLAYER_SPEED = cfg["player-speed"]
        self.payload_color = cfg["payload-color"]
        self.goal_color = cfg["goal-color"]

        #init pygame
        self.pygame = pygame
        self.pygame.init()

        #init visual
        self.visual = My_visual(self.pygame, self.HEIGHT, self.WIDTH, (0, 0, 0))

    def load_level(self, level):
        try:
            from yaml import CLoader as Loader, CDumper as Dumper
        except ImportError:
            from yaml import Loader, Dumper

        # Load level
        with open(level + ".yml", "r") as lvl_file:
            self.level = yaml.load(lvl_file, Loader=Loader)
        
        self.objects = []
        self.objects.append(self.level.payload)
        self.objects.append(self.level.goal)
        for obj in self.level.objects:
            self.objects.append(obj)
        for obj in self.objects:
            obj.visual = self.visual

    def start(self):
        level = "lvl2" # HARDCODED FOR NOW
        self.load_level(level)
        self.running = True

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.visual.fill()
        for obj in self.objects:
            obj.run()
        self.visual.flip()

    def quit(self):
        self.pygame.quit()