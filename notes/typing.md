# Forward References

When referring to a type before it's been defined you can use forward references to tell the interpreter to re-process the type annotation later.  This is done by wrapping type annotation in a string like so:

```python
class Node:
    def __init__(self, head: Node): pass # Will result in errors
    def __init__(self, head: "Node"): pass # Forward references
```

This feature is officially documented in [PEP 484](https://www.python.org/dev/peps/pep-0484/#forward-references).

## Interesting Insights
According to the PEP 484 documentation on [problems with the forward reference implementation](https://www.python.org/dev/peps/pep-0484/#the-problem-of-forward-declarations), this suboptimal edge case where strings are used to invoke a forward reference instead of the feature being inherently supported by the normal typing syntax is the current reality because Python classes do not become defined until the entire body of the class has been executed.