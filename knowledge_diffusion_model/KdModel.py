import mesa
from mesa.model import random as mrandom
import numpy as np
from random import randint

from student import Student

class KdModel(mesa.Model):
    """
    """
    
    def __init__(self, width=20, height=20, initial_population=20, nb_disciplines=4):
        # Initiate width and height of world
        self.width = width
        self.height = height
        # Initiate mesa grid class
        self.grid = mesa.space.MultiGrid(width=self.width, height=self.height, torus=True)
        # Initiate schedule
        self.schedule = mesa.time.RandomActivationByType(self)
        # Initiate DataCollector and data visualization attr
        self.datacollector = mesa.DataCollector({"agents_count":len(self.schedule.agents)})
        self.mean_knowledge = 0
        # Initiate population attributes
        Student.nb_disciplines = nb_disciplines
        Student.max_knowledge = 100
        Student.knowledge_loss = 2

        for i in range(initial_population):
            pos = (randint(0, width-1), randint(0, height-1))
            student = Student(i, self, pos)
            self.schedule.add(student)
            self.grid.place_agent(student, student.pos) # TODO Edit with random coords
        # TODO Use numpy for initial agents distribution
        
    def step(self):
        # Prepare data
        self.mean_knowledge = 0
        student_shuffle = list(self.schedule.agents_by_type[Student].values())
        mrandom.shuffle(student_shuffle)
        for student in student_shuffle:
            student.step()
            # Make the agent move
            new_pos = self.grid.torus_adj(student.calculate_next_pos())
            self.pos = new_pos
            self.grid.move_agent(student, new_pos)
            # Update model data
            self.mean_knowledge += student.get_mean_knowledge()
        self.mean_knowledge /= len(student_shuffle)
        # Step forward
        self.schedule.steps += 1

    def run_model(self, step_count=1000):
        for i in range(step_count):
            print("Step n°", i)
            self.step()