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

  def get_sugar(self, pos):
    '''
    used in self.get_sugar_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Sugar:
        return agent
    return None

  def get_spice(self, pos):
    '''
    used in self.get_spice_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Spice:
        return agent
    return None
  
  def get_sugar_amount(self, pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    sugar_patch = self.get_sugar(pos)
    if sugar_patch:
      return sugar_patch.amount
    return 0

  def get_spice_amount(self, pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    spice_patch = self.get_spice(pos)
    if spice_patch:
      return spice_patch.amount
    return 0
  
  def is_occupied_by_other(self, pos):
    '''
    Helper function part 1 of self.move()
    '''
    if pos == self.pos:
      # Agent's position is considered unoccupied as agent can stay here
      return False
    this_cell = self.model.grid.get_cell_list_contents(pos)
    for a in this_cell:
      # See if occupied by another agent
      if isinstance(a, Trader):
        return True
    return False

  def calculate_welfare(self, sugar, spice):
    '''
    helper function part 2 self.move()
    '''
    m_total = self.metabolism_sugar + self.metabolism_spice
    # Cobb-douglas function form
    return sugar**(self.metabolism_sugar/m_total) * spice**(self.metabolism_spice/m_total)

  def move(self):
    '''
    Function for trader agent to identify optimal move for each step in 4 parts
    1 - Identify all possible moves
    2 - Determine which move maximizes welfare
    3 - Find closest best option
    4 - Move
    '''
  
    # 1 - Identify all possible moves
    neighbors = [i
                 for i in self.model.grid.get_neighborhood(
                   self.pos, self.moore, True, self.vision
                ) if not self.is_occupied_by_other(i)]
    print(self.pos, neighbors)
    # 2 - Determine which move maximizes welfare
    welfares = [
      self.calculate_welfare(
        self.sugar + self.get_sugar_amount(pos),
        self.spice + self.get_spice_amount(pos))
      for pos in neighbors
    ]
    print(welfares)