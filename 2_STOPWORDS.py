
# We all know what are stopwords
# In computer search engines, a stop word is a commonly used word 
# (such as "the") that a search engine has been programmed to ignore, 
# both when indexing entries for searching and when retrieving them
# as the result of a search query.
# Words like a,an,the,for,is,of,in,on,at  etc are of no significance for speech context
#  Hence we remove them before processing the natural language

import nltk   # As always, import the library

from nltk.corpus import stopwords    # As you can read , importing the packages
from nltk.tokenize import word_tokenize     # invoking word tokenizer 


eg = "Node is currently integrated with Salesforce, and customers can ask questions like  What company will be most interested in my product? Node will tell the customer who or what they need to connect with, why it came up with that answer, and even what to say to make the most of the opportunity. It's searching without using a search box."

# Setting up the stopwords
stop_words = set(stopwords.words("english"))

# Lets tokenize them now
words =  word_tokenize(eg)


# Lets filter out stop words by checking each word if they exist in stopwords list or not
filtered_sentence = []

# Checking each word
for each_word in words:
	if each_word not in stop_words:
		filtered_sentence.append(each_word)

# fINALLY Print out the tokenized and filtered words
print(filtered_sentence)



# Next we'll see  STEMMING





















