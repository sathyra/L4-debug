
import nltk
nltk.download('punkt')
from nltk import sent_tokenize
from nltk import word_tokenize

#open the text file
text_file=open("C:\\Users\\ADMIN\\Downloads\\testing.txt",'r', encoding='utf-8')

#read the data
read_text=text_file.read()

#Datatype of the data read
print(type(read_text))
print("\n")

#print the entire story text
print(read_text)

#length of the text
print(len(read_text))

#tokenize the text by sentence
token_sentence= senttokenize(read_text)

#sentence count
print(len(token_sentence))

print(token_sentence)

#tokenize the word
token_words=wordtokenize(read_ext)

print(token_words)
