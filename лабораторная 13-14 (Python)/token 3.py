import nltk
nltk.download('punkt')

with open("C:\Users\User\лингв\метель.txt", "r", encoding="utf-8") as file:
    a = file.read()
    tokens = nltk.word_tokenize(a)
    print(tokens)