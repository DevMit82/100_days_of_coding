# with open ("weather_data.csv", "r") as csv_file:
#     data = (csv_file.readlines())
#
# print(data)

# import csv
#
# with open ("weather_data.csv", "r") as csv_file:
#     data = csv.reader(csv_file)
#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))
#         if row[1] == "temp":
#             temperatures.remove("temp")
#
# print(temperatures)
import pandas

data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# Get data on columns
# temp_list = data["temp"].to_list()
# average_temp = data["temp"].mean()
# max_temp = data["temp"].max()
#
# print(temp_list)
# print(round(average_temp, 2))
# print(max_temp)
###############################

#get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
#
# print(monday_temp * 1.8 + 32)
##########################################################################
#create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("new_data.csv")
print(data_frame)