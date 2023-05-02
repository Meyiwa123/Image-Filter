from image_filters import *

# Function Definitions 
def _display_menu() -> str:
    """
    Prints a string of options. 
    
    >>> L)oad image  S)ave-as 
    >>> 3)-tone  X)treme contrast  T)int sepia  P)osterize 
    >>> E)dge detect  D)raw curve  V)ertical flip  H)orizontal flip 
    >>> Q)uit
    """
    return print("L)oad image  S)ave-as \n3)-tone  X)treme contrast  T)int sepia  P)osterize \nE)dge detect  D)raw curve  V)ertical flip  H)orizontal flip \nQ)uit") 
    
def get_command() -> None:
    """
    Prompts the user for a command.
    
    >>> get_command()
    >>> L)oad image  S)ave-as 
    >>> 3)-tone  X)treme contrast  T)int sepia  P)osterize 
    >>> E)dge detect  D)raw curve  V)ertical flip  H)orizontal flip 
    >>> Q)uit
    >>>
    >>> : 
    """
    command = "\n: "
    image = 0
    
    while command != "Q":
        _display_menu()
    
        command = input("\n: ").upper()
    
        if command == "L" :
            image = load_image(choose_file())
            
        elif command == "Q":
            return None        
        
        elif image == 0:
            print("No image loaded")
        
        elif command == "3":
            image = three_tone(image, "blood", "lemon", "gray")
            show(image)
        
        elif command == "X":
            image = extreme_contrast(image)
            show(image)
        
        elif command == "T":
            image = sepia(image)
            show(image)
        
        elif command == "P":
            image = posterize(image)
            show(image)
        
        elif command == "E":
            threshold = input("Threshold? ")
            image = detect_edges(image, int(threshold))
            show(image)
        
        elif command == "D":
            return_draw = draw_curve(image, "cyan")
            image = return_draw[-1]
            show(image)
        
        elif command == "V":
            image = flip_vertical(image)
            show(image)
        
        elif command == "H":
            image = flip_horizontal(image)
            show(image)
        
        elif command == "S":
            save_as(image)

        elif command != "Q":
            print("No such command")
     
# Main Script       
get_command()