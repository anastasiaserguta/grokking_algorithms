from binary_search import binary_search

def test_binary_search_int_nums():
    assert binary_search([1, 3, 5, 7, 9, 11, 13, 15], 1) == 0

def test_binary_search_float_nums():
    assert binary_search([0.1, 2.2, 3.5, 4.8, 5.9, 6.3, 8.8, 10.0], 8.8) == 6

def test_binary_search_neg_pos_int_nums():
    assert binary_search([-10, -5, 0, 2, 3, 7, 15, 20], 20) == 7

def test_binary_search_none_nums():
    assert binary_search([1, 3, 5, 7, 9, 11, 13, 15], 17) == None

def test_binary_search_low_strings():
    assert binary_search(['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi'], 'cherry') == 2
    assert binary_search(['a', 'abc', 'abacus', 'abundance', 'applepie', 'banana'], 'applepie') == 4

def test_binary_search_upp_strings():
    assert binary_search(['Apple', 'Banana', 'Cherry', 'Grape', 'Orange'], 'Apple') == 0

def test_binary_search_none_strings():
    assert binary_search(['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi'], 'mango') == None
