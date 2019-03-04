# default argument values
# definition: it is possible to assaign a default value to some parameters
# (AFTER THE POSITIONALS ONES)


def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint


# default argument values
# call: the values are still passed positionally, but the parameters with a
# default can be omitted
ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


# keyword arguments
# definition: same as the default parameters
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"


# keyword arguments
# call: only positional parameters are mandatory, the keyword ones, that
# must follow, can be called in any order or omitted
parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
# wrong call methods:
# parrot() # required argument missing
# parrot(voltage=5.0, 'dead') # non-keyword argument after a keyword argument
# parrot(110, voltage=220) # duplicate value for the same argument
# parrot(actor='John Cleese') # unknown keyword argument
