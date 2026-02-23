import pandas

data = pandas.read_csv("data_squirrel.csv")

count = data["Primary Fur Color"].value_counts()
count.to_csv("Squirrel_Colors.csv")

print(count)