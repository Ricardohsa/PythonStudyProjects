import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(data)
# print(type(data))
# print(data["temp"])

#
# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# temp_average = data["temp"].mean()
# max_temp = data["temp"].max()
# min_temp = data.temp.min()
# print(max_temp)

#Get data in Column
# print(data.condition)


#Get Data in Row
# print(data[data.condition == "Rain"])
#
# monday = data[data.day == 'Monday']
# monday_temp_fahrenheit = (monday.temp * 1.8) + 32

# print(monday_temp_fahrenheit)



# print(f"This is max temp of the week: {data[data.temp == max_temp]}")
# print(f"This is min temp of the week: {data[data.temp == min_temp]}")


# Create a datafreame from scratch
data_dict = {
    "students": ["Any", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")