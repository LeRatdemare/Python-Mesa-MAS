import mesa
from mesa import space
from agents_classes import *
import numpy as np

class SugarscapeG1mt(mesa.Agent):
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
    self.grid = space.MultiGrid(width=self.width, height=self.height, torus=False)

    # Read in landscape file from supplementary materials
    sugar_distribution = np.genfromtxt("resources/sugar-map.txt")
    print(sugar_distribution.shape)
    print(sugar_distribution[30])

    self.spice = Spice()
    self.sugar = Sugar()
    self.trader = Trader()