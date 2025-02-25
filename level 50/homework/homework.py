#1
def derive(coefficient, exponent):
    nex = 0
    if exponent == 2:
        nex = 2
    else:
        nex = exponent - 1
    return str( str(coefficient*exponent) + "x^" + str(nex)
#2
