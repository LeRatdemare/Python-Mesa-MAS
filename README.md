# Mesa Tutorial


## Visualization

### Agents Portrayal

The KdModel_Viz.py uses a *agent_portrayal* method to represent an agent on the UI. This method takes an agent as an argument and returns a dict with the following keys describing how the agent will be drawn.<br>
Source page [here](https://mesa.readthedocs.io/en/main/modular-visualization.html).

- "Shape": Can be "circle", "rect" or "arrowHead"
    - For Circles:
        - "r": The radius, defined as a fraction of cell size. r=1 will fill the entire cell.
    - For rectangles:
        - "w", "h": The width and height of the rectangle, which are in fractions of cell width and height.
    - For arrowHead:
        - "scale": Proportion scaling as a fraction of cell size.
        - "heading_x": represents x direction unit vector.
        - "heading_y": represents y direction unit vector.
- "Color": The color to draw the shape in; needs to be a valid HTML color, e.g."Red" or "#AA08F8"
- "Filled": either "true" or "false", and determines whether the shape is filled or not.
- "Layer": Layer number of 0 or above; higher-numbered layers are drawn above lower-numbered layers.
- "text": Text to overlay on top of the shape. Normally, agent's unique_id is used .
- "text_color": Color of the text overlay.

(Shapes also have "x" and "y" coordinates, for the x and y of the grid cell in which it is, but CanvasGrid adds those automatically).

## Resources
- Youtube [tutorial](https://www.youtube.com/watch?v=fUrUWnWGHEQ&list=PLF0b3ThojznRpQOd7iFukqXybbMV_vwZn&index=1) followed for this project
- Super [documentation](https://mesa.readthedocs.io/en/latest/apis/time.html) for Mesa library
- Visualization [CanvasGrid](https://mesa.readthedocs.io/en/main/tutorials/adv_tutorial_legacy.html)
