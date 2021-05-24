# _author_='Rahul kharatmol'
import nltk
# tokenization
from nltk.tokenize import sent_tokenize

text = """people are good in india. They are verry helpfull"""

tokenized_text = sent_tokenize(text)
print(tokenized_text)


# Stopworrds Remove
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))
print(stop_words)
filtered_sent = []
import string
stopwords = nltk.corpus.stopwords.words('english')

text_new = "".join([i for i in text if i not in string.punctuation])
print(text_new)
words = nltk.tokenize.word_tokenize(text_new)
print(words)
words_new = [i for i in words if i not in stopwords]
print(words_new)
# Stemming
ps = nltk.PorterStemmer()
w = [ps.stem(word) for word in words_new]
print(w)
# lemitization
wn = nltk.WordNetLemmatizer()
w = [wn.lemmatize(word) for word in words_new]
print(w)
# pos tagging
tagged = nltk.pos_tag(w)

print(tagged)