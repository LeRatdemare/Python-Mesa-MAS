from KdModel import mesa, KdModel
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
# from mesa_viz_tornado.ModularVisualization import ModularServer

from student import Student
from visualization_elements import *

def agent_portrayal(agent: Student):
    portrayal = {
        "Shape": "circle",
        "Color": get_color(agent.get_mean_knowledge()),
        "Filled": "true",
        "Layer": 0,
        "r": 0.5,
    }
    return portrayal

model_params = {
    "initial_population": {
        "type": "SliderInt",
        "value": 20,
        "label": "Number of agents:",
        "min": 10,
        "max": 100,
        "step": 1,
    },
    "nb_disciplines": {

    },
    "width": 20,
    "height": 20,
}


########################## Useful Methods


def get_color(value):
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

server = ModularServer(KdModel, [canvas_element, mean_knowledge_element], "Knowledge Diffusion Model")
server.launch()
