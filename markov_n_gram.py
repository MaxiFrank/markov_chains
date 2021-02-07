
"""Generate Markov text from text files."""

from random import choice
# import sys

# input_path = sys.argv[1]

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = open(file_path).read()

    return text


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    n is the number of elements in the tuple key.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')
                                
    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    # {('hi', 'there'):['mary', 'juanita'], ('mary', 'hi'):['there'], ('there', 'mary'):['hi'], ('there', 'juanita'):[None]}
    # n_gram: {('hi', 'there', 'mary'):['hi'], ('there', 'mary', 'hi'):['there'], ('mary', 'hi','there'):['juanita'], ('hi','there', 'juanita'):[None]}

    chains = {}
    clean_string = text_string.split()
    for i in range(len(clean_string) - n):
        key = []
        if i == 0:
            for num in range(n):
                key.append(clean_string[num])
        else:
            for num in range(i,n+i):
                key.append(clean_string[num])
        key = tuple(key)
        if len(chains.get(key,[])) == 0:
            chains[key] = chains.get(key,[clean_string[i+n]])
        else:
            chains[key].append(clean_string[i+n])
        

    # need to make the key into a tuple of n elements
    key = []

    index_list = sorted([(-1)*i for i in range(1,n+1)])

    for num in index_list:
        key.append(clean_string[num])
    key = tuple(key)
    chains[key] = [None]

    return chains

def make_text(chains,n):
    """Return text from chains."""
    words = []
    
    key = choice(list(chains.keys()))
    words.extend(key)
    value = choice(chains[key])
    words.append(value)

    key_list = []
    index_list = sorted([(-1)*i for i in range(1,n+1)])

    for num in index_list:
        key_list.append(words[num])
    key_tuple = tuple(key_list)
    
    while chains.get(key_tuple,[]) != [None]:
        new_key = key_tuple
        if len(chains.get((new_key),[])) > 0:
            value = choice(chains[new_key])
            words.append(value)
        key_list = []
        for num in index_list:
            key_list.append(words[num])
        key_tuple = tuple(key_list)

    return ' '.join(words)

input_path = 'gettysburg.txt'

input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 3)

# Produce random text
random_text = make_text(chains,3)

print(random_text)

