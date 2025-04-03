def distinct(seq):
    result = []
    for item in seq:
        if item not in result:
            result.append(item)

    return result
#2
def get_planet_name(id):
    return{
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }.get(id)