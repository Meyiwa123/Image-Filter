from Cimpl import *
from simple_Cimpl_filters import grayscale
import numpy as np

#Function Definitions

# Red Filter
def red_channel(image: Image) -> Image:
    """ 
    Author: Temile Oritsemeyiwa Jordan 101196274
    Return a copy of the original image with a red filter.
    
    >>> image = load_image(choose_file())
    >>> show(red_channel(image))
    """
    new_image = copy(image)
    
    for x, y, (r, g, b) in image:
        red = create_color(r, 0, 0)    
        set_color(new_image, x, y, red)        
    return new_image

# Green Filter
def green_channel(image:Image) -> Image:
    """ 
    Author: Temile Oritsemeyiwa Jordan 101196274
    Returns a copy of the original image with a green filter.
    
    >>> image = load_image(choose_file())
    >>> show(green_channel(image))
    """
    new_image = copy(image)
    
    for x, y, (r, g, b) in image:
        green = create_color(0, g, 0)    
        set_color(new_image, x, y, green)        
    return new_image

# Blue Filter
def blue_channel(image:Image) -> Image:
    """
    Author: Alizee Drolet 101193138
    Returns a copy of the original image with a blue filter.
    
    >>> image = load_image(choose_file())
    >>> show(blue_channel(image))
    """
    new_image = copy(image)
    
    for x, y, (r, g, b) in image:
        blue = create_color(0, 0, b)    
        set_color(new_image, x, y, blue)        
    return new_image  

# Combine Filter
def combine(red_image: Image, green_image: Image, blue_image: Image) -> Image:
    """
    Author: Alizee Drolet 101193138
    Returns an image of the RGB combination of three images. 
    
    >>> red_image = load_image(choose_file())
    >>> green_image = load_image(choose_file())
    >>> blue_image = load_image(choose_file())
    >>> show(combine(red_image, green_image, blue_image))
    """
    new_image = copy(red_image)
    
    for x, y, (r, g, b) in new_image:
        red = get_color(red_image, x, y)
        green = get_color(green_image, x, y)
        blue = get_color(blue_image, x, y)
        set_color(new_image, x, y, create_color(red[0], green[1], blue[2]))
    
    return new_image

# Three-tone Filter
def three_tone(image:Image, color1:str, color2:str, color3:str) -> Image:
    """
    Author: Temile Oritsemeyiwa Jordan 101196274
    Returns a copy of an image with only three colours (tones).
    >>> original_image = load_image(choose_file())
    >>> three_tone(original_image, "black", "gray", "white")
    >>> show(new_image)
    """
    color_name = ["black", "white", "blood", "green", "blue", "lemon", "cyan", "magenta", "gray"]
    color_code = [(0,0,0), (255,255,255), (255,0,0), (0,255,0), (0,0,255), (255,255,0), (0,255,255), (255,0,255), (128,128,128)]
    
    new_image = copy(image)
    for x, y, (r, g, b) in new_image:
        brightness = (r+g+b) // 3 
        if brightness <= 84:
            color = color1
        elif brightness <= 170: 
            color = color2
        elif brightness <= 255:
            color = color3
        
        for element in range(len(color_name)):
            if color == color_name[element]:
                color = color_code[element]        
                
        three_tone_color = create_color(color[0], color[1], color[2])
        set_color(new_image, x, y, three_tone_color)        
        
    return new_image

# Extreme Contrast filter
def extreme_contrast(image: Image) -> Image:
    """ 
    Author: Alizee Drolet 101193138
    Returns a copy of an image in which the contrast between the pixels has been maximized. 
    
    >>> original_image = load_image(choose_file())
    >>> contrast_image = extreme_contrast(original_image)
    >>> show(contrast_image)
    """
    new_image = copy(image)
    
    for x, y, (r, g, b) in new_image:
        color = [r, g, b]
        for index, component in enumerate(color):
            if 0 <= component <= 127:
                component = 0
                
            else:
                component = 255
                
            color[index] = component 
            
        pixel = create_color(color[0], color[1], color[2])
        set_color(new_image, x, y, pixel)
        
    return new_image

