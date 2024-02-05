# import new_module
#
# print(new_module.another_variable)
#
# from turtle import Turtle, Screen
#
# timmy=Turtle()
# timmy.shape("turtle")
# timmy.pencolor("coral")
# timmy.forward(100)
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# print(timmy)
# my_screen=Screen()
# height=my_screen.canvheight
# print(height)
# my_screen.exitonclick()

from prettytable import PrettyTable

x=PrettyTable()
x.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
x.add_column("Type", ["Electric","Water", 'Fire'])
x.align="l"
x.valign="m"
print(x.header)
print(x)



