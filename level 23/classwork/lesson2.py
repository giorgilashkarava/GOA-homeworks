# 3)მომხმარებელს შემოატანინეთ სახელი, შემდეგ შემოატანინეთ ასო და თუ ამ სახელში ეს 
# ასო არიქნება, აშინ გამოუტანეთ "cant find character", თუ იქნება მაშინ გამოუტანეთ "found it" და გვერდზე 
# მიუწერეთ ამ ასოს ინდექსი

name = input("enter your name here") 
abc = input("your abc")
if name.find(abc) == -1:
    print("found it")
else:   
    print("Can't find it") 
    