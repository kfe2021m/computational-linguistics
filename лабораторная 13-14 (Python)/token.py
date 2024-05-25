with open("C:\Users\User\лингв\метель.txt", "r", encoding="utf-8") as file:
    c = file.read()
    tokens = c.split(" ")
    print(tokens)