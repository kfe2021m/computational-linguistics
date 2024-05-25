with open("C:\Users\User\лингв\метель.txt", encoding="utf-8") as file:
    text = file.read()
n = ''.join([char for char in text if char.isalpha() or char.isspace()])
print(n)