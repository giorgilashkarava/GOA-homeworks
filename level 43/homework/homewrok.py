#codewars
def sequence_sum(start, end, step):
    return sum(range(start, end+1, step))
#2
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())
#3
def sum_mix(arr):
    sum = 0
    for i in arr:
        sum += int(i)
    return sum