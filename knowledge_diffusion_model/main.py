import mesa
from mesa.model import random as mrandom
import numpy as np
import matplotlib.pyplot as plt

class Student(mesa.Agent):
    """
    """
    
    def __init__(self, unique_id, model, nb_disciplines, max_knowledge=100):
        super().__init__(unique_id, model)
        self.knowledge = []
        for i in range(nb_disciplines):
            self.knowledge.append(mrandom.randint(0, max_knowledge+1))


class Kd_mas(mesa.Model):
    """
    """
    
    def __init__(self, width=50, height=50, initial_population=200, nb_disciplines=4):
        # Initiate width and height of world
        self.width = width
        self.height = height
        # Initiate mesa grid class
        self.grid = mesa.space.MultiGrid(width=self.width, height=self.height, torus=True)
        # Initiate schedule
        self.schedule = mesa.time.RandomActivationByType(self)
        # Initiate population attributes
        self.students = []
        for i in range(initial_population):
            student = Student(i, self, nb_disciplines, 100)
            self.students.append(student)
            self.schedule.add(student)
            self.grid.place_agent(student, 0, 0) # TODO Edit with random coords
        # TODO Use numpy for initial agents distribution
        
        def step(self):
            # TODO
            pass

        def run_model(self, step_count=1000):
            for i in range(step_count):
                print("Step n°", i)
                self.step()

model = Kd_mas(10, 4)