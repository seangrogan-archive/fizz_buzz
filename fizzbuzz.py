p = print


def print(l=None, end='\n', doit=False):
    if doit:
        print(l, end=end)
    pass


def fizz_buzz_v1(fizz=3, buzz=5, count=30):
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
    for i in range(1, count):
        line = ""
        line += "fizz" if i % fizz == 0 else ""
        line += "buzz" if i % buzz == 0 else ""
        line += str(i) if len(line) == 0 else ""
        print(line)


def fizz_buzz_generic(fizzy_words={"fizz": 3, "buzz": 5}, count=30):
    for i in range(1, count):
        line = str().join(word if i % multiple == 0 else "" for word, multiple in fizzy_words.items())
        line += str(i) if len(line) == 0 else ""
        print(line)


def fizz_buzz_v4(fizz=3, buzz=5, count=30):
    def print_num(c, args):
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


def fizz_buzz_one_line(fizzy_words={"fizz": 3, "buzz": 5}, num=30):
    print("\n".join("".join(w if i % m == 0 else "" for w, m in fizzy_words.items()) if max(
        i % m == 0 for m in fizzy_words.values()) > 0 else str(i) for i in range(1, num)))


if __name__ == "__main__":
    times = {}
    import timeit

    times["fizz_buzz_v1"] = timeit.timeit(fizz_buzz_v1)
    times["fizz_buzz_explicit"] = timeit.timeit(fizz_buzz_explicit)
    times["fizz_buzz_generic"] = timeit.timeit(fizz_buzz_generic)
    times["fizz_buzz_v4"] = timeit.timeit(fizz_buzz_v4)
    times["fizz_buzz_one_line"] = timeit.timeit(fizz_buzz_one_line)


    def line(name, time, times):
        return f'{name:<{(2 + max(len(t) for t in times))}} : {time:f<.{4}}'


    v = max(len(line(name, time, times)) for name, time in times.items())
    p(f'+={"=":=<{v}}=+')
    [p(f"| {line(name, time, times)} |") for name, time in times.items()]
    p(f'+={"=":=<{v}}=+')
