def power_of_number(base, exponent):
    # პირველი რიცხვის მეორეში აყვანა
    result = base ** exponent
    # შედეგის დაბრუნება
    return result

# ფუნქციის ტესტირება
base = 2
exponent = 3
result = power_of_number(base, exponent)
print(f"{base} ხარისხში {exponent} არის: {result}")
