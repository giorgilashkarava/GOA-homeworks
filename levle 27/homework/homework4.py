def number_check(nums):
    if nums > 0:
        return "რიცხვი დადებითია"
    elif nums < 0:
        return "რიცხვი უარყოპითია"
    else:
        return "რიცხვი ნულია"
    



number_check = int(input("enter your nums here"))
print(number_check)
 