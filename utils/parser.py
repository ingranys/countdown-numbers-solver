#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Custom parser for countdown.

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


from argparse import ArgumentParser
from random import randint


def parse():  
    """
    Parse given arguments according to countdown specifications.
    - Defines arguments names.
    - Verify argument type and limitation on number of values.
    - Verify that values are contained in given choices.
    - Set argument to default when no value is given.
    - Provide usage and help menu.

    Returns:
        argparse.Namespace: Object containing parsed arguments.
    """
  
    parser = ArgumentParser(description="Countdown numbers solver.")
    parser.add_argument(
        "-n",
        "--numbers",
        type=int,
        nargs='*',
        default=None,
        choices=[1,2,3,4,5,6,7,8,9,10,25,50,75,100],
        help="numbers to be used to reach target, "\
            "must be in [1|2|3|4|5|6|7|8|9|10|25|50|75|100] "\
            "(default is random)",
        metavar=''
    )
    parser.add_argument(
        "--size",
        type=int,
        nargs='?',
        default=6,
        choices=range(3,10+1),
        help="maximum number or values to be used (default is 6)",
        metavar='3..10'
    )
    parser.add_argument(
        "-u",
        "--use",
        type=str,
        nargs="?",
        choices=['all','some'],
        default='some',
        help="rule for using numbers (default is 'some')",
        metavar = 'all|some'
    )
    parser.add_argument(
        "-t",
        "--target",
        type=int,
        nargs="?",
        choices=range(100, 999+1),
        default=randint(100,999),
        help="target value (default is random)",
        metavar='100..999'
    )
    parser.add_argument(
        "-s",
        "--solutions",
        type=str,
        nargs="?",
        choices=['approximate','exact'],
        default="exact",
        help="type of authorized answers (default is 'exact')",
        metavar='approximate|exact'
    )
    parser.add_argument(
        "--tolerance",
        type=int,
        nargs="?",
        choices=range(1,10+1),
        default=10,
        help="tolerance range for approximate solutions (default is 10)",
        metavar='1..10'
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        nargs="?",
        choices=['all','unique'],
        default="unique",
        help="solutions to output (default is 'unique')",
        metavar='all|unique'
    )
    parser.add_argument(
        "-v",
        "--verbose",
        type=int,
        nargs="?",
        choices=range(0,3),
        default=0,
        help="verbose level for logging (default is 0)",
        metavar='0|1|2'
    )
    args = parser.parse_args()

    return args