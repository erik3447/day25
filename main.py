import pandas

pd = pandas.read_csv("Squirrel.csv")

grey = len(pd[pd["Primary Fur Color"] == "Gray"])

red = len(pd[pd["Primary Fur Color"] == "Cinnamon"])

black = len(pd[pd["Primary Fur Color"] == "Black"])

print(grey)
print(red)
print(black)


squirrel_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey, red, black],
}

data_to_excel = pandas.DataFrame(squirrel_dict).to_csv("squirrel_dict.csv")