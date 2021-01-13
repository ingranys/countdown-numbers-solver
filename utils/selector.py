#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Countdown Numbers Game selector.

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


from random import randint, sample

def pickFromBigNumbers(n_desired=-1):
    """
    Pick as many numbers as required in the set of big numbers {25,50,75,100}.
    Choose randomly between 0 and 4 if nothing is specified.

    Args:
        n_desired (int, optional): Number of desired numbers. Defaults to -1.

    Returns:
        list[int]: Generated list of numbers from the set of big numbers.
    """
    # build set of big numbers {25, 50, 75,100]}
    big_numbers = [25, 50, 75,100]

    # choose randomly when no value is specified
    if not n_desired >= 0:
        n_desired = randint(0,4)

    return sample(big_numbers, n_desired)


def pickFromSmallNumbers(n_desired:int):
    """
    Pick as many numbers as required in the set of small numbers {1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10}.

    Args:
        n_desired (int): Number of desired numbers.

    Returns:
        list[int]: Generated list of numbers from the set of small numbers.
    """
    # build set of small numbers
    # {1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10}
    smalls_numbers = [ i for i in list(range(1,10+1)) for _ in range(2) ]

    return sample(smalls_numbers, n_desired)


def pick(n_numbers=6,n_big=-1):
    """
    Generate numbers as specified.
    First pick 'n_big' from the set of big numbers. Default value is for random.
    Then pick as many numbers as necessary from the set of small numbers to get to 'n_numbers'. 

    Args:
        n_numbers (int, optional): Number of numbers to generate. Defaults to 6.
        n_big (int, optional): Number of big numbers to generate. Defaults to -1.

    Returns:
        list[int]: Generated list of numbers.
    """
    big_numbers = pickFromBigNumbers(n_big)

    return big_numbers + pickFromSmallNumbers(n_numbers - len(big_numbers))