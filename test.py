"""
A file that contains tests for Document class and
search_engine class
"""
from cse163_utils import assert_equals
from document import Document
from search_engine import SearchEngine


def test_get_path(Document):
    """
    test for get_path method in
    document.py
    """
    # test get_path for test_document
    assert_equals('/home/test_document.txt', Document.get_path())


def test_term_frequency(Document):
    """
    test for term_frequency method in
    document.py
    """
    # test term_frequency for test_document
    assert_equals(0.125, Document.term_frequency('eye'))
    # test for non_existed term
    assert_equals(0, Document.term_frequency('house'))


def test_term_frequency_empty(Document):
    """
    test for term_frequency method in
    document.py with empty file
    """
    # test for empty file
    assert_equals(0, Document.term_frequency('Nothing'))


def test_get_words(Document):
    """
    test for get_words method in
    document.py
    """
    # test get_words for test_document
    assert_equals(['you', 'fit', 'into', 'me', 'like', 'a', 'hook',
                   'an', 'eye', 'fish', 'open'], Document.get_words())


def test_search_engine(Directory):
    """
    test the search engine class
    """
    # search for word 'fit'
    assert_equals(['test_file/test_file_2.txt', 'test_file/test_file_1.txt'],
                  Directory.search('cat'))
    # search for word 'dog'
    assert_equals(['test_file/test_file_1.txt', 'test_file/test_file_3.txt'],
                  Directory.search('dog'))
    # search for phrase 'human cat'
    assert_equals(['test_file/test_file_2.txt', 'test_file/test_file_1.txt',
                   'test_file/test_file_3.txt'], Directory.search('cat human'))


def main():
    test = Document('test_document.txt')
    test_empty = Document('test_document_empty.txt')

    test_search = SearchEngine('test_file')

    test_get_path(test)
    test_term_frequency_empty(test_empty)
    test_term_frequency(test)
    test_get_words(test)

    test_search_engine(test_search)


if __name__ == '__main__':
    main()
