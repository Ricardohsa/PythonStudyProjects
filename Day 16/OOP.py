# from turtle import *
# timmy = Turtle()
#
#
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.shapesize(3.45)
# timmy.color("DarkSlateGray")
#
# timmy.forward(100)
# timmy.left(45)
#
# timmy.up()
#
# print(timmy)
#
# my_screen.exitonclick()


import prettytable

# x = prettytable.PrettyTable()
# x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# x.add_row(["Adelaide", 1295, 1158259, 600.5])
# x.add_row(["Brisbane", 5905, 1857594, 1146.4])
# x.add_row(["Darwin", 112, 120900, 1714.7])
# x.add_row(["Hobart", 1357, 205556, 619.5])
# x.add_row(["Sydney", 2058, 4336374, 1214.8])
# x.add_row(["Melbourne", 1566, 3806092, 646.9])
# x.add_row(["Perth", 5386, 1554769, 869.4])

pokemonTable = prettytable.PrettyTable()
pokemon_name = ["Pikachu", "Squirtle", "Charmander"]
pokemon_type = ["Electric", "Water", "Fire"]
pokemonTable.add_column("Pokemon Name", pokemon_name)
pokemonTable.add_column("Type", pokemon_type)
pokemonTable.border = True
pokemonTable.header = True
pokemonTable.header_style = "upper"



print(pokemonTable)

