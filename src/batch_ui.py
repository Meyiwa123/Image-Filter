from image_filters import *

# Function Definitions
def _execute_command(command: list) -> None:
    """
    Saves the image of the execution of the given command list
    in the form:[image, new_image_file, filter_list]
    
    >>> _execute_command(command)
    """
    image_name = command[0] 
    image = load_image(image_name)
    
    filename = command[1]
    
    filter_list = command[-1]

    for name in filter_list:
        
        if name == "3":
            image = three_tone(image, "blood", "lemon", "gray")

        elif name == "X":
            image = extreme_contrast(image)
        
        elif name == "T":
            image = sepia(image)

        elif name == "P":
            image = posterize(image)

        elif name == "E":
            image = detect_edges(image, 15)

        elif name == "V":
            image = flip_vertical(image)

        elif name == "H":
            image = flip_horizontal(image)

    saved = save_as(image, filename)
    
    return saved

def batch_image() -> None:
    """
    Rearranges the inputted batch and calls _execute_command. 
    
    >>> batch_image()
    """
    filename = input("Enter name of the batch file: ")
    batch_file = open(filename)

    for line in batch_file:
        items = line.split(" ")
        command = [items[0], items[1]]
        items.pop(0)
        items.pop(0)
        for element in items:
            if element == ' ':
                items.pop(element)
                
        command.append(items)
        
        result = _execute_command(command)
    
    return result

# Main Script
batch_image()

