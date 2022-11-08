"""
Aaron Liu
CSE 163 AI
02/06/2021

File contain the class Document, represent single
file in the SearchEngine. Class contain function
get_path that return the path of document, term_frequency
that return the TF for given term and get_words that
return a list of unqiue words in the document
"""

import re
import os


class Document:
    """The Document class represents a single file in the
    SearchEngine, and will include multiple function to compute
    the term frequency of a term in the document, path of the document
    and the list of unqiue words. """
    def __init__(self, file_name):
        """
        inplementing intializer for Document class, it takes
        a file name as parameter
        """
        self._file_name = file_name
        self._list_word = []
        self._file_path = os.path.abspath(file_name)
        self._term_dict = {}

        if os.stat(file_name).st_size == 0:
            pass
        else:
            with open(file_name) as f:
                count = 0
                for line in f.readlines():
                    for word in line.split():
                        word = word.lower()
                        word = re.sub(r'\W+', '', word)
                        count += 1
                        if word in self._term_dict:
                            self._term_dict[word] = self._term_dict[word] + 1
                        else:
                            self._term_dict[word] = 1
                            self._list_word.append(word)
        for word in self._term_dict:
            self._term_dict[word] = self._term_dict[word] / count

    def get_path(self):
        """
        return the path of the file the
        document represent
        """
        return self._file_path

    def term_frequency(self, term):
        """
        take a term for parameter and return
        the frequency of the term in the file, the
        term can be case insensitive since function will
        strip it down to an lower case term.
        """
        term = re.sub(r'\W+', '', term)
        term = term.lower()
        if term not in self._list_word:
            return 0
        else:
            return self._term_dict[term]

    def get_words(self):
        """
        return the list of unqiue
        words in the file
        """
        return self._list_word
