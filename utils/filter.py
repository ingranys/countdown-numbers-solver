#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Custom filter for countdown.

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


from sympy import sympify,srepr


def output(values,displayname='',output='unique',debug=False):
    """
    Filter and print output to console according to settings.
    
    Filtering is done following these 4 steps :
    1) Remove elements in the list that are exactly the same.
    2) Simplify mathematical expressions using sympy (remove unnecessary brackets).
    3) Convert expressions to graphs (or trees) that represent the operations in the mathematical expressions and ALWAYS in the same order.
    4) Store values in dictionnary using graphs as keys (filter duplicates automatically).

    Args:
        values (list[str]): List of strings to be filtered and printed.
        displayname (str, optional): Displayname to be printed to console. Defaults to ''.
        output (str, optional): Type of output. Defaults to 'unique'.
        debug (bool, optional): Enable DEBUG mode. Defaults to False.

    Raises:
        ValueError: In case that unexpected argument value is encountered.
    """
    
    # solver may find the same solution many times
    # we filter all duplicates before deep dive
    values = list(set(values))

    ## values might be different but still refering to the same set of operations
    ## SPOILER : we heavily rely on sympy librairies to filter out duplicates!
    # first we simplify mathematical expressions 
    # (remove unnecessary brackets and keep right-hand side only)
    simplified_expressions = [sympify(value.split(" =", 1)[0],evaluate=False) for value in values]
    
    # then we build expression trees that represent the set of operation in a conceptual manner
    # same solutions may have different simplified expressions but always have the same tree
    tree_expressions = ['{0}'.format(srepr(simplified_expression)) for simplified_expression in simplified_expressions]
    
    # now we can filter solutions putting all them in a dictionnary
    # and by using each corresponding expression tree as key
    unambiguous_solutions = {}
    for i in range(len(tree_expressions)):
        unambiguous_solutions[tree_expressions[i]] = values[i]


    # filtering is done > TIME TO PRINT OUTPUT

    ## print header according do displayname and filter
    if output.upper() in ['ALL','UNIQUE']:
        print('\n>>> {0} {1}'.format(output.upper(), displayname.upper()))
    else:
        # unepexted value for output arg
        raise ValueError('Unexpected value for the argument <output> : {0}'.format(output))

    ## more info when debug mode is enabled
    if debug:
        print('---------DEBUG---------')
        print('{0} | {1} | {2}'.format('SOLUTION','SIMPLIFIED EXPRESSION','EXPRESSION TREE'))
        for i in range(len(values)):
            print('{0} | {1} | {2}'.format(values[i],simplified_expressions[i],tree_expressions[i]))
        print('--------/DEBUG---------')

    ## print values depending on what is required
    ### output all solutions when required > VALUES
    if output.upper() == 'ALL':
        # verify if empty        
        if values:   
            for value in values:
                print(value)
        else:
            # print default message whem empty
            print('None found...')  
    ### output needs to be unique values > UNAMBIGUOUS SOLUTIONS
    elif output.upper() == 'UNIQUE':
        # verify if empty 
        if unambiguous_solutions:
            for _ ,value in unambiguous_solutions.items():
                print(value)    
        else :
            # print default message whem empty
            print('None found...')
    ### unepexted value for output arg
    else:
        raise ValueError('Unexpected value for the argument <output> : {0}'.format(output))