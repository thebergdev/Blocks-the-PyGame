import numpy as np

class My_object:
  def __init__(self, rect, color, solid=True, visible=True):
    self.rect = rect
    self.color = color
    self.solid = solid
    self.visible = visible
  
  ###run
  #if visible -> draw object

class My_object_dynamic(My_object):
  def __init__(self, rect, color, solid=True, visible=True, density=1):
    My_object.__init__(self, rect, color, solid, visible)
    self.density = density
    self.velocity = np.array([0, 0])

  ###run
  #physics (check for hitbox collition. if solid -> handle collition)
  #run child

class My_creature(My_object_dynamic):
  def __init__(self, id, acceleration_x, acceleration_y, jump_force, rect, color, solid=True, visible=True, density=1):
    My_object_dynamic.__init__(self, rect, color, solid, visible, density)
    self.id = id
    self.acceleration_x = acceleration_x
    self.acceleration_y = acceleration_y
    self.jump_force = jump_force
  
  ###run
  #run child

class My_player(My_creature):
  def __init__(self, id, acceleration_x, acceleration_y, jump_force, rect, color, solid=True, visible=True, density=1):
    My_creature.__init__(self, id, acceleration_x, acceleration_y, jump_force, rect, color, solid, visible, density)
    self.name = "Player " + str(id)
    self.state = 0
    self.input = [0, 0, 0]

  ###run
  #recieve input
  #act on input
  #run child
