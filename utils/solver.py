#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Countdown Numbers Game solver.

For more information, see README.

For usage, use help menu <python3 countdown.py -h>.

Project can be found here <https://github.com/ingranys/countdown-numbers-solver>.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "ingranys"
__contact__ = "ingranys@protonmail.com"
__copyright__ = "Copyright 2021, Mustapha Gaies, Toulouse (France)"
__date__ = "2021/01/13"
__deprecated__ = False
__email__ =  "ingranys@protonmail.com"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.4.2"


# lamdba functions
add = lambda a,b: a+b
sub = lambda a,b: a-b if a>b else None
osub = lambda a,b: b-a if b>a else None
mul = lambda a,b: a*b
div = lambda a,b: a//b if a % b == 0 else None
idiv = lambda a,b: b//a if b % a == 0 else None

# available operation
operations = [ (add, '+',   '({0} + {1})'),
               (sub, '-',   '({0} - {1})'),
               (osub,'^-', '({1} - {0})'),
               (mul, '*',   '({0} * {1})'),
               (div, '/',   '({0} / {1})'),
               (idiv, '^/', '({1} / {0})')]


def check(numbers,expressions,target,solutions,approximations,tolerance=10,use='some',verbose=False,stage=''):
    """
    Check if numbers contain a solution (either exact or approximate).
    When a solution is encountered, add to the list (either 'solutions' for exact solutions or 'approximatations' for approximate solutions).

    Args:
        numbers (list[int]): List of numbers to checked.
        expressions (list[str]): List of corresponding mathematical expressions.
        target (int): Target value, a number is a solution if close enough to target.
        solutions (list[str]): List of exact solutions.
        approximations (list[str]): List of approximate solutions.
        tolerance (int, optional): Tolerance range when looking for approximate solutions. Defaults to 10.
        use (str, optional): Rule for numbers to be used. Defaults to 'some'.
        verbose (bool, optional): Enable DEBUG mode. Defaults to False.
        stage (str, optional): Log level ('--- ', '------ ', '--------- ' and so on). Defaults to ''.
    """

    # enforce rule on number usage before checking numbers for a potential solution
    ## use='some' > we can look for a solution no matter how many numbers are remaining
    ## use='all' > make sure there is no remaining numbers before looking for a solution
    if use.upper() == 'SOME' or (use.upper() == 'ALL' and len(numbers)==1):

        # we always look for both exact and approximate solutions
        # if we find one, we store the mathematical expression used to find the solution (set of operations)

        ## look for an exact solution
        if target in numbers:
            target_index = numbers.index(target)
            solution = '{0} = {1}'.format(expressions[target_index],numbers[target_index])
            solutions.append(solution)
            print('{0} EXACT SOLUTION FOUND : {1}'.format(stage,solution)) if verbose else False

        ## look for an approximate solution
        for number in numbers:
            ## consider approximate solution that are not exact solution (number must be different from target)
            if (number in list(range(target - tolerance,target + tolerance + 1))) and (number!=target):
                approx_index = numbers.index(number)
                approximation = '{0} = {1}'.format(expressions[approx_index],numbers[approx_index])
                approximations.append(approximation)
                print('{0} APPROXIMATE SOLUTION FOUND : {1}'.format(stage,approximation)) if verbose else False


def recurse(numbers,expressions,target,solutions,approximations,tolerance=10,use='some',verbose=False,stage=''):
    """
    Main function for the solver, most of the algorithm is implemented here.
    -Iterate through every unique pairs of elements in input numbers and apply operations all possible operations. 
    -Make recursive call on the newly generated values.

    Args:
        numbers (list[int]): List of input numbers to used.
        expressions ([type]): List of mathematical expressions for numbers.
        target (int): Target value, the goal is to reach that value.
        solutions ([type]): List that will contain exact solutions.
        approximations ([type]): List that will contain approximate solutions.
        tolerance (int, optional): Tolerance range when looking for approximate solutions. Defaults to 10.
        use (str, optional): Rule for numbers to be used. Defaults to 'some'.
        verbose (bool, optional): Enable DEBUG mode. Defaults to False.
        stage (str, optional): Log level ('--- ', '------ ', '--------- ' and so on). Defaults to ''.
    """

    n_numbers = len(numbers)            # will be useful to implement loops over number
    new_stage = stage.strip() + '--- '  # crank up log level at each recursive call

    # first check if numbers cocntains solutions
    check(numbers=numbers,
            expressions=expressions,
            target=target,
            solutions=solutions,
            approximations=approximations,
            tolerance=tolerance,
            use=use,
            verbose=verbose,
            stage=new_stage)

    # keep on computing while two or more numbers left    
    if n_numbers > 1:
        print('{0} Current number(s) {1} corresponding to the following expression(s) {2}'.format(new_stage,numbers,expressions)) if verbose else False
        # go through all unique pairs in the list (order is ignored)
        for i in range(n_numbers):
            for j in range(i+1,n_numbers):
                # apply each possible operations to these two numbers
                # (+) > add, (-) > substract, (^-)> switch order then substract ,(x) > multiply, (/) > divide, (/) > switch order then divide 
                # applying (^-) and (^/) allow us to ignore order when picking pair of number which saves time   
                for op in operations:
                    print('{0} Apply operation ({1}) to numbers of indexes (i={2},j={3}) in {4}'.format(new_stage,op[1],i,j,numbers)) if verbose else False
                    operand = op[0]

                    updated_numbers = numbers[:]                  
                    updated_numbers[i]= operand(numbers[i],numbers[j])
                    del updated_numbers[j]                

                    updated_expressions = expressions[:]
                    updated_expressions[i] = op[2].format(updated_expressions[i], updated_expressions[j])
                    del updated_expressions[j]

                    print('{0} Number(s) become(s) {1} corresponding to the following expression(s) {2}'.format(new_stage,updated_numbers,updated_expressions)) if verbose else False

                    # check that newly computed number is valid
                    if None not in updated_numbers:
                        # valid > next recursive call
                        recurse(numbers=updated_numbers,
                                expressions=updated_expressions,
                                target=target,
                                solutions=solutions,
                                approximations=approximations,
                                tolerance=tolerance,
                                use=use,
                                verbose=verbose,
                                stage=new_stage)
                    else:
                        # not valid > stop because of the rules (all values must be postive integers at any given time)
                        print('{0} STOP. Unauthorized expression...'.format(new_stage)) if verbose else False
    
    # no more numbers to crunch > time to stop
    else:
        print('{0} FINAL VALUE is {1} corresponding to this expression {2}'.format(new_stage,numbers,expressions)) if verbose else False



# start solver
def solve(numbers,target,tolerance=10,use='some',verbose=False):
    """
    Start solver.
    Initialize lists that will contain mathematical expressions and solutions.
    Launch the first recursive call of all.


    Args:
        numbers (list[int]): List of input numbers to used.
        target (int): Target value, the goal is to reach that value.
        tolerance (int, optional): Tolerance range when looking for approximate solutions. Defaults to 10.
        use (str, optional): Rule for numbers to be used. Defaults to 'some'.
        verbose (bool, optional): Enable DEBUG mode. Defaults to False.

    Returns:
        (list[int],list[int]): List of solutions (exact solutions and approximate solutions).
    """

    # initialize lists for results
    expressions = numbers[:]
    solutions = []
    approximations = []

    # launch recursive call
    recurse(numbers=numbers,
            expressions=expressions,
            target=target,
            solutions=solutions,
            approximations=approximations,
            tolerance=tolerance,
            use=use,
            verbose=verbose)

    return solutions, approximations