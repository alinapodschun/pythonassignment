# -*- coding: utf-8 -*-
"""
Finalised on 09.04.2020

@author: Alina Podschun

A python module that defines four functions to scramble words in various ways.

Defines the following functions:

    scramble_without_firstlast
    scramble_all
    scramble_shortwords
    random_uppercase

"""


def scramble_without_firstlast(text):
    """
    Reorders/scrambles all the characters in words in a text in a random way, 
    leaving the first and last letter of each word in place.
    
    Words here are defined as being separated by white spaces and remain 
    separated during the scrambling process.
    
    The function also takes care of punctuation, not scrambling it.
    
    Example:
        >>> scramble_all('Hello I am Alina')
        'Hlleo I am Anila'
        >>> scramble_all('Hello. I am: Alina')
        'Hlelo. I am: Ainla'
        >>> scramble_all('have a margherita')
        'hvae a mgtrrehaia'
        
    Arguments:
        text: A string or integer containing characters that can be separated
        into words by white spaces.
    
    Returns:
        A new string in which the first and last letter of the 
        input words are left in place, while all other letters are scrambled.
        
    Raises:
        TypeError for texts that are not strings or integers.
        ValueError for len(text) <= 4.
       
    """
    if isinstance(text, str) == True:
        pass
    elif isinstance(text, int) == True:
        text = str(text)
    else:
        raise TypeError('Your input needs to be of type string or integer.')
    # testing if text is long enough (consisting of at least four 
    # characters): four characters because there need to be a first and last 
    # one that can stay in place, and two middle ones that could be scrambled:
    if len(text) <= 4:
        raise ValueError('Cannot scramble a text this short.')
    else:
        pass
    import random
    import string
    result = []
    punctuation = tuple(string.punctuation)
    words_list = text.split()
    for word in words_list:
        # removing spaces behind words to not scramble those as well
        word = word.strip()
        punch = False
        if len(word) >= 4:
            # if there is punctuation, scramble the word without it, else,
            # just scramble all of the word
            if word.endswith(punctuation):
                scramble_this = list(word[1:-2])
                punch = True
            else:
                scramble_this = list(word[1:-1])
            random.shuffle(scramble_this)
            # if there is punctuation, also append it, else, just append
            # the scrambled result
            if punch:
                result.append('{0}{1}{2}{3}'.format(word[0],  
                              ''.join(scramble_this),  word[-2:], ' '))
            else:
                result.append('{0}{1}{2}{3}'.format(word[0],  
                              ''.join(scramble_this), word[-1], ' '))
        # shorter words don't need to be scrambled; nothing would change here.
        # so just directly append them to the result as they are
        else:
            if word.endswith(punctuation):
                result.append('{0}{1}{2}'.format(word[:-1], word[-1], ' '))
            else:
                result.append('{0}{1}'.format(word, ' '))
    # join all the scrambled words together to form a new string
    scrambled_text = ''.join(result)
    # stripping the tailing space behind the last word:
    scrambled_text = scrambled_text.strip()
    return scrambled_text


def scramble_all(text):
    """
    Reorders/scrambles all the characters in words in a text in a random way.
    
    Words here are defined as being separated by white spaces and remain 
    separated during the scrambling process.
    
    The function also takes care of punctuation, not scrambling it.
    
    Example:
        >>> scramble_all('Hello I am Alina')
        'hlole I ma nilaa'
        >>> scramble_all('Hello. I am: Alina')
        'lheol. I ma: ianal'
        >>> scramble_all('have a margherita')
        'vhae a gmtrarehai'
        
    Arguments:
        text: A string or integer containing characters that can be separated
        into words by white spaces.
    
    Returns:
        A new string in which all letters of the input words are scrambled.
        
    Raises:
        TypeError for texts that are not strings or integers.
        ValueError for len(text) <= 1.
    
    """
    if isinstance(text, str) == True:
        pass
    elif isinstance(text, int) == True:
        text = str(text)
    else:
        raise TypeError('Your input needs to be of type string or integer.')
    if len(text) <= 1:
        raise ValueError('Cannot scramble a text this short.')
    else:
        pass
    import random
    import string
    result = []
    punctuation = tuple(string.punctuation)
    words_list = text.split()
    for word in words_list:
        word = word.strip()
        punch = False
        if word.endswith(punctuation):
            scramble_this = list(word[:-1])
            random.shuffle(scramble_this)
            punch = True
        else:
            scramble_this = list(word)
            random.shuffle(scramble_this)
        if punch:
            result.append('{0}{1}{2}'.format(''.join(scramble_this),  
                          word[-1], ' '))
        else:
            result.append('{0}{1}'.format(''.join(scramble_this), ' '))
        scrambled_text = ''.join(result)
        scrambled_text = scrambled_text.strip()
    return scrambled_text

