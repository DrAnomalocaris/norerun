# remember
Backup to store results of functions, so they do not need to be rerun.
As long as the function is unchanged, and the inputs are the same.

```
from norerun import norerun
@norerun
def count(n):
  for i in range(n):
    pass
  return i

count(1000000000) #this is going to take a few seconds

count(1000000000) #now this is inmediate
```

A hidden pickle file is created in the current working directory ".bak".
It can be deleted to reset the memory, or `norerun.flush()` will do the same.


Easy install with `pip install norerun`

