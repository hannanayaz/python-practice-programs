with open("practice.txt", "r") as file:
    r = file.read()
    print(r)
    
a = input("what do you want to replace in the file? ")
b = input("what do you want to replace it with? ")
replace = r.replace(a, b)
        


with open("practice.txt", "w") as file:
    file.write(replace)

    print("\nthe saved changes are: ")
    print(replace)      