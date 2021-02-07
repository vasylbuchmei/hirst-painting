### Extracting color from the image using cologram ###
import colorgram
colors = colorgram.extract("image.jpg", 30)
color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)
