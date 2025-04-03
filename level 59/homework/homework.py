#1
def min_max(lst):
  min, max = lst[0], lst[0]
  
  for x in lst:
    if x > max:
      max = x
    elif x < min:
      min = x
  
  return [min, max]
#2
def is_leap_year(year):
    
    x: bool = False

    if year % 4 == 0:
        x = True
        if year % 100 == 0:
            x = False
            if year % 400 == 0:
                x = True
    return x
#3
def fizzbuzz(n):
    li = []
    for i in range (1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            li.append("FizzBuzz")
        elif i % 3 == 0:
            li.append("Fizz")
        elif i % 5 == 0:
            li.append("Buzz")
        else:
            li.append(i)
    return li