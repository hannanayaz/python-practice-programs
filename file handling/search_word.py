with open("practice.txt", "r") as file:
    r = file.read()
    word = input("enter the word to search: ")
    if word in r:
        print("word found")
    else:
        print("word not found!")