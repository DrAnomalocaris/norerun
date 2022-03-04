# remember
Backup to store results of functions, so they do not need to be rerun.
As long as the function is unchanged, and the inputs are the same

```
from remember import remember
@remember
def count(n):
  for i in range(n):
    pass
  return i

count(1000000000) #this is going to take a few seconds

count(1000000000) #now this is inmediate
```
