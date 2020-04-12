# -*- coding: utf-8 -*-
"""
@author: Alina Podschun

A python test module to test the function scramble_shortwords from the module
scrambled.py.

This test module defines the following test functions:
    
    test_random_result
    test_errors
    test_punctuation
    test_only_shortwords
    
"""

from scrambled import scramble_shortwords

def test_random_result():
    """
    Tests whether the function returns a result that is different
    from the input.
    
    Examples/Arguments/Returns/Raises:
        None: This is a test function
        
    Test fails: When the result is the same string as the input.
    
    """
    text = 'One Four Seven Ten'
    result = scramble_shortwords(text)
    # in case the function randomly created a result that is the same as the
    # text, let's scramble again:
    if result == text:
        result = scramble_shortwords(text)
    assert result != text

def test_errors():
    """
    Tests whether the errors are correctly raised.
    
    Examples/Arguments/Returns/Raises:
        None: This is a test function
        
    Test fails: When the function doesn't raise errors in respose to an input
    of type integer, as well as when it doesn't raise errors in response to 
    an input with lenght = 1
    
    """
    import pytest
    text = 3489012
    with pytest.raises(TypeError):
       scramble_shortwords(text)
    text_2 = 'H'
    with pytest.raises(ValueError):
        scramble_shortwords(text_2)

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
    result = scramble_shortwords(text)
    indices_result = []
    for letter in result:
        if letter in punctuation:
            #find me the index of the letter and add it to my list
            position_letter = result.index(letter)
            indices_result.append(position_letter)
        else:
            pass
    assert indices_text == indices_result
    
def test_only_shortwords():
    """
    Tests whether the function scrambles only short words, not long words.
    
    Examples/Arguments/Returns/Raises:
        None: This is a test function
        
    Test fails: When the long words don't remain the same as in the input,
    as well as when not least one of the short words has been scrambled.
    
    """
    text = 'One Four Seven Ten'
    result = scramble_shortwords(text)
    # in case the function randomly created a result that is the same as the
    # text, let's scramble again:
    if result == text:
        result = scramble_shortwords(text)
    result = result.split()
    text = text.split()
    # it could be that randomly the result has only changed for either "One"
    # or "Ten". One of them changing would be sufficient to know that the 
    # function CAN instead randomly change short words. Thus:
    assert text[0] != result[0] or text[3]!= result[3]
    assert text[1] == result[1]
    assert text[2] == result[2]  

if __name__ == '__main__':
    test_random_result()
    test_errors()
    test_punctuation()
    test_only_shortwords()
    print('If you can read this, the tests all passed.')