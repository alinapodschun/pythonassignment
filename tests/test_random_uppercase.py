# -*- coding: utf-8 -*-
"""
@author: Alina Podschun

A python test module to test the function random_uppercase from the module
scrambled.py.

This test module defines the following test functions:
    
    test_random_result
    test_errors
    test_positions_uppercase
    
"""

from scrambled import random_uppercase

def test_random_result():
    """
    Tests whether the function returns a result that is different
    from the input.
    
    Examples/Arguments/Returns/Raises:
        None: This is a test function
        
    Test fails: When the result is the same string as the input.
    
    """
    text = 'Hello I am Alina'
    result = random_uppercase(text)
    assert text != result

def test_errors():
    """
    Tests whether the errors are correctly raised.
    
    Examples/Arguments/Returns/Raises:
        None: This is a test function
        
    Test fails: When the function doesn't raise errors in respose to an input
    of type integer, as well as when it doesn't raise errors in response to 
    an empty string
    
    """
    import pytest
    text = 12397095
    with pytest.raises(TypeError):
       random_uppercase(text)
    text_2 = ''
    with pytest.raises(ValueError):
        random_uppercase(text_2)

def test_positions_uppercase():
    """
    Tests whether there are new uppercase letters compared to the input.
    
    Examples/Arguments/Returns/Raises:
        None: This is a test function
        
    Test fails: When the indices of the uppercase letters in the result
    all remain the same to the indices of the uppercase letters in the input.
    
    """
    text = 'Hello I am Alina'
    result = random_uppercase(text)
    # to find the indices for each upper case letter in text as well as result:
    upper_text = set()
    for index, letter in enumerate(text):
        if letter == letter.upper():
            upper_text.add(index)
    upper_result = set()
    for index, letter in enumerate(result):
        if letter == letter.upper():
            upper_result.add(index)
    assert upper_text != upper_result

if __name__ == '__main__':
    test_random_result()
    test_errors()
    test_positions_uppercase()
    print('If you can read this, the tests all passed.')