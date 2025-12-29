# travel_log = {
#     "Frankreich" : ["Paris", "Lille", "Dijon"],
#     "Deutschland" : ["Stuttgart", "Berlin"]
#      }

#print(travel_log["Frankreich"][1])

#nested_list = ["A", "B", ["C", "D"]]

#print(nested_list[2][1])

travel_log = {
    "Frankreich" : {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Deutschland" : {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart" ],
        "total_visits": 5
    }
}

print(travel_log["Deutschland"]["cities_visited"][2])