def check_list_length(lst):
    # სიის სიგრძის ლუწობის შემოწმება
    if len(lst) % 2 == 0:
        return "List length is even"
    else:
        return "List length is odd"

# ფუნქციის ტესტირება
test_list = [1, 2, 3, 4]  # სიის სიგრძე: 4 (ლუწი)
result = check_list_length(test_list)
print("ტესტი 1 შედეგი:", result)

test_list = [1, 2, 3]  # სიის სიგრძე: 3 (კენტი)
result = check_list_length(test_list)
print("ტესტი 2 შედეგი:", result)
