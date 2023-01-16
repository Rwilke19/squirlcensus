import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = data["Primary Fur Color"]
black = 0
cinnamon = 0
gray = 0
for hue in color:
    if hue == "Gray":
        gray = gray + 1
    if hue == "Cinnamon":
        cinnamon = cinnamon + 1
    if hue == "Black":
        black = black + 1

new_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray, cinnamon, black]
}

color_cvs = pandas.DataFrame(new_dict)
color_cvs.to_csv("Color.csv")