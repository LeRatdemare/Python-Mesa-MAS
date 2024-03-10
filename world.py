import mesa
import mesa.space as mspace
import mesa.time as mtime
from agents_classes import *
import numpy as np
import matplotlib.pyplot as plt

class SugarscapeG1mt(mesa.Model):
  '''
  A model class ot  mange Sugarscape with Traders (G1mt)
  form Groing Artificial Societies
  '''
  def __init__(self, width=50, height=50):
    # Initiate width and height of sugarscape
    self.width = width
    self.height = height
    # Initiate mesa grid class
    # See https://github.com/projectmesa/mesa/blame/main/mesa/space.py for world classes
    self.grid = mspace.MultiGrid(width=self.width, height=self.height, torus=False)
    # Initiate schedule
    self.schedule = mtime.RandomActivation(self)

    # Find file here https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/materials
    sugar_distribution = np.genfromtxt("resources/sugar-map.txt")
    spice_distribution = np.flip(sugar_distribution, 1)
    
    # Printing distributions
    # im = plt.imshow(sugar_distribution, origin="lower")
    # plt.colorbar(im)
    # plt.show()

    agent_id = 0
    for (_, x, y) in self.grid.coord_iter():
      max_sugar = sugar_distribution[x, y]
      if max_sugar > 0:
        sugar = Sugar(agent_id, self, (x,y), max_sugar)
        self.grid.place_agent(sugar, (x,y))
        self.schedule.add(sugar)
        agent_id += 1
      
      max_spice = spice_distribution[x, y]
      if max_spice > 0:
        spice = Spice(agent_id, self, (x,y), max_spice)
        self.grid.place_agent(spice, (x,y))
        self.schedule.add(spice)
        agent_id += 1
    print(self.schedule.agents)