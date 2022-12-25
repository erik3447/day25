import pandas

pd = pandas.read_csv("weather_data.csv")


temp_series = pd["temp"]

temp_list = []

for degress in temp_series:
    temp_list.append(degress)

print(temp_list)