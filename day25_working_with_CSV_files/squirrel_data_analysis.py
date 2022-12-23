import pandas


def no_of_squirrels(color, given_data):
    squirrels = given_data[given_data["Primary Fur Color"] == f"{color}"]
    count = squirrels["Primary Fur Color"].count()
    return count


data = pandas.read_csv("squirrel_count.csv")

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [no_of_squirrels("Gray", data), no_of_squirrels("Cinnamon", data), no_of_squirrels("Black", data)],
}
print(data_dict)

converted_squirrel = pandas.DataFrame(data_dict)
converted_squirrel.to_csv("final_squirrel.csv")
