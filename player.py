from datetime import datetime
from turtle import speed

class Player:
  def __init__(self, id, color, rect, speed):
      self.id = id
      self.color = color
      self.rect = rect
      self.action = [0, 0]
      self.speed = speed