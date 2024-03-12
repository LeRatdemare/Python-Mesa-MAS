import mesa

class Sugar(mesa.Agent):
  """
  Sugar:
  - Containes an amount of sugar
  - Grows one amount of sugar at each turn
  """

  def __init__(self, unique_id, model, pos, max_sugar):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_sugar
    self.max_sugar = max_sugar
  def step(self):
    '''
    Sugar Growth funtion, adds one unit of sugar each step until
    max amount 
    '''
    self.amount = min([self.max_sugar, self.amount+1])

class Spice(mesa.Agent):
  """
  Spice:
  - Containes an amount of spice
  - Grows one amount of spice at each turn
  """

  def __init__(self, unique_id, model, pos, max_spice):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_spice
    self.max_spice = max_spice
  
  def step(self):
    '''
    Spice growth function, adds one unit of
    Spice each step until max amount
    '''
    self.amount = min([self.max_spice, self.amount+1])


class Trader(mesa.Agent):
  """
  Trader:
  - Has a metabolism for sugar and spice
  - Harvest and trade spice to survive and thrive
  """

  def __init__(self, unique_id, model, pos, moore=False, sugar=0,
               spice=0, metabolism_sugar=0, metabolism_spice=0,
               vision=0):
    super().__init__(unique_id, model)
    self.pos = pos
    self.moore = moore
    self.sugar = sugar
    self.spice = spice
    self.metabolism_sugar = metabolism_sugar
    self.metabolism_spice = metabolism_spice
    self.vision = vision
  def move(self):
    '''
    Function for trader agent to identify optimal move for each step in 4 parts
    1 - Identify all possible moves
    2 - Determine which move maximize welfare
    3 - Find closest best option
    4 - Move
    '''
    
    # 1 - Identify all possible moves
    # neighbors = [i
    #              for i in self.model.grid.get_neighborhood(
                   
    # )]
    pass