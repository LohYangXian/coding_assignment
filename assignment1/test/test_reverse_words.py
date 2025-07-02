import sys
import os

# Manually add src/ to sys.path before any imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from reverse_words import WordReverserProcessor

def test_basic_example():
    r = WordReverserProcessor()
    assert r.reverse_words("String; 2be reversed...") == "gnirtS; eb2 desrever..."

def test_simple_words():
    r = WordReverserProcessor()
    assert r.reverse_words("hello world") == "olleh dlrow"

def test_punctuation_preserved():
    r = WordReverserProcessor()
    assert r.reverse_words("hello, world!") == "olleh, dlrow!"

def test_numbers_and_letters():
    r = WordReverserProcessor()
    assert r.reverse_words("a1b2 c3d4") == "2b1a 4d3c"

def test_only_numbers():
    r = WordReverserProcessor()
    assert r.reverse_words("12345 67890") == "54321 09876"

def test_leading_and_trailing_spaces():
    r = WordReverserProcessor()
    assert r.reverse_words("  leading and trailing  ") == "  gnidael dna gniliart  "

def test_multiple_spaces_between_words():
    r = WordReverserProcessor()
    assert r.reverse_words("word1   word2") == "1drow   2drow"

def test_empty_string():
    r = WordReverserProcessor()
    assert r.reverse_words("") == ""

def test_single_word():
    r = WordReverserProcessor()
    assert r.reverse_words("Python3") == "3nohtyP"

def test_symbols_only():
    r = WordReverserProcessor()
    assert r.reverse_words("...!!! ***") == "...!!! ***"

def test_mixed_content():
    r = WordReverserProcessor()
    assert r.reverse_words("Hi! I'm @home.") == "iH! m'I @emoh."

def test_unicode_characters():
    r = WordReverserProcessor()
    assert r.reverse_words("Café123") == "321éfaC"

def test_non_alphanumeric_word_boundary():
    r = WordReverserProcessor()
    assert r.reverse_words("(abc123)!") == "(321cba)!"

def test_word_with_underscores_and_dashes():
    r = WordReverserProcessor()
    assert r.reverse_words("a_b-c") == "c_b-a"  # underscores and dashes are not alphanumeric