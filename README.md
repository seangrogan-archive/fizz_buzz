# `fizzbuzz`
A testbed to try different fizz buzz coding practices.

## Recent results:

| Code | `timeit` time<br>(sec, probably) |
|:---| ---: |
| fizz_buzz_v1         | 20.88 |
| fizz_buzz_explicit   | 17.87 |
| fizz_buzz_generic    | 63.87 |
| fizz_buzz_v4         | 82.15 |
| fizz_buzz_one_line   | 60.34 |

## Functions

`fizz_buzz_v1` :  A naive fizz-buzz implementation.

`fizz_buzz_explicit` : A naive fizz-buzz implementation that leverages some of python's coding practices.

`fizz_buzz_generic` :  A fizz-buzz implementation that allows any definition of fizz-buzz words.

`fizz_buzz_one_line` : FizzBuzz Code Golf

`fizz_buzz_with_kwargs` : Playing around with fizz-buzz and python I realized that you can unpack some arguments after arguments. This 
    might be my most general fizz-buzz function.  It also catches bad arguments like trying to fizz-buzz on a string.
    :param count: The upper bound of the fizz-buzz, exclusive.  i.e. from [1, count)
    :param increment: range() step.  Defaults to 1.
    :param start: What number to start the fizz-buzz from.  Defaults to 1
    :param fizzy_wds: fizzy words to fizz-buzz.  If left empty, defaults to fizz at 3, buzz at 5. You can pass a 
    fizz-buzz word as an argument, e.g. (sean=6, tim=4, holly=3), and it will print the argument on the value. If you 
    want spaces in words, pass any non-defined argument name with a dict with the space. 
    E.g. dummy={'f i z z': 3,'b u z z':5}