def fizz_buzz_with_kwargs(count=30, start=1, increment=1, **fizzy_wds):
    """ Playing around with fizz-buzz and python I realized that you can unpack some arguments after arguments. This
    might be my most general fizz-buzz function.  It also catches bad arguments like trying to fizz-buzz on a string.
    :param count: The upper bound of the fizz-buzz, exclusive.  i.e. from [1, count)
    :param increment: range() step.  Defaults to 1.
    :param start: What number to start the fizz-buzz from.  Defaults to 1
    :param fizzy_wds: fizzy words to fizz-buzz.  If left empty, defaults to fizz at 3, buzz at 5. You can pass a
    fizz-buzz word as an argument, e.g. (sean=6, tim=4, holly=3), and it will print the argument on the value. If you
    want spaces in words, pass any non-defined argument name with a dict with the space.
    E.g. dummy={'f i z z': 3,'b u z z':5}
    """
    fizzy_wds = {"fizz": 3, "buzz": 5} if not bool(fizzy_wds) else fizzy_wds
    for k, v in fizzy_wds.copy().items():
        if isinstance(v, dict):
            # Finding dicts in arguments.
            fizzy_wds.update(v)
            fizzy_wds.pop(k, None)
        if not isinstance(v, int) and not isinstance(v, float):
            # Checking if the arguments are passed as numbers.
            fizzy_wds.pop(k, None)
    # Finally printing the fizzy words.
    for i in range(start, count, increment):
        line = str().join(word if i % multiple == 0 else "" for word, multiple in fizzy_wds.items())
        line += str(i) if len(line) == 0 else ""
        print(line)


def fizz_buzz_v1(fizz=3, buzz=5, count=30):
    """
    A naive fizz-buzz implementation.
    """
    i = 1
    while i < count:
        if i % fizz == 0:
            print("fizz", end='')
        if i % buzz == 0:
            print("buzz", end='')
        if not i % buzz == 0 and not i % fizz == 0:
            print(str(i), end='')
        print()
        i += 1


def fizz_buzz_explicit(fizz=3, buzz=5, count=30):
    """
    A naive fizz-buzz implementation that leverages some of python's coding practices.
    """
    for i in range(1, count):
        line = ""
        line += "fizz" if i % fizz == 0 else ""
        line += "buzz" if i % buzz == 0 else ""
        line += str(i) if len(line) == 0 else ""
        print(line)


def fizz_buzz_generic(fizzy_words={"fizz": 3, "buzz": 5}, count=30):
    """
    A fizz-buzz implementation that allows any definition of fizz-buzz words.
    """
    for i in range(1, count):
        line = str().join(word if i % multiple == 0 else "" for word, multiple in fizzy_words.items())
        line += str(i) if len(line) == 0 else ""
        print(line)


def fizz_buzz_v4(fizz=3, buzz=5, count=30):
    """
    I have no idea what I was trying to accomplish here...
    """

    def print_num(c, args):
        """ It was probably something to do with this? :param c: :param args: :return: True or False??
        """
        return max(1 if c % multiple == 0 else 0 for word, multiple in args.items()) < 1

    for i in range(1, count):
        if i % fizz == 0:
            print("fizz", end='')
        if i % buzz == 0:
            print("buzz", end='')
        if print_num(i, dict(fizz=3, buzz=5)):
            print(str(i), end='')
        print()
        i += 1


def fizz_buzz_one_line(fzy_wrds={"fizz": 3, "buzz": 5}, num=30):
    """FizzBuzz Code Golf"""
    print("\n".join("".join(w if i % m == 0 else "" for w, m in fzy_wrds.items()) if max(
        i % m == 0 for m in fzy_wrds.values()) > 0 else str(i) for i in range(1, num)))


if __name__ == "__main__":
    print('Testing FizzBuzzes')
    fizz_buzz_with_kwargs()
