from pymystem3 import Mystem

mystem = Mystem()
with open("C:\Users\User\лингв\метель.txt", encoding="utf-8") as file:
    text = file.read()

lemmas = mystem.lemmatize(text)
analysis = mystem.analyze(text)

print(lemmas)
print(analysis)