# Sepia Tinting filter
def sepia(image: Image) -> Image:
    """ 
    Author: Alizee Drolet 101193138
    Returns a copy of an image where the pixels have been sepia-tinted.
    
    >>> original_image = load_image(choose_file())
    >>> sepia_image = sepia(original_image)
    >>> show(sepia_image)
    """
    new_image = copy(image)
    
    for x, y, (r, g, b) in grayscale(new_image):
        if (r + g + b) > (191 * 3):
            light = create_color((r * 1.08), g, (b * 0.93))
            set_color(new_image, x, y, light)
            
        elif (63 * 3) <= (r + g + b) <= (191 * 3):
            medium = create_color((r * 1.15), g, (b * 0.85))
            set_color(new_image, x, y, medium)
            
        elif (r + g + b) < (63 * 3):
            dark = create_color((r * 1.1), g, (b * 0.9))
            set_color(new_image, x, y, dark)
            
    return new_image

# Posterize filter
def _adjust_component(component: int) -> int:
    """
    Author: Temile Oritsemeyiwa Jordan 101196274
    Returns the midpoint value of the quadrant in which a components lies 
    from the passed value of a pixel's red, green, or blue component.
    
    >>>_adjust_component(190)
    159
    >>> _adjust_component(223)
    223
    """
    if component <= 63:
        midpoint = 31
    elif component <= 127:
        midpoint = 95
    elif component <= 191:
        midpoint = 159        
    else:
        midpoint = 223 
    return midpoint
        
