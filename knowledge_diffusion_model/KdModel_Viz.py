from KdModel import mesa, KdModel
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import *
# from mesa_viz_tornado.ModularVisualization import ModularServer

from student import Student
from visualization_elements import *

def agent_portrayal(agent: Student):
    portrayal = {
        "Shape": "circle",
        "Color": get_agent_color_from_knowledge(agent.get_mean_knowledge()),
        "Filled": "true",
        "Layer": 0,
        "r": 0.5,
    }
    return portrayal

model_params = {
    "width": 20,
    "height": 20,
    "initial_population": Slider("Number of agents", 20, 10, 100, 1),
    "nb_disciplines": NumberInput("Number of disciplines", 4),
    "knowledge_loss": Slider("Knowledge loss", 2, 0, 5, 1),
    "knowledge_gain": Slider("Knowledge gain", 10, 0, 20, 1),
    "study_rate":Slider("Study rate", 0.4, 0, 1, 0.1)
}


########################## Useful Methods


def get_agent_color_from_knowledge(value):
    # Ensure the value is between 0 and 100
    value = max(0, min(value, 100))

    # Calculate the red, green, and blue values
    r = 255 - (value * 255 / 100)
    g = value * 255 / 100

    # Convert the RGB values to a single color code
    color = '#{:02x}{:02x}{:02x}'.format(int(r), int(g), 0)
    return color


########################## CREATE SIMULATION


# Create a CanvasGrid in a 500px * 500px window
canvas_element = CanvasGrid(agent_portrayal, 20, 20, 500, 500)
mean_knowledge_element = AttributeElement("mean_knowledge")

server = ModularServer(KdModel, [canvas_element, mean_knowledge_element], "Knowledge Diffusion Model", model_params)
server.launch()
