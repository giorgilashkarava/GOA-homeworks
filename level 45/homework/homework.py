#codewars
def format_money(amount):
    amount = str(amount)
    if "." in amount:
        split = amount.split(".")
        if len(split[1]) == 1:
            split[1] = split[1] + "0"
        return "$" + split[0] + "." + split[1]
    else:
        return "$" + amount + ".00"
    #2
    def swap_values(arr): 
    arr.reverse()
    #3
    def same_case(a, b):
    if a.isalpha() and b.isalpha():
        return a.islower() == b.islower()
    return -1
#4
def sum_mul(n, m):
    if m <= 0 or n <= 0:
        return "INVALID"
    k = (m - 1) // n
    return (k + 1) * k // 2 * n
