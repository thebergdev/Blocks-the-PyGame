import numpy as np

class My_object:
  def __init__(self, rect, color, visual, solid=True, visible=True, friction=1):
    self.rect = rect
    self.color = color
    self.solid = solid
    self.visible = visible
    self.friction = friction

    self.visual = visual
  
  def run(self):
    if self.visible and self.visual is not None:
      self.visual.draw(self)

class My_object_dynamic(My_object):
  def __init__(self, rect, color, visual, solid, visible, friction, PE, density=1):
    My_object.__init__(self, rect, color, visual, solid, visible, friction)
    self.density = density
    self.velocity = np.array([0, 0])

    self.PE = PE

  def run(self):
    #if PE is not None -> physics (apply gravity and friction, check for hitbox collition. if solid -> handle collition)
    My_object.run(self)

class My_creature(My_object_dynamic):
  def __init__(self, id, rect, color, visual, solid, visible, friction, PE, density, acceleration_x=1, acceleration_y=1, jump_force=1):
    My_object_dynamic.__init__(self, rect, color, visual, solid, visible, friction, PE, density)
    self.id = id
    self.acceleration_x = acceleration_x
    self.acceleration_y = acceleration_y
    self.jump_force = jump_force
  
  def run(self):
    My_object_dynamic.run(self)

  #handle movement

class My_player(My_creature):
  def __init__(self, id, input, rect, color, visual, solid, visible, friction, PE, density, acceleration_x, acceleration_y, jump_force):
    My_creature.__init__(self, id, rect, color, visual, solid, visible, friction, PE, density, acceleration_x, acceleration_y, jump_force)
    self.name = "Player " + str(id)
    self.state = 0

    self.input = input

  def run(self):
    input = input.get()
    #act on input
    My_creature.run(self)
