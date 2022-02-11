def play(player, delta_time):
    player.rect.x += (delta_time * player.speed * player.action[1]) / 100
    if player.rect.left < 0: player.rect.left = 0
    elif player.rect.right > WIDTH: player.rect.right = WIDTH

# Simple pygame program

# Import and initialize
from player import Player
import pygame
import yaml
import level
from datetime import datetime

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# Open config.yml
with open("config.yml", "r") as config_file:
    cfg = yaml.load(config_file, Loader=Loader)

# Use cfg
HEIGHT = cfg["height"]
WIDTH = cfg["width"]
LEVEL = cfg["level"]
PLAYER_SPEED = cfg["player-speed"]
payload_color = cfg["payload-color"]
goal_color = cfg["goal-color"]

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([HEIGHT, WIDTH])

# Load level
with open(LEVEL + ".yml", "r") as lvl_file:
    level = yaml.load(lvl_file, Loader=Loader)

# Players
player1 = Player(1, (255, 0, 0), pygame.Rect(500, 750-50, 50, 50), PLAYER_SPEED)

# Run until the user asks to quit
running = True
last_timestamp = datetime.now()
while running:
    delta_time = (datetime.now() - last_timestamp).microseconds
    if delta_time > 1000:
        last_timestamp = datetime.now()
        # Resets player input
        player1.action = [0, 0]

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Checking pressed keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player1.action[0] = 1
            #print("UP pressed")
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            player1.action[1] = 0
            #print("RIGHT and LEFT pressed")
        elif keys[pygame.K_LEFT]:
            player1.action[1] = -1
            #print("LEFT pressed")
        elif keys[pygame.K_RIGHT]:
            player1.action[1] = 1
            #print("RIGHT pressed")

        
        # Players play
        play(player1, delta_time)

        # Fill the background with white
        screen.fill((0, 0, 0))

        ### Draw level

        # Draw payload
        pygame.draw.rect(screen, payload_color, level.payload)

        # Draw goal
        pygame.draw.rect(screen, goal_color, level.goal)
        
        # Draw static
        for static in level.static:
            pygame.draw.rect(screen, static.color, static.rect)

        # Draw players
        pygame.draw.rect(screen, player1.color, player1.rect)

        # Flip the display
        pygame.display.flip()

# Done! Time to quit.
pygame.quit()