def scramble_shortwords(text, number = 4):
    """
    Reorders/scrambles all the characters in words that are shorter than a
    given number.
    
    Words here are defined as being separated by white spaces and remain 
    separated during the scrambling process.
    
    The function also takes care of punctuation, not scrambling it.
    
     Example:
        >>> scramble_all('Hello I am Alina')
        'Hello I ma Alina'
        >>> scramble_all('Hello. I am: Alina', 6)
        'lehlo. I ma: anial'
        >>> scramble_all('have a margherita', 5)
        'avhe a margherita'
        
    Arguments:
        text: A string containing characters that can be separated
        into words by white spaces.
        number: A chosable integer defining what the short words need to be
        shorter then. Default value is 4, meaning all words that are less
        then four characters will be scrambled.
    
    Returns:
        A new string in which all letters of the input words, that are
        shorter than a given number, are scrambled.
        
    Raises:
        TypeError for texts that are not strings.
        ValueError for len(text) <= 1.
        
    """
    if isinstance(text, str) == True:
        pass
    else:
        raise TypeError('Your input needs to be of type string.')
    if len(text) <= 1:
        raise ValueError('Cannot scramble a text this short.')
    else:
        pass
    import random
    import string
    result = []
    punctuation = tuple(string.punctuation)
    words_list = text.split()
    for word in words_list:
        word = word.strip()
        punch = False
        # This clause is added so that python doesn't think words that end with
        # punctuation are 1 letter longer than they acutally are:
        if word.endswith(punctuation):
            length = len(word)-1
        else:
            length = len(word)
        # in case the word is short/scramble-able, do the following:
        if length < number:
            if word.endswith(punctuation):
                # don't scramble punctuation:
                scramble_this = list(word[:-1])
                random.shuffle(scramble_this)
                punch = True
            else:
                scramble_this = list(word)
            random.shuffle(scramble_this)
            if punch:
                result.append('{0}{1}{2}'.format(''.join(scramble_this),  
                              word[-1], ' '))
            else:
                result.append('{0}{1}'.format(''.join(scramble_this), ' '))
        # in case the word is long, don't change it:
        else:
            result.append('{0}{1}'.format(word, ' '))
        scrambled_text = ''.join(result)
        scrambled_text = scrambled_text.strip()
    return scrambled_text

def random_uppercase(text):
    """
    Turns a random number of letters in a word into uppercase letters.
    
    Example:
        >>> random_uppercase('hello')
        'hEllO'
        >>> random_uppercase('hello')
        'heLLo'
        >>> random_uppercase('margherita')
        'MaeGHeRiTA'
        
    Arguments:
        text: A string containing characters that can be separated
        into words by white spaces.
    
    Returns:
        A new string in which a random amount of letters is capitalized.
        
    Raises:
        TypeError for texts that are not strings.
        ValueError for empty strings.
        
        
    """
    if isinstance(text, str) == True:
        pass
    else:
        raise TypeError('The text you want to scramble needs to be a string.')
    if len(text) < 1:
        raise ValueError('Cannot scramble a text without letters.')
    else:
        pass
    import random
    result = []
    words_list = text.split()
    for word in words_list:
        word = word.lower()
        # for each character n in each word in the list, choose randomly
        # whether to capitalize it, then reassemble the characters into words,
        # add a white space at the end, and append them to the result list:
        result.append('{0}{1}'.format(''.join(random.choice([n.upper(), n]) \
            for n in word), ' '))
    random_upper = ''.join(result)
    random_upper = random_upper.strip()
    return random_upper


# Here comes some very basic testing. Programs testing each function more
# rigorously are included in separate testing modules.   
if __name__ == '__main__':
    print('\n')
    print('Testing scramble_without_firstlast:')
    print('Sentence is: Hello. I am: Alina')
    print(scramble_without_firstlast('Hello. I am: Alina'))
    print('\n')
    print('Testing scramble_all:')
    print('Sentence is: Hello. I am: Alina')
    print(scramble_all('Hello. I am: Alina'))
    print('\n')
    print('Testing scramble_shortwords:')
    print('Sentence is: This is the result, the value of number being [...]')
    print(scramble_shortwords('This is the result, the value of number \
                              being 4.'))
    print(scramble_shortwords('This is the result, the value of number \
                              being 5.', 5))
    print('\n')
    print('Testing random_uppercase:')
    print('Sentence is: Hello. I am: Alina')
    print(random_uppercase('Hello. I am: Alina'))