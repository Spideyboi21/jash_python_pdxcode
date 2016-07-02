def room0():
  description = """Do you smell that? what's cooking in the house?"""


doors = {"east: room1, "south": room5}
return proccess_user_movement(description, doors)

def room1():
description = "What kind of shrimp do I think is here?"
doors = {"south": room6, "east": room2, "west": room0}
return proccess_user_movement(description, doors)

def room2():
    description = "You can go east or south or west."
    doors = {"east": room3, "west": room1, "south": room7}
    return proccess_user_movement(description, doors)

def room3():
    description = "Move east, west, or south."
    doors = {"east": room4, "west": room4, "south": room8}
    return proccess_user_movement(description, doors)

def room4():
    description = " A corner! You may go south or west."
    doors = {"south": room9, "west" room3}
    return proccess_user_movement(description, doors)

def room5():
    description = "Way over by zero. You can go east or north!"
    doors = {"east":room6, "north": room8}
    return proccess_user_movement(description, doors)
    
