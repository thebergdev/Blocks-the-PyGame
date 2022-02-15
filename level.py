from my_object import My_object, My_object_dynamic, My_creature, My_player

class Level:
  def __init__(self, id, payload, goal, objects):
      self.id = id
      self.payload = payload #object
      self.goal = goal #object
      self.objects = objects #list of objects