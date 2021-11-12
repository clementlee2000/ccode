My go at the [ccode assesment](https://github.com/ChromaCodeINC/challenge-core-methods).

The tool runs in Python3 venv with no dependencies besides pytest.
The three main parts are importing plate.json data, processing data to find the 
max first and second derivative cycles, and outputing the data as a csv.

##### If only allowed 90 minutes:

* All functions would be in main.py
* Lists generated in nested `for` instead of list comprehension
* No real tests (besides 'if extension == <filetype>' and data type checks)

##### Some things I learned:
* pytest
* Zip and list comprehension are neat
* Using with() instead of fopen and forgetting to close
* more pythonic ways to do things, other anti patterns
* Probably ought to write more comments as I go even though I tried to use verbose variable names
* write csv on Windows adds carriage returns for some reason?
##### from the review:
* fail more loudly since python catches exceptions well
* no point in catching and raising the wrong error
* find max twice would be more readable than find maxima 
* don't overthink / add 'future-proof' code before thinkign about current usage (e.g. filetype ext checkers will leave 
  users wondering where their file is since there are no errors)
* report errors or crash where errors happen, don't pass it around and make debugging any harder
  
##### For a full project:

* Support other file_io formats
* process_data could have fxn for central derivative implementation, or fit sigmoid
* More pytests

