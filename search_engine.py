"""
File contain the class SearchEngine. Class contain a private
function _calculate_idf that calculate the Inverted Index frequency
for the given word. A function search that will return a list of
file according to the tf-idf of the word.
"""
import os
import re
from document import Document
import math


class SearchEngine:
    """
    The class SearchEngine contains functions that help
    to return a list of file for a given word according to
    its tf-idf.
    """
    def __init__(self, directory_name):
        """
        implementing a initializer for SearchEngine class,
        it takes a directory name that represent the directory
        that contains all the files for searching.
        """
        self._inverse_index = {}
        self._list_file = []
        self._num_document = len(self._list_file)
        self._directory_name = directory_name

        for file_name in os.listdir(directory_name):
            self._list_file.append(file_name)
            self._num_document += 1
            if not file_name.startswith('.'):
                file_path = self._directory_name + '/' + file_name
                file_doc = Document(file_path)
                for word in file_doc.get_words():
                    if word in self._inverse_index:
                        self._inverse_index[word].append(file_doc)
                    else:
                        self._inverse_index[word] = [file_doc]

    def _calculate_idf(self, term):
        """
        take a parameter term, and return
        the IDF for such term
        """
        if term not in self._inverse_index:
            return 0
        else:
            return math.log(self._num_document /
                            len(self._inverse_index[term]))

    def search(self, search_terms):
        """
        take a string as parameter, return the ranked list of document
        with the highest ti_idf relatively to the search term
        as first. The search term can be case insensitive, the function
        will strip it down to an lower case term.
        """
        list_file = []
        term_list = []
        document_dict = {}
        list_path = []
        wordcount = 0

        for search_term in search_terms.split():
            search_term = re.sub(r'\W+', '', search_term)
            search_term = search_term.lower()
            term_list.append(search_term)

        for search_term in term_list:
            if search_term in self._inverse_index.keys():
                wordcount += 1
                for document in self._inverse_index[search_term]:
                    tf_idf = (document.term_frequency(search_term) *
                              self._calculate_idf(search_term))
                    if document in document_dict:
                        document_dict[document] += tf_idf
                    else:
                        document_dict[document] = tf_idf
            if wordcount == 0:
                return None

        sorted_list = dict(sorted(document_dict.items(),
                           key=lambda x: x[1], reverse=True))
        for key in sorted_list.keys():
            list_file.append(key)
        for path in list_file:
            file_path = path.get_path()
            file_path = file_path[5:]
            list_path.append(file_path)
        return list_path
