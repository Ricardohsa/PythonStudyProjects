travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
country_visited = {}
def  add_new_country(country, numbervisit, cities ):
    country_visited = {
        "country": country,
        "visits": numbervisit,
        "cities": cities}
    
    travel_log.append(country_visited)
    



#🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("Russia", 2,  ["Moscow", "Saint Petersburg"])
print(travel_log)

