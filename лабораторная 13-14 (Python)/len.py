file = open("C:\Users\User\лингв\метель.txt", encoding="utf-8")

words = 0

for line in file:
    words += len(line.split())

print("Words:", words)