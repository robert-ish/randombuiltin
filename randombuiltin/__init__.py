# AI Notice (???)
# I wrote basically all of it but ChatGPT helped me build some of it

import builtins
import random

python = builtins.__dict__
def randbuiltin():
    """Returns a random builtin."""
    f = random.choice(list(python.values()))
    return f

def randcallable():
    """Returns a random callable."""
    f = random.choice(list(python.values()))
    while not callable(f):
        f = random.choice(list(python.values()))
    return f

def randvalue():
    """Returns a random non-callable builtin."""
    f = random.choice(list(python.values()))
    while callable(f):
        f = random.choice(list(python.values()))
    return f

def randof(typ):
    """Returns a random builtin of a specific type."""
    matches = [
        f for f in python.values()
        if isinstance(f, typ)
    ]

    if not matches:
        raise ValueError(f"No builtin matching {typ}")

    return random.choice(matches)

def randpair():
    """Returns a random pair of Builtin Name, Builtin."""
    name = random.choice(list(python))
    return name, python[name]

def randcallablepair():
    """Returns a random pair of Builtin Name, CALLABLE Builtin."""
    f = randpair()
    while not callable(f[1]):
        f = random.choice(list(python.values()))
    return f

def randvaluepair():
    """Returns a random pair of Builtin Name, NON-CALLABLE Builtin."""
    f = randpair()
    while callable(f[1]):
        f = random.choice(list(python.values()))
    return f

def randofpair(typ):
    """Returns a random pair of Builtin Name, Builtin OF A SPECIFIC TYPE."""
    matches = [ #type: ignore
        f for f in python.keys(), python.values()
        if isinstance(f[1], typ)
    ]

    if not matches:
        raise ValueError(f"No builtin matching {typ}")

    return random.choice(matches)

def allof(typ):
    """Returns all found builtins of a specific type"""
    return [
        value
        for value in python.values()
        if type(value) == typ
    ]

def allofc(typ):
    """Returns all found builtins of a specific type (subtypes counted)"""
    return [
        value
        for value in python.values()
        if isinstance(value, typ)
    ]

def countof(typ) -> int:
    """Returns how many builtins there are of a specific type."""
    return len(allof(typ))

def countofc(typ) -> int:
    """Returns how many builtins there are of a specific type."""
    return len(allofc(typ))

def randcall(*args, attempts=999, **kwargs):
    """Calls a random builtin with the provided args until it works, tries for a certain amount of attempts, raises RuntimeError if couldnt call any builtin."""
    for _ in range(attempts):
        f = randcallable()

        try:
            return f(*args, **kwargs)
        except Exception:
            pass

    raise RuntimeError("No builtin worked")

def nameof(obj):
    """Gets the name of an object"""
    for name, value in python.items():
        if value is obj:
            return name
    return None
# i hate nameof i hate nameof i hate nameof i hate nameof i hate nameof  chatgpt forced me to do this
__all__ = [
    "randbuiltin",
    "randcallable",
    "randvalue",
    "randof",
    "randpair",
    "allof",
    "countof",
    "randcall"
]
# no im not putting NAMEOF into all
