from random import randint, sample

def pickFromBigNumbers(n_desired=-1):
    # build set of big numbers {25, 50, 75,100]}
    big_numbers = [25, 50, 75,100]

    # choose randomly when no value is specified
    if not n_desired >= 0:
        n_desired = randint(0,4)

    return sample(big_numbers, n_desired)


def pickFromSmallNumbers(n_desired):
    # build set of small numbers
    # {1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10}
    smalls_numbers = [ i for i in list(range(1,10+1)) for _ in range(2) ]

    return sample(smalls_numbers, n_desired)


def pick(n_numbers=6,n_big=-1):
    big_numbers = pickFromBigNumbers(n_big)

    return big_numbers + pickFromSmallNumbers(n_numbers - len(big_numbers))