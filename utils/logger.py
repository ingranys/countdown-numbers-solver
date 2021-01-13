#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Custom logger for countdown.

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


def log(title: str, obj):
    """
    Print information to the console.

    Args:
        title (str): Title to be printed.
        obj :  Object to be printed.  
    """
    print('\n>>> {0} {1}'.format(title.upper(), obj))


def parameters(args,debug=False):
    """
    Print meaningful information about given arguments.

    Args:
        args (argparse.Namespace): Object containing parsed arguments.
        debug (bool, optional): Enable DEBUG mode. Defaults to False.

    Raises:
        ValueError: In case that unexpected argument value is encountered.
    """
    print('\n>>> PARAMETERS')
    
    # numbers info and size info
    if args.numbers:
        print('Input number(s) : {0}.'.format(args.numbers))
        print('The first {0} number(s) will be considered.'.format(args.size))
    else:
        print('Input number(s) :'\
            ' None given (numbers will be picked randomly).')
    
    # target and use info
    print('The goal is to reach {0} using {1} numbers.'.format(args.target,args.use))

    # solutions
    if args.solutions.upper() == 'EXACT':
        print('We are looking for exact solutions only.')
    elif  args.solutions.upper() == 'APPROXIMATE':
        print('We are looking for exact and approximate solutions' \
                ' (tolerance is {0}).'.format(args.tolerance))
    else :
        raise ValueError('Unexpected value for the argument <solutions> : {0}'.format(args.solutions))

    # output
    if args.output.upper() == 'UNIQUE':
        print('We will filter duplicates and display unique solutions.')    
    elif args.output.upper() == 'ALL':
        print('We will display all solutions, even duplicates' \
                ' (operations order will differ).')
    else:
        raise ValueError('Unexpected value for the argument <output> : {0}'.format(args.output))

    # verbose info    
    if args.verbose == 0:
        pass    
    elif args.verbose == 1:
        print('DEBUG mode has been enabled.')    
    elif args.verbose == 2:
        print('DEBUG mode has been enabled.')
        print('!!!SPAM mode has been enabled!!!')    
    else:
        raise ValueError('Unexpected value for the argument <verbose> : {0}'.format(args.verbose))

    # show technical details if DEBUG mode is enabled
    if debug:
        print('\n---------DEBUG---------')
        print('Technical details about args :')
        for arg in vars(args):
            print(arg, getattr(args, arg))
        print('--------/DEBUG---------')