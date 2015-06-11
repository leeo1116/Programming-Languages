__author__ = 'liangl2'

words = ["running", "cat", "window", "defenestrate"]
for w in words:
    print(w, len(w))

for w in words[:]:  # make a new of words
    if len(w) > 6:
        words.insert(0, w)
print(words)
"""
for w in words:  # in situ operation, can be trapped in infinite loop
    if len(w) > 6:
        words.insert(0, w)
print(words)
"""
# Fibonacci series
a, b = 0, 1
while b < 100:
    print(b, end=', ')
    a, b = b, a + b  # Simultaneous assignment, evaluate right hand operation first, then assign simultaneously (no order)
print('\n', end='')

for word_index in range(len(words)):
    print(word_index, words[word_index], end=", ")
print('\n', end='')

for word_index, word in enumerate(words):
    print(word_index, word, end=", ")
print('\n', end='')

print(list(range(5)))


def initlog(*args):
    pass


def fib(n):
    """Print a Fibonacci series up to n"""  # documentation string, or docstring
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()  # new line
    # no return value, will print None


fib(100000)

# pass value
def change_value(a):
    a = 10
    return a


b = 1
# b points to int object 1, and copy to a when invoke change_value, then a also points to int object 1,
# when assign a = 10, a will point to a new int object 10. So finally b doesn't change, a = 10
change_value(b)
print(b)

b = change_value(b)  # change b by pointing to the returned object
print(b)

# Renaming function
f = fib
print(f)
print(f(1000))


def fib2(n):
    """
    :rtype : list
    :param n: maximum Fibonacci element
    :return: result
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


f100 = fib2(100)
print(f100)

# Default argument values
def ask_ok(prompt, retries=4, complaint="Yes or no, please!"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        elif ok in ('n', 'no', 'nop', 'nope'):
            return False
        else:
            print(complaint)
        retries -= 1
        if retries < 0:
            raise OSError("Uncooperative user")

# ask_ok("Do u wanna exit?")

# when default argument is mutable, L will accumulate the values
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# Solution to default mutable arguments
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

f(a=10, L=list(range(9)))

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any ", kind, '?')
    print("-- I'm sorry, we're all out of ", kind)
    for arg in arguments:
        print(arg)
    print('-' * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ':', keywords[kw])
    for k, v in keywords.items():
        print(k, ':', v)  # not in order, may be multi-thread

# Arbitrary arguments list
cheeseshop("Limburger", "It's very runny, sir.", "It's really very, very runny, sir.", shopkeeper="Michael Palin", \
           client="John Clear", sketch="Cheese Shop Sketch")

def concat(*args, sep='/'):
    return sep.join(args)

print(concat("my", "name", "is", "Liang", "Li", sep=' '))

# Unpacking argument lists
print(list(range(3, 6)))
args = [3, 6]
print(list(range(*args)))

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, '!')

d = {"voltage": "four million", "state": "beeping", "action": "voom"}
parrot(**d)

# Syntactic sugar: lambda expression (restricted to a single expression)
def make_incrementor(n):
    return lambda x: x+n  # return function object

f = make_incrementor(42)
print(f(1))

pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
# key: specify a function to be called on each list element prior to making comparisons
pairs.sort(key=lambda pair: pair[1]) # sort by the second tuple value for each element

# Doc string
def my_func():
    """Concise summary

    Do nothing
    """
    pass

print(my_func.__doc__)
# Doc annotation
def f(ham: str, eggs: str = "eggs") -> str:
    print("Annotations: ", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham+" and "+eggs

f("hambergure", eggs="duck eggs")

# Looping
knights = {"gallhand": "the pure", "robin": "the brave"}
for k, v in knights.items():
    print(k, v)
for i, v in enumerate(["tic", "tac", "toe"]):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

def main():
    print("put main body inside this section")

if __name__ == "__main__":
    main()

import sys
print(dir(sys))