import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

with open("C:\Users\User\лингв\метель.txt", encoding="utf-8") as file:
    text = file.read()
stop_words = set(stopwords.words('russian'))

word_tokens = word_tokenize(text)
filtered_text = [word for word in word_tokens if word.lower() not in stop_words]

clean_text = ' '.join(filtered_text)
print(clean_text)