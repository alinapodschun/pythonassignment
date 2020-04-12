# -*- coding: utf-8 -*-
"""
@author: Alina Podschun

A python test module to test the function scramble_all from the module
scrambled.py.

This test module defines the following test functions:
    
    test_random_result
    test_errors
    test_punctuation
    
"""

from scrambled import scramble_all

def test_random_result():
    """
    Tests whether the function returns a result that is different
    from the input.
    
    Examples/Arguments/Returns/Raises:
        None: This is a test function
        
    Test fails: When the result is the same string as the input.
    
    """
    text = 'Hello I am Alina'
    result = scramble_all(text)
    # in case the function randomly created a result that is the same as the
    # text, let's scramble again:
    if result == text:
        result = scramble_all(text)
    assert result != text
    text_2 = 87908098
    result_2 = scramble_all(text_2)
    # in case the function randomly created a result that is the same as the
    # text, let's scramble again:
    if result_2 == text_2:
        result_2 = scramble_all(text_2)
    result_2 = int(result_2)
    assert result_2 != text_2


def test_errors():
    """
    Tests whether the errors are correctly raised.
    
    Examples/Arguments/Returns/Raises:
        None: This is a test function
    
    Test fails: When the function doesn't raise errors in respose to an input
    of type list, as well as when it doesn't raise errors in response to 
    an input with lenght = 1
    
    """
    import pytest
    text = 'Hello I am Alina'
    # splitting the text creates a list; the function should raise a TypeError
    # when it gets something that's not a str or int, e.g. a  list as an input
    text = text.split()
    with pytest.raises(TypeError):
       scramble_all(text)
    text_2 = 'H'
    with pytest.raises(ValueError):
        scramble_all(text_2)
        
def test_punctuation():
    """
    Tests whether punctuation is kept in place, as intended.
    
    Examples/Arguments/Returns/Raises:
        None: This is a test function
        
    Test fails: When the indices of the punctuation in the result are not the
    same as in the input (e.g., when the function mistakingly shuffled
    the punctuation around)
    
    """
    text = 'Hello. I am: Alina'
    import string
    punctuation = tuple(string.punctuation)
    # finding out the positions of the punctuations in the input text
    indices_text = []
    for letter in text:
        if letter in punctuation:
            #find me the index of the letter and add it to my list
            position_letter = text.index(letter)
            indices_text.append(position_letter)
        else:
            pass
    # scrambling text and finding out positions in scrambled text
    result = scramble_all(text)
    indices_result = []
    for letter in result:
        #find me the index of the letter and add it to my list
        if letter in punctuation:
            position_letter = result.index(letter)
            indices_result.append(position_letter)
        else:
            pass
    assert indices_text == indices_result
        
if __name__ == '__main__':
    test_random_result()
    test_errors()
    test_punctuation()
    print('If you can read this, the tests all passed.')