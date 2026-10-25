# randombuiltin
The name is self-explanatory, gets random builtins.
## Installation
```powershell
pip install randombuiltin
```
## Documentation
do i just paste the docstrings in here
### randbuiltin()
Returns a random builtin.
### randcallable()
Returns a random callable.
### randvalue()
Returns a random non-callable builtin.
### randof(typ)
Returns a random builtin of a specific type.
### randpair()
Returns a random pair of Builtin Name, Builtin.
### randcallablepair()
Returns a random pair of Builtin Name, CALLABLE Builtin.
### randvaluepair()
Returns a random pair of Builtin Name, NON-CALLABLE Builtin.
### randofpair(typ)
Returns a random pair of Builtin Name, Builtin OF A SPECIFIC TYPE.
### allof(typ)
Returns all found builtins of a specific type
### allofc(typ)
Returns all found builtins of a specific type (subtypes counted)
### countof
Returns how many builtins there are of a specific type.
### randcall(*args, attemps=999, **kwargs)
Calls a random builtin with the provided args until it works, tries for a certain amount of attempts, raises RuntimeError if couldnt call any builtin.
### nameof(obj)
*Sigh* Gets the name of an object...

## License
MIT.