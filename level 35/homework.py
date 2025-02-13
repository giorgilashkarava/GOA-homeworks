#1
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())
#2
def sequence_sum(start, end, step):
    return sum(range(start, end+1, step))
#3
def better_than_average(class_points, your_points):
    i = 0
    totalP = 0
    while i < len(class_points):
        totalP += class_points[i]
        i += 1
    totalP = totalP / len(class_points)
    if totalP > your_points:
        return False
    else:
        return True
#4
def grow(arr):
    sum = 1
    for i in arr:
        sum *= i
    return sum
#5
def smash(words):
    
    i=0
    l=len(words)
    str1=""
    while i<l:
        if i<l-1:
            str1+=words[i] + " "
        else: 
            str1+=words[i]
        i+=1
        
    return str1