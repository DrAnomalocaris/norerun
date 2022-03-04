# remember
Backup to store results of functions, so they do not need to be rerun.
As long as the function is unchanged, and the inputs are the same

```
from remember import remember
@remember
def len_file(textFile):
  #returns the number of characters in a text file
  with open(textFile) as f:
    return len(f.read())

#running len_file might take a few seconds depending on the file size
print(len_file("Alice_in_wonderland"))

#But now remember will keep track of the function being run with that input, and if asked again, the output would not need to be rerun again
print(len_file("Alice_in_wonderland"))

```
