import mesa
import numpy as np
import matplotlib.pyplot as plt

class Student(mesa.Agent):
    """
    """
    
    def __init__(self, nb_disciplines, max_knowledge=100):
        self.knowledge = []
        for i in range(nb_disciplines):
            self.knowledge.append(mesa.model.random.randint(0, max_knowledge+1))
            

class Kd_mas(mesa.Model):
    """
    """
    
    def __init__(self):
        pass

model = Kd_mas()