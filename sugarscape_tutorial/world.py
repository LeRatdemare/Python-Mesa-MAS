import mesa
import mesa.space as mspace
import mesa.time as mtime
from mesa.model import random as mrandom
from agents_classes import *
import numpy as np
import matplotlib.pyplot as plt

class SugarscapeG1mt(mesa.Model):
  '''
  A model class ot  mange Sugarscape with Traders (G1mt)
  form Groing Artificial Societies
  '''
  def __init__(self, width=50, height=50, initial_population=200, endowment_min=25, endowment_max=50,
               metabolism_min=1, metabolism_max=5, vision_min=1, vision_max=5):
    # Initiate width and height of sugarscape
    self.width = width
    self.height = height
    # Initiate population attributes
    self.initial_population = initial_population
    self.endowment_min = endowment_min
    self.endowment_max = endowment_max
    self.metabolism_min = metabolism_min
    self.metabolism_max = metabolism_max
    self.vision_min = vision_min
    self.vision_max = vision_max

    # Initiate mesa grid class
    # See https://github.com/projectmesa/mesa/blame/main/mesa/space.py for world classes
    self.grid = mspace.MultiGrid(width=self.width, height=self.height, torus=False)
    # Initiate schedule
    self.schedule = mtime.RandomActivation(self)
    # Find file here https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/materials
    sugar_distribution = np.genfromtxt("sugarscape_tutorial/resources/sugar-map.txt")
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
    for i in range(self.initial_population):
      # Get agent position
      x = mrandom.randrange(self.width)
      y = mrandom.randrange(self.height)
      # See growing Artificial Societies p. 108 for parameter initialization
      # Give agent initial endowment
      sugar = int(mrandom.uniform(self.endowment_min, self.endowment_max+1))
      spice = int(mrandom.uniform(self.endowment_min, self.endowment_max+1))
      # Give agents initial metabolism
      metabolism_sugar = int(mrandom.uniform(self.metabolism_min, self.metabolism_max+1))
      metabolism_spice = int(mrandom.uniform(self.metabolism_min, self.metabolism_max+1))
      # Give agents initial vision
      vision = int(mrandom.uniform(self.vision_min, self.vision_max+1))
      # Create Trader object
      trader = Trader(agent_id,
                      self,
                      (x,y),
                      moore = False,
                      sugar = sugar,
                      spice = spice,
                      metabolism_sugar = metabolism_sugar,
                      metabolism_spice = metabolism_spice,
                      vision = vision)
      # Place agent
      self.grid.place_agent(trader, (x,y))
      self.schedule.add(trader)

      agent_id += 1
  
  def step(self):
    '''
    Unique step function that does stage activation of sugar and spice
    and then randomly activates traders.
    '''
    for sugar in self.get_agents_by_type(Sugar):
      sugar.step()
    for spice in self.get_agents_by_type(Spice):
      spice.step()

    self.schedule.steps += 1 # Important for data collector to track number of steps
  
  def run_model(self, step_count=1000):
    for i in range(step_count):
      print(i)
      self.step()
  
  def get_agents_by_type(self, agent_type):
        return [agent for agent in self.schedule.agents if type(agent) == agent_type]
