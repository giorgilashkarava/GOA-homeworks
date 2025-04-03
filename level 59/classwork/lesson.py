#1
def count_positives_sum_negatives(arr):
    sum,count = 0,0
    if (len(arr) == 0):
        return []
    for i in arr:
        if i > 0:
            count += 1
        else:
            sum = sum + i    
    return [count,sum]
#2
def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
#3
def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    return number*9