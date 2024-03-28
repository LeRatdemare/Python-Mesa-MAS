from mesa.visualization.modules import TextElement

class AttributeElement(TextElement):
    def __init__(self, attr_name):
        '''
        Create a new text attribute element.

        Args:
            attr_name: The name of the attribute to extract from the model.

        Example return: "happy: 10"
        '''
        self.attr_name = attr_name

    def render(self, model):
        val = getattr(model, self.attr_name)
        return self.attr_name + ": " + str(val)