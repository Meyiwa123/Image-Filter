# Image Filter (1.0)

## Description
The Image Filter Program is a versatile tool that enables users to enhance their images by applying a wide range of filters. Whether working with .jpg or .png files, users can load their chosen image into the program and effortlessly apply various filters to modify the appearance. Once the desired adjustments are made, the program allows users to conveniently save the edited image to a file and view the final result.

The program includes the following eight filters:
* 3-tone (3)
* Extreme Contrast (X)
* Sepia Tinting (T)
* Posterize (P\)
* Edge Detection (E)
* Draw Curve (D)
* Vertical Flip (V)
* Horizontal Flip (H)
 
## Dependency
To run the program, you will need the following dependencies:
* Wing 101 Version 7.2.4.0
* Pillow (version 20.3.3 or higher)
* Cimpl.py (version 1.04)
* image_filters.py (version 1.0)

## Usage
The Image Filter Program offers two usage options: batch_ui and interactive_ui. In batch_ui, users can perform batch processing by providing a .txt file with a list of commands. It's important to note that the 3-tone filter uses "blood," "lemon," and "gray" as the three tones. Additionally, the Edge Detection filter has a threshold value of 15. Draw Curve filter is not available for batch_ui. In interactive_ui, users can interactively load an image and apply filters. Commands can be entered in uppercase, lowercase, or a combination of both. The Draw Curve filter uses the curve color "cyan." Users can save the filtered image by entering "S" and quit the program by entering "Q".

### Batch UI
1. Create a .txt file and put the name of the image to be filtered, filename when saved, and consecutive commands of filters all in one line, separated by a space.
2. Run the program and enter the name of the .txt file containing the commands.
3. A new file with the desired name containing the filtered image should appear in the file app.
```
image1.jpg test1 3 X V
image2.jpg test2 E S T
```

### Interactive UI
1. Run the program and load an image by entering "L".
2. Enter the command for the desired filter.
3. Close the appeared image to enter a new command.
4. Save the filtered image by entering "S."
5. Quit the program by entering "Q."
```python
>>> L)oad image  S)ave-as 
>>> 3)-tone  X)treme contrast  T)int sepia  P)osterize 
>>> E)dge detect  D)raw curve  V)ertical flip  H)orizontal flip 
>>> Q)uit

>>> : L

>>> L)oad image  S)ave-as 
>>> 3)-tone  X)treme contrast  T)int sepia  P)osterize 
>>> E)dge detect  D)raw curve  V)ertical flip  H)orizontal flip 
>>> Q)uit

>>> : v

>>> L)oad image  S)ave-as 
>>> 3)-tone  X)treme contrast  T)int sepia  P)osterize 
>>> E)dge detect  D)raw curve  V)ertical flip  H)orizontal flip 
>>> Q)uit

>>> : Q
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
