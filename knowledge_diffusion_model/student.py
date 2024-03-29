import mesa
from mesa.model import random as mrandom
import numpy as np
from random import randint

class Student(mesa.Agent):
    """
    """
    nb_disciplines = 4
    max_knowledge = 100
    knowledge_loss = 2
    knowledge_gain = 10
    study_rate = 0.4

    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        
        self.pos = pos
        self.knowledge = []
        for i in range(Student.nb_disciplines):
            self.knowledge.append(mrandom.randint(70, Student.max_knowledge+1))

    def step(self):
        # Agent knowledge decreases with time
        for i in range(Student.nb_disciplines):
            self.knowledge[i] -= Student.knowledge_loss
            self.knowledge[i] = max(self.knowledge[i], 0)

        if mrandom.random() < Student.study_rate:
            self.study(randint(0, len(self.knowledge)-1))
        # print(f"{self} -> {self.knowledge}")

    def study(self, discipline):
        self.knowledge[discipline] += Student.knowledge_gain
        self.knowledge[discipline] = min(self.knowledge[discipline], Student.max_knowledge)

    def calculate_next_pos(self) -> tuple:
        # Moves randomly by one cell
        newx = self.pos[0]-1 + randint(0, 2)
        newy = self.pos[1]-1 + randint(0, 2)
        return (newx, newy)

    def get_mean_knowledge(self):
        mean = 0
        for k in self.knowledge:
            mean += k
        mean /= len(self.knowledge)
        return mean

    def __str__(self) -> str:
        return f"Student n°{self.unique_id} {self.pos}"