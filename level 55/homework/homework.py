my_dict = {
    "სახელი": "გიორგი",
    "ასაკი": 13,
    "ქალაქი": "სენაკი"
}

# ცარიელი სიები
keys_list = []
values_list = []

# for loop მონაცემების დამატებისთვის
for key, value in my_dict.items():
    keys_list.append(key)
    values_list.append(value)

# შედეგის გამოყვანა
print("Keys:", keys_list)
print("Values:", values_list)