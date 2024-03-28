from KdModel import mesa, KdModel
from mesa.visualization.modules import CanvasGrid
from mesa_viz_tornado.ModularVisualization import ModularServer

def agent_portrayal(agent):
    portrayal = {
        "Shape": "circle",
        "Color": "blue",
        "Filled": "true",
        "Layer": 0,
        "r": 0.5,
    }
    return portrayal

# model_params = {
#     "initial_population": {
#         "type": "SliderInt",
#         "value": 20,
#         "label": "Number of agents:",
#         "min": 10,
#         "max": 100,
#         "step": 1,
#     },
#     "nb_disciplines": {

#     },
#     "width": 50,
#     "height": 50,
# }

# Create a CanvasGrid in a 500px * 500px window
canvas_element = CanvasGrid(agent_portrayal, 50, 50, 500, 500)

server = ModularServer(KdModel, [canvas_element], "Knowledge Diffusion Model")
server.launch()
