"""Common utility functions shared across classes"""

def convert_layers_to_string(layers: list) -> str:
    """Given Card or View layers, convert the grid layers to a string"""
    string_conversion = ""
    for layer in layers:
        string_conversion += "\n" + "".join(layer)
    return string_conversion