import pickle
from dis import dis
from os.path import exists
from io import StringIO

class norerun:
    def __init__(self,file=".bak"):
        self._file=file
        if exists(self._file):            
            with open(file, 'rb') as f:
                self._objects = pickle.load(f)
        else:
            self._objects={}     
    def _backup(self):
        with open(self._file,'wb') as f:
            pickle.dump(self._objects, f)              
    def format_key(self,func,args,kwargs):
            key=func.__name__
            key += "\n"+'#'*50+'\n'
            key += str(args)
            key += "\n"+'#'*50+'\n'
            longest_key=max([1]+[len(i) for i in kwargs.keys()])
            longest_val=max([1]+[len(str(i)) for i in kwargs.values()])
            for a,b in kwargs.items():
                a=f"{a}:"
                key+=f"{a: <{longest_key+2}}{b: <{longest_val+1}}{type(b)}"
            key += "\n"+'#'*50+'\n'
            with StringIO() as out:
                dis(func, file=out)
                key += out.getvalue()
            return key
    def __call__(self,func):
        def inner(*args, **kwargs):
            key = self.format_key(func, args, kwargs)
            if key in self._objects:
                return self._objects[key]
            else:
                 self._objects[key] = func(*args, **kwargs)
                 self._backup()
                 return self._objects[key]
        return inner 

    def flush(self):
        self._objects={}  
        self._backup()
        
        
norerun=norerun()
