#1
def update_light(current):
    if current=="green":
        return "yellow"
    elif current=="yellow":
        return "red"
    return "green"
#2
def count_by(x, n):
    arr = []
    for num in range(1, n+1):
        result = x * num
        arr.append(result)
    return arr
#3
def abbrevName(name):
    return '.'.join(x[0].upper() for x in name.split())