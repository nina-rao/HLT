# CS 4395: Human Language Technologies <3
**Portfolio for Human Language Technologies @ UTD**

### Thoughts & Observations on NLP
This [assignment](https://nina-rao.github.io/HLT/Overview%20of%20NLP.pdf) details NLP, various NLP approaches, and a reflection on my interest in the subject.

### Text Processing with Python
This [program](https://nina-rao.github.io/HLT/asgn1.py) takes in an employee file, cleans the data, and outputs the data. To run it, go to your terminal and navigate to the directory where the .py file is located. Then type python [name of py file] [relative path of data file] 
e.g. python asgn1.py data/data.csv

Compared to other programming languages, text processing with Python is a fairly painless process (as painless as text processing can be). There are many libraries and functions that take care of tasks that would otherwise take multiple lines of code. I found that many of the redundant aspects of normalizing text could be condensed into a single line. However for someone who isn't fully aware of the many Python resources at their disposal, it could be difficult especially considering Python is not a strongly typed language. This may be offputting to those used to working with languages like C++ or Java.

This assignment was an introduction to many concepts for me such as making a program universally compilable regardless of OS, pickling files, working with DataFrames, and Python structures in general. I have only used Python for the odd class assignment or small personal project and since I use it so infrequently I had to familiarize myself with much of the syntax and data structures. The utilization of RegEx was a refresher for me, and trying to match the phone numbers was a tedious puzzle. 

### NLTK + Word Guessing Game
This [program](https://nina-rao.github.io/HLT/asgn2.py) tokenizes the first chapter of an anatomy textbook and does some preprocessing using NLTK. It produces a dictionary of nouns and their counts in order to play a word guessing game with the 50 most common nouns in the text. 

### WordNet
This [notebook](https://nina-rao.github.io/HLT/asgn3.ipynb) is an exploration into the organization of words in WordNet, word forms, word similarity, word sentiment, and collocations.


### N-Grams
This assignment consists of 2 programs. The [first program](https://nina-rao.github.io/HLT/ngram1.py) reads in 3 sets of training data in English, French, and Italian and constructs seperate language models for each of them. These language models are unigram and bigram dictionaries. The [second program](https://nina-rao.github.io/HLT/ngram2.py) uses these dictionaries to construct a probabilistic model that uses LaPlace smoothing to compute the probability of a given text being in the language. Click [here](https://nina-rao.github.io/HLT/N-grams%20Narrative.pdf) to read more about N-Grams. 

### Sentence Parsing
This [assignment](https://nina-rao.github.io/HLT/Sentence%20Parsing.docx) compares 3 different parsing methods: PSG tree, Dependency parse, and SRL parse. Using an example sentence, I've illustrated each of these parses and how they provide a deeper look into the syntax and semantics of text.

### Web Crawler
This [project](https://nina-rao.github.io/HLT/webCrawler.py) obtains relevant links from a starting URL through a web-crawling function. These links are used to build a knowledge base.

### Text Classification
This [assignment](https://nina-rao.github.io/HLT/TextClassification.pdf) uses sklearn to run Naïve Bayes, Logistic Regression, Neural Networks for text classification on a dataset.

### ACL Paper Summary
This is a [summary](https://nina-rao.github.io/HLT/ACL%20Paper%20Summary.pdf) of the paper "Improving the Generalizability of Depression Detection by Leveraging Clinical Questionnaires" (Nguyen et al., ACL 2022). 

### Chatbot Code & Report
This is a [chatbot](https://nina-rao.github.io/HLT/ChatPoet.ipynb) I wrote that uses poetry to generate responses. It was written in Google Colab but there is also a [Python file](https://nina-rao.github.io/HLT/chatpoet.py). The [report](https://nina-rao.github.io/HLT/ChatbotReportNinaRao.pdf) contains the system description, sample dialogs, and evaluation.

### Text Classification 2
This [assignment](https://nina-rao.github.io/HLT/TextClassification2.pdf) is text classification of a multi-class dataset using a sequential model, RNN, and different Embedding techniques in Keras.

### Summary
Having neared the completion of this course, I can confidently say that my understanding of Natural Language Processing has improved. The solutions to many problems are shrouded in unstructured data in the form of text, this class has taught me to analyze these problems and begin to see a path towards the solution. I know what kind of preprocessing a text dataset needs, whether syntax parsing or POS or sentiment analysis is necessary, how to create numerical representations of this text, as well as begin to build language models to achieve a task. I am still enthusiastic about NLP and how it can be used to change the way we interact with machines. With a better understanding of how to extract insights from text data, I am hopeful for the advancement of this field of research. Though there are many applications of NLP with business value, I've found that it is equally as satisfying and delightful to use NLP to play with language in casual, experimental ways. Making my chatbot revealed to me how absurd and amorphous language is, which is a revelation shared in both the study of human language and technology. In the future, I plan to keep an eye out for developments and product rollouts in the NLP sphere of research as corporations are starting to invest massively in AI and NLP. As someone keen on reading and analysis I would definitely be interested in a career that allowed me to apply what I've learned this semester. 

[SKILLS](https://nina-rao.github.io/HLT/skills.html)