def posterize(image: Image) -> Image:
    """
    Author: Temile Oritsemeyiwa Jordan 101196274
    Returns a posterized filter of the original_image.The filter takes the
    values from the midpoints of the four quadrants and applies them to the image.
    
    >>> original_image = load_image(choose_file())
    >>> posterize_image = posterize(original_image)
    >>> show(posterize_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in new_image:
        mid_red = _adjust_component(r)
        mid_green = _adjust_component(g)
        mid_blue = _adjust_component(b)
        posterize_color = create_color(mid_red, mid_green, mid_blue)
        set_color(new_image, x, y, posterize_color)
    return new_image

# Edge Detection Filter
def detect_edges(image: Image, threshold: int) -> Image:
    """
    Author: Alizee Drolet 101193138
    Returns a copy of an image with an edge detection filter.
    
    >>> original_image = load_image(choose_file())
    >>> edge_image = detect_edges(original_image, 10)
    >>> show(edge_image)
    """
    new_image = copy(image)
    max_height = get_height(new_image)
    white = create_color(255, 255, 255)
    
    for x, y, (r, g, b) in new_image:
        if y < (max_height - 2):
            top_brightness = (r + g + b) // 3
            pixel_color = get_color(new_image, x, (y + 1))
            bottom_brightness = (pixel_color[0] + pixel_color[1] + pixel_color[2]) // 3
            contrast = abs(top_brightness - bottom_brightness)
                
            if contrast > threshold:
                black = create_color(0, 0, 0)
                set_color(new_image, x, y, black)
            
            else:
                set_color(new_image, x, y, white)
                
        else:
            set_color(new_image, x, y, white)
            
    return new_image

# Draw Curve filter
def _interpolation(lst: list) -> list:
    """ 
    Author: Alizee Drolet 101193138
    Returns the coefficients of the interpolating polynomial or the quadratic regression polynomial.
    
    >>> _interpolation([(5, 10), (10, 0), (15, 10)])
    [ 0.4 -8.  40. ]
    >>> _interpolation([(1, 2), (3, 4)])
    [1. 1.]
    >>> _interpolation([(4, 11), (5, 10), (8, 1), (10, 0), (13, 4), (15, 10)])
    [ 0.35650658 -6.97385747 34.33578621]
    """
    x_array = []
    y_array = []
    
    power_4 = []
    power_3 = []
    power_2 = []
    x_2_y = []
    x_y = []
    
    for coords in lst:
        for i in coords:
            if i == coords[0]:
                x_array.append(i)
            else:
                y_array.append(i)
    if len(lst) == 2:
        return np.polyfit(x_array, y_array, 1)
    
    elif len(lst) == 3:
        return np.polyfit(x_array, y_array, 2)
    
    else:
        for i in lst:
            power_4.append(i[0] ** 4)
            power_3.append(i[0] ** 3)
            power_2.append(i[0] ** 2)
                    
            x_2_y.append((i[0] ** 2) * i[1])
            x_y.append(i[0] * i[1])

            
        A = np.array([[sum(power_4), sum(power_3), sum(power_2)], 
                      [sum(power_3), sum(power_2), sum(x_array)], 
                      [sum(power_2), sum(x_array), len(lst)]])
    
        b = np.array([sum(x_2_y), sum(x_y), sum(y_array)])
                
        x = np.linalg.solve(A, b)
        return x
    
def _exhaustive_search(max_x: int, polycoeff: list, val: int) -> int:
    """
    Author: Alizee Drolet 101193138
    Solves f(x)-val=0 for x between 0 and max_x where polycoeff containsthe coefficients of f, 
    using EPSILON of 1 (as we only need ints for pixels).
    Returns None if there is no solution between the bounds.
    
    >>> _exhaustive_search(639,[6.33e-03,-3.80e+00,5.57e+02],0)
    253.0
    >>> _exhaustive_search(639,[7.24e-04,-1.19e+00,4.51e+02],0)
    590.0
    >>> _exhaustive_search(639,[7.24e-04,-1.19e+00,4.51e+02],479)
    None
    """   
    EPSILON = 1
    step = EPSILON / 2
    guess = 0
    
    if len(polycoeff) >= 3:
        equation = (polycoeff[0] * (guess ** 2)) + (polycoeff[1] * guess) + (polycoeff[-1])
        
    else:
        equation = (polycoeff[0] * guess) + (polycoeff[1])
    
    while val == equation:
            return guess        
        
    while val != equation and guess < max_x:
        guess += step 
        
        if len(polycoeff) >= 3:
            equation = (polycoeff[0] * (guess ** 2)) + (polycoeff[1] * guess) + (polycoeff[-1])
        
        else:
            equation = (polycoeff[0] * guess) + (polycoeff[1])
        
        if abs(equation - val) < EPSILON:
            return guess
    
def _image_border_finding(image_size: list, interpolation: list) -> list:
    """ 
    Author: Alizee Drolet 101193138
    Returns the pixels where the curve intersects the border of the image. 
    
    >>> _image_border_finding(dimensions, coefficients)
    """
    # Crosses the vertical border
    f_x0 = np.polyval(interpolation, 0)
    f_x1 = np.polyval(interpolation, (image_size[0] - 1))
    
    # Crosses the horizontal border
    f_y0 = _exhaustive_search(image_size[0] - 1, interpolation, 0)
    f_y1 = _exhaustive_search(image_size[0] - 1, interpolation, image_size[1] - 1)
    
    points = [(0, f_x0), (image_size[0] - 1, f_x1), (f_y0, 0), (f_y1, image_size[1] - 1)]
    
    return points
    
def draw_curve(image: Image, color: str, pointlist: list = None) -> tuple:
    """ 
    Author: Alizee Drolet 101193138
    Returns a tuple containing a new image with a coloured curve on it and a 
    list of points on the border of the image.
    
    >>> original_image = load_image("p2-original.png")
    >>> curve_image = draw_curve(original_image, "cyan", [(1, 2), (3, 4)])
    >>> (<Cimpl.Image object at 0x03EC8A00>, [(0, 1.0), (639, 640.0000000000002), (None, 0), (477.0, 479)])
    """
    new_image = copy(image)
    colors = {"black": [0, 0, 0], "white": [255, 255, 255], "blood": [255, 0, 0], 
               "green": [0, 255, 0], "blue": [0, 0, 255], "lemon": [255, 255, 0], 
               "cyan": [0, 255, 255], "magenta": [255, 0, 255], "gray": [128, 128, 128]}

    # Get dimensions of image
    dimensions = [get_width(new_image), get_height(new_image)]
    
    
    if pointlist == None:
        
        #Notifies the user with dimensions
        print('Width of picture: ', dimensions[0], '\n'+ 'Height of picture:', dimensions[1])
        
        # Number of input points
        print("How many points (pixels' coordinates)? Must be greater than or equal to 2.")
        points = int(input())
    
        # Coordinates of the points
        print("Enter x component and y component")
        point_list = []
    
        for number in range(points):
            print("Coordinate for point", number + 1)
            x_coordinate = input("x component:")
            y_coordinate = input("y component:")
        
            point_list += [(int(x_coordinate), int(y_coordinate))]

        sorted_pointlist = sorted(point_list)
        
    else:
        sorted_pointlist = sorted(pointlist)
        
    # Drawing graph on image
    coefficients = _interpolation(sorted_pointlist)
    rgb = colors.get(color)
    color_of_line = create_color(rgb[0], rgb[1], rgb[2])
    
    for i in range(dimensions[0] - 1):
        power = len(coefficients) - 1
        f_x = 0
        
        for num in coefficients:
            f_x += num * ((i - 1) ** power)
            power -= 1
            
        if 0 <= f_x <= dimensions[1] - 1:
            set_color(new_image, i, int(f_x), color_of_line)
            
            if int(f_x) + 2 < dimensions[1]:
                set_color(new_image, i, int(f_x) + 2, color_of_line)
                
            if int(f_x) + 1 < dimensions[1]:
                set_color(new_image, i, int(f_x) + 1, color_of_line) 
                
            if int(f_x) - 2 >= 0:
                set_color(new_image, i, int(f_x) - 2, color_of_line)            
                
            if int(f_x) - 1 >= 0:
                set_color(new_image, i, int(f_x) - 1, color_of_line)
    
    border_points = _image_border_finding(dimensions, coefficients)            
    
    if pointlist == None:
        return print(new_image, border_points), new_image #not for testing
    else:
        return new_image #for testing

# Flip Image Horizontally filter
def flip_horizontal(image:Image) -> Image:
    """
    Author: Temile Oritsemeyiwa Jordan 101196274
    Returns new_image from a Flipped image along the vertical axis.
    
    >>> original_image = load_image(choose_file())
    >>> flipped_h_image = flip_horizontal(original_image)
    >>> show(flipped_h_image)
    """
    new_image = copy(image)
    width = get_width(new_image)
    height = get_height(new_image)
    
    for x in range(0, width//2):
        for y in range(0, height): 
            left = get_color(new_image, x, y)
            right = get_color(new_image, width - x - 1, y)
            set_color(new_image, x, y, right)
            set_color(new_image, width - x - 1, y, left)
    return new_image

# Flip Image Vertically filter
def flip_vertical(image:Image) -> Image:
    """
    Author: Temile Oritsemeyiwa Jordan 101196274
    Returns new_image from a flipped image along the horizontal axis
    
    >>> original_image = load_image(choose_file())
    >>> flipped_v_image = flip_vertical(original_image)
    >>> show(flipped_v_image)
    """
    new_image = copy(image)
    width = get_width(new_image)
    height = get_height(new_image)
    
    for y in range(0, height//2):
        for x in range(0, width): 
            up = get_color(new_image, x, y)
            down = get_color(new_image, x, height - y - 1)
            set_color(new_image, x, y, down)
            set_color(new_image, x, height - y - 1, up)
    return new_image    
