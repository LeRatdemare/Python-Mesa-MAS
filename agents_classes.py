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


class Spice(mesa.Agent):
  """
  Spice:
  - Containes an amount of spice
  - Grows one amount of spice at each turn
  """

  def __init__(self):
    print("I am a Spice")

class Trader(mesa.Agent):
  """
  Trader:
  - Has a metabolism for sugar and spice
  - Harvest and trade spice to survive and thrive
  """

  def __init__(self):
    print("I am a Trader")