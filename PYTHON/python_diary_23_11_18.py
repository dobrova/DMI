Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars ()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> __builtins__.input.__doc__
'input([prompt]) -> value\n\nEquivalent to eval(raw_input(prompt)).'
>>> print __builtins__.input.__doc__
input([prompt]) -> value

Equivalent to eval(raw_input(prompt)).
>>> from math import sin
>>> vars ()
{'__builtins__': <module '__builtin__' (built-in)>, '__doc__': None, '__name__': '__main__', '__package__': None, 'sin': <built-in function sin>}
>>> print sin.__doc__
sin(x)

Return the sine of x (measured in radians).
>>>  import math
 
  File "<pyshell#6>", line 1
    import math
    ^
IndentationError: unexpected indent
>>> import math
>>> vars ()
{'__builtins__': <module '__builtin__' (built-in)>, '__doc__': None, '__name__': '__main__', '__package__': None, 'sin': <built-in function sin>, 'math': <module 'math' (built-in)>}
>>> math.exp
<built-in function exp>
>>> print math.exp.__doc__
exp(x)

Return e raised to the power of x.
>>> import math as matematika
>>> vars ()
{'__builtins__': <module '__builtin__' (built-in)>, 'matematika': <module 'math' (built-in)>, '__doc__': None, '__name__': '__main__', '__package__': None, 'sin': <built-in function sin>, 'math': <module 'math' (built-in)>}
>>> matematika.log.__doc__
'log(x[, base])\n\nReturn the logarithm of x to the given base.\nIf the base not specified, returns the natural logarithm (base e) of x.'
>>> math.log(10,10)
1.0
>>> sin(5)
-0.9589242746631385
>>> from math import sin as sinuss
>>> sinuss(5)
-0.9589242746631385
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/home/user/DMI/PYTHON/zimesana1.py", line 3, in <module>
    import matplotlib.font_manager as fm
ImportError: No module named matplotlib.font_manager
>>> import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()



Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    import matplotlib.pyplot as plt
ImportError: No module named matplotlib.pyplot
>>> import matplotlib

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    import matplotlib
ImportError: No module named matplotlib
>>> 
