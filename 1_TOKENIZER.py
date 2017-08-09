# Now we'll start with our first Topic Tokenizer
# Tokenizer divides a given line into separate words or sentences

# Example_TEXT = "Hi Everyone , NLP is fun, isn't it ? Keep Learning NLP."
# Word Tokenizer -> ["Hi", "Everyone","NLP".............]
# Sentence Tokenizer -> ["Hi Everyone, NLP is fun, isn't it ?", "Keep Learning NLP."]
# Those are the expected outputs

import nltk

# Invoking the tokenize package inside nltk library
from nltk.tokenize import Word_tokenize, sent_tokenize


# Lets take an example text
example_line = "Travel and tell no one, live a true love story and tell no one, live happily and tell no one, people ruin beautiful things."

# Now lets print the output
print(sent_tokenize(example_line))
print(word_tokenize(example_line))


# Thats all. We Just tokenized a given sentence . Good Going. Our Next topic is STOPWORDS !

