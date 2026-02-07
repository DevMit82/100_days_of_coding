import colorgram

colors = colorgram.extract("image.jpg", 85)
lst_colors_tuple = []
for color in colors:
    color = (color.rgb.r, color.rgb.g, color.rgb.b)
    lst_colors_tuple.append(color)

print(lst_colors_tuple)