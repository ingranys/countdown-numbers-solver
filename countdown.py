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
__date__ = "2021/01/07"
__deprecated__ = False
__email__ =  "ingranys@protonmail.com"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.4.0"


from utils.parser import parse
from utils.selector import pick
from utils.solver import check, recurse, solve
from utils.filter import output
from utils.logger import log, parameters


def main():
    """
    Main function for 'countdown.py'.
    - Parse arguments and set options
    - Log useful information about arguments
    - Start solver
    - Output results
    """

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
    log('start numbers',numbers)
    log('target',target)

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