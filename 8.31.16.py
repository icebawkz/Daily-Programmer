# Solution from /u/MichaelPenn for learning purposes

with open('enable1.txt') as file:
    lexicon = {word.strip() for word in file}

def dank(name, word='', i=0):   
    global top_word_length, longest_words

    if i < len(name):
        dank(name, word + name[i].lower(), i + 1)
        if i != 0: 
            dank(name, word, i + 1)
    elif word in lexicon:
        if len(word) > top_word_length:
            longest_words = {word.title()}
            top_word_length = len(word)
        elif len(word) == top_word_length:
            longest_words.add(word.title())

names = ['Donald Knuth', 'Alex McAfee', 'Alan Turing', 'Claude Shannon', 'Ada Lovelace', 'Haskell Curry', 'Michael Penn']
for n in names:
    top_word_length = 0
    longest_words = {}
    dank(n)
    print(', '.join(longest_words))