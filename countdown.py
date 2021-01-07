#!/usr/bin/env python3
#
# Copyright 2020 Mustapha
#
# Licensed under the GNU Licencse, Version 3.0 (the "License");
# you may not use this file except in compliance with the License.
#

from utils.parser import parse
from utils.selector import pick
from utils.solver import check, recurse, solve
from utils.filter import output
from utils.logger import log, parameters


def main():

    # parse input
    args = parse()     

    # translate args into params
    numbers, target = args.numbers, args.target    
    SIZE, TOLERANCE = args.size, args.tolerance
    USE, SOLUTIONS, OUTPUT = args.use, args.solutions, args.output
    DEBUG = args.verbose >= 1
    SPAM = args.verbose >= 2

    # get numbers and crop to size
    if not numbers:
        numbers = pick(n_numbers=SIZE)
    else:
        numbers = numbers[:SIZE]

    # log inputs
    parameters(args,DEBUG)      
    log(numbers,'start numbers')
    log(target,'target')

    # solve problem
    solutions, approximations = solve(numbers=numbers,
                                    target=target,
                                    tolerance=TOLERANCE,
                                    use=USE,
                                    verbose=SPAM)

    # print results
    ## always print exact solutions 
    ## (all or unique values depending on desired ouput)
    output(values=solutions,
            displayname='exact solutions',
            output=OUTPUT,
            debug=DEBUG)
    ## print approximate solutions when required
    ## (all or unique values depending on desired ouput)
    if SOLUTIONS.upper() == 'APPROXIMATE':
        output(values=approximations,
                displayname='approximate solutions',
                output=OUTPUT,
                debug=DEBUG)


if __name__ == '__main__':
    main()