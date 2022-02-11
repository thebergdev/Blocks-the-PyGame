from datetime import datetime
from turtle import speed

class Player:
  def __init__(self, id, color, rect, speed):
      self.id = id
      self.color = color
      self.rect = rect
      self.action = [0, 0]
      self.speed = speed
      self.payload = False
      self.goal = False
      self.dead = False

  def load_payload(self):
    if self.payload:
      return False
    else:
      self.payload = True
      print("Payload True")
      return True
    

  def enter_goal(self):
    if self.payload:
      self.goal = True
      print("Goal True")
      return True
    else:
      return False
  
  def reset(self, x, y):
    self.payload = False
    self.goal = False
    self.rect.x = x
    self.rect.y = y