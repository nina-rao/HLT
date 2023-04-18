# CS 4395: Human Language Technologies :sparkling_heart:
**Portfolio for Human Language Technologies @ UTD**

### Thoughts & Observations on NLP
This [assignment](https://github.com/nina-rao/HLT/blob/main/Overview%20of%20NLP.pdf) details NLP, various NLP approaches, and a reflection on my interest in the subject.

### Text Processing with Python
This [program](https://github.com/nina-rao/HLT/blob/main/asgn1.py) takes in an employee file, cleans the data, and outputs the data. To run it, go to your terminal and navigate to the directory where the .py file is located. Then type python [name of py file] [relative path of data file] 
e.g. python asgn1.py data/data.csv

Compared to other programming languages, text processing with Python is a fairly painless process (as painless as text processing can be). There are many libraries and functions that take care of tasks that would otherwise take multiple lines of code. I found that many of the redundant aspects of normalizing text could be condensed into a single line. However for someone who isn't fully aware of the many Python resources at their disposal, it could be difficult especially considering Python is not a strongly typed language. This may be offputting to those used to working with languages like C++ or Java.

This assignment was an introduction to many concepts for me such as making a program universally compilable regardless of OS, pickling files, working with DataFrames, and Python structures in general. I have only used Python for the odd class assignment or small personal project and since I use it so infrequently I had to familiarize myself with much of the syntax and data structures. The utilization of RegEx was a refresher for me, and trying to match the phone numbers was a tedious puzzle. 

### NLTK + Word Guessing Game
This [program](https://github.com/nina-rao/HLT/blob/main/asgn2.py) tokenizes the first chapter of an anatomy textbook and does some preprocessing using NLTK. It produces a dictionary of nouns and their counts in order to play a word guessing game with the 50 most common nouns in the text. 

### WordNet
This [notebook](https://github.com/nina-rao/HLT/blob/main/asgn3.ipynb) is an exploration into the organization of words in WordNet, word forms, word similarity, word sentiment, and collocations.


### N-Grams
This assignment consists of 2 programs. The [first program](https://github.com/nina-rao/HLT/blob/main/ngram1.py) reads in 3 sets of training data in English, French, and Italian and constructs seperate language models for each of them. These language models are unigram and bigram dictionaries. The [second program](https://github.com/nina-rao/HLT/blob/main/ngram2.py) uses these dictionaries to construct a probabilistic model that uses LaPlace smoothing to compute the probability of a given text being in the language. Click [here](https://github.com/nina-rao/HLT/blob/main/N-grams%20Narrative.pdf) to read more about N-Grams. 

### Sentence Parsing
This [assignment](https://github.com/nina-rao/HLT/blob/main/Sentence%20Parsing.docx) compares 3 different parsing methods: PSG tree, Dependency parse, and SRL parse. Using an example sentence, I've illustrated each of these parses and how they provide a deeper look into the syntax and semantics of text.

### Web Crawler
This [project](https://github.com/nina-rao/HLT/blob/main/webCrawler.py) obtains relevant links from a starting URL through a web-crawling function. These links are used to build a knowledge base.

### Text Classification
This [assignment](https://github.com/nina-rao/HLT/blob/main/TextClassification.pdf) explores using sklearn to run Naïve Bayes, Logistic Regression, Neural Networks for text classification on a dataset.
