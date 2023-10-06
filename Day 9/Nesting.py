# Nesting is a list to a value in a dictionary or even add another dictionary as a value in a dictionary
# {
#     Key: [List],
#     Key2: {Dict},    
# }


# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Canada": "Ottawa",
}

#Nestin a List in a Dictionary
# travel_log = {
#     "Canada": {"cities_visited": ["Toronto", "London", "Quebec"]
#                , "total_visits": 5
#                , "total_rents": 5},
#     "Brasil": {"cities_visited": ["Sao Paulo", "Bahia", "Rio Grande do Sul", "Rio de Janeiro", "Mato Grosso", "Minas Gerais" ]
#                , "total_visits": 5
#                , "total_rents": 5},
#     "USA": "Boston",        
# }

# Nesting dictionay in a list
travel_log = [
    {
        "Country": "Canada", 
        "cities_visited": ["Toronto", "London", "Quebec"], 
        "total_visits": 5
    },
    {
        "Country": "Brasil", 
        "cities_visited": ["Sao Paulo", "Bahia", "Rio Grande do Sul", "Rio de Janeiro", "Mato Grosso", "Minas Gerais" ], 
        "total_visits": 5
    }
]

    
order =   {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(travel_log[1]["Country"])  