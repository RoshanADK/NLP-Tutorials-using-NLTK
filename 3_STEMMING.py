# Stem projects the root to the ground. Similarly, we have affixes in our words attached to a stem
# Removing those affixes is what STEMMING IS 
# Example:  Running , Runs, Runnn, Runik, Runner   etc all has common STEM 'Run' Since all their meanings are same.



import nltk

# We'll use Porter Stemmer for stemming the words which is in stem package
from nltk.stem import PorterStemmer

# Again we'll be tokening the words before stemming them.
from nltk.tokenize import word_tokenize


# Lets Invoke Porter Stemmer now
ps = PorterStemmer()

# Since this is a tokenized set of words hence no need to go for further Tokenization
eg_words = ["Python","pythonly","pythonic","pythoner","pythoned"]

for w in eg_words:
	print(ps.stem(w))   # This is how one calls the stemmer


# If you see the output there is one word called Pythonli , this is because of the Stemmer where it stems any word ending in y followed by a consonant, it stems the word from 'y' to 'i'

# If you want to take sentences as input you have to Tokenize them first and rest is same step

# eg_sentence = "This is an example sentence"
# words = word_tokenize(eg_sentence)
# Rest of the steps are same as above 


# And words case doesn't matter here 