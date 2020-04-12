# Python Assignment 2020 / Alina Podschun

A repository to store the files for the 2019/2020 "Introduction to python" final assignment. Author: Alina Podschun

## Getting started

### Prerequesites

You need an environment able to handle python code.

Concerning the packages used in the code, there is a *requirements.txt* file in this repository. If you don't already have them, please install those packages before running any code in this repository.

### Running the program(s)

All files correspond to assignment Nr. 1 (Scrambled text). 

All four functions are contained in the file *scrambled.py* . You can download it and run the code: There is some basic testing/examples of each function included at the end of the code, which will show you an example for each function if you run the code in the main namespace.

Alternatively, if you want to test the functions on your own text, you can additionally (!) download and run *demonstrate_scrambled.py* . When you run this program, you will be asked to input a sentence of your choice and can watch the program run the funcions on your sentence.

## Testing the functions

In this repository, there are files testing each function more thoroughly, all located in the [tests](tests) subfile:
* *test_scramble_all.py*
* *test_scramble_without_firstlast.py*
* *test_scramble_shortwords.py*
* *test_random_uppercase.py*

You can, of course, test each function individually by downloading and running the corresponding test module.

However, for this program I have also used code coverage and created a coverage report.
I have used the *coverage* package and included a file *coverage_scrambled.html* in this directory. Feel free to download it and open it with a browser of your choice. You can see that the only lines not coverd by tests are the example lines at the end of the code, which don't need to be tested and could have been excluded - I left them in for visualization's sake.

## Sources and further development

The sources I used for my code(s) are included in the *sources.md* file in this repository.
There is also a file *additional_info.md* explaining the reasoning behind my program, as well as giving suggestions for additional improvements or changes.

## License

Click [here](LICENSE) for the license file.
