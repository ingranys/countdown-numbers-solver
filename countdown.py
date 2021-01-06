#!/usr/bin/env python3
#
# Copyright 2020 Mustapha
#
# Licensed under the GNU Licencse, Version 3.0 (the "License");
# you may not use this file except in compliance with the License.
#



### Interesting Examples 
## Many cases
#numbers = [8,3,2,9,7,5]
#target = 905
## Only off-by-1 answers
#numbers = [100,75,50,25,1,3]
#target = 823
## Many answers
#numbers = [50,75,25,5,4,9]
#target = 201
## Only one answer
#numbers = [9,3,5,3,2,4]
#target = 669
## Compare http://www.maths-resources.com/countdown/index.html


from utils.parser import parse
from utils.selector import pick
from utils.solver import check, recurse, solve
from utils.filter import output
from utils.logger import log


def main():

    # parse input and log args
    args = parse()
    log(args,'args')   

    # translate args into params
    numbers, target = args.numbers, args.target    
    SIZE, TOLERANCE = args.size, args.tolerance
    USE, SOLUTIONS, OUTPUT = args.use, args.solutions, args.output

    # check inputs and apply control
    if not numbers:
        numbers = pick(n_numbers=SIZE)
    else:
        numbers = numbers[:SIZE]
    log(numbers,'start numbers')
    log(target,'target')

    # solve problem
    solutions, approximations = solve(numbers,target,TOLERANCE,USE,verbose=False)

    # print results
    output(solutions,'exact solutions',output=OUTPUT)
    if SOLUTIONS.upper() == 'APPROXIMATE':
        output(approximations,'approximate solutions',output=OUTPUT)


if __name__ == '__main__':
    main()