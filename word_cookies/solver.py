#!/usr/bin/env python

"""Goal: find all the valid words in a dictionary that use only the specified
letters."""

################################### Imports: ###################################

import argparse

################################## Functions: ##################################

def load_dict(dict_filename):
    """Load a dictionary file into a list of (lowercase) words."""
    with open(dict_filename) as f:
        content = f.readlines()
    content = [x.strip().lower() for x in content]
    return content

def word_works(letters, word, allow_repeats=False):
    """Return True if word can be spelled using only letters.  letters is a single
    string.  allow_repeats allows each letter to be used many times.
    """
    letters_remaining = letters.lower()
    for letter in word:
        if letter in letters_remaining:
            if not allow_repeats:
                letters_remaining = letters_remaining.replace(letter, '', 1)
        else:
            return False
    return True

def match_words(letters, dictionary, allow_repeats=False):
    """Return all words in dictionary that can be spelled using only letters.
    dictionary should be a python list from load_dict().
    """
    results = []
    for word in dictionary:
        if word_works(letters, word, allow_repeats):
            results.append(word)
    return results

################################### main(): ####################################

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='List the words in dictionary that can be spelled using only the given letters.')
    parser.add_argument('dictionary',
                        help='text file with one word per line')
    parser.add_argument('letters',
                        help="set of letters, e.g. 'wdro'")
    parser.add_argument('-r', '--reuse_letters', action='store_true',
                        help='allow each letter to be used more than once')
    args = parser.parse_args()

    dictionary = load_dict(args.dictionary)
    matching_words = match_words(args.letters, dictionary,
                                 allow_repeats=args.reuse_letters)
    print(matching_words)

#################################### TODO: #####################################

# - limit results based on number of answer slots, and sort more common words first
# - update remaining solutions as they are used, and by remaining spots on board (alphabetical)
# - discuss / implement faster solutions, e.g. using indexed dictionary, or split dict into 
#   individual letters and only search through starting letters that are on the board.  that
#   would also allow discussion of parallelism, e.g. one computer per starting letter.
# - OCR of screenshot
# - set up email address that automatically replies with solutions

################################################################################
