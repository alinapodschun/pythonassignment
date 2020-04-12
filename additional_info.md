# Additional info

Additional info explaining the reasoning behind my program, as well as giving suggestions for additional improvements or changes.

## Reasoning behind the program

### Randomness

The functions in this program scramble TRULY randomly, in the sense that the result may, by chance, be the same as the original input. 
If you want to make sure every word is in fact different from the input word, you can add a loop, advising python to keep randomly changing letters until the result word does not resemble the input word.

### Input type

Right now, all functions allow integer input. *scramble_without_firstlast* and *scramble_all* also allow integer input, since it might be fun to scramble long numbers too. *scramble_shortwords* doesn't, because integers normally can't be split into units by white spaces. *random_uppercase* doesn't, because integers can't be capitalized. The functions return error messages for all other input types, but this of course, can be changed.

## Possible changes

### Capitalized Words

Capitalized input words, such as the first word in a sentence, or words that are names, are left capitalized right now (appart from the function *random_uppercase*, which will change every word to lower case before scrambling it). This means that the first word of a sentence, or names, will still contain one capitalized letter after being scrambled.
This is the way the Cambridge University experiment did it.

If you would like to have only lower letters in your words before scrambling them, you can for example add the line *text = text.lower()* 
before splitting your text into a list of words.

### Punctuation

I am not sure whether to think of apostrophes (such as in Let's, I'm..) as letters or as punctuation. Right now, in my program, punctuation is characters that can logically seperate or end sentences. Apostrophes don't do that, and thus are treated as characters.

If they should rather be treated as punctuation, meaning they stay in place when the word get's scrambled, the variable *punctuation* can be appended by the apostrophe character.

### Random_Uppercase

An improvement could be made by allowing the user to choose how many letters should be randomly capitalized. The function than would have to take a second argument, an integer, defining the number of letters to be capitalized.