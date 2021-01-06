from argparse import ArgumentParser
from random import randint

def parse():  
  
    parser = ArgumentParser(description="Countdown numbers solver.")
    parser.add_argument(
        "-n",
        "--numbers",
        type=int,
        nargs='*',
        default=None,
        choices=[1,2,3,4,5,6,7,8,9,10,25,50,75,100],
        help="the numbers to use to reach target",
        metavar=''
    )
    parser.add_argument(
        "--size",
        type=int,
        nargs='?',
        default=6,
        choices=range(3,10+1),
        help="the size of the set of numbers to use (default is 6)",
        metavar='3:10'
    )
    parser.add_argument(
        "-u",
        "--use",
        type=str,
        nargs="?",
        choices=['all','some'],
        default='some',
        help="the rule for the numbers to use (default is 'some')"
    )
    parser.add_argument(
        "-t",
        "--target",
        type=int,
        nargs="?",
        choices=range(100, 999+1),
        default=randint(100,999),
        help="the target value (default is random)",
        metavar='100:999'
    )
    parser.add_argument(
        "-s",
        "--solutions",
        type=str,
        nargs="?",
        choices=['exact','approximate'],
        default="exact",
        help="the authorized answers, (default is 'exact')"
    )
    parser.add_argument(
        "--tolerance",
        type=int,
        nargs="?",
        choices=range(1,10+1),
        default=10,
        help="the tolerance range around target when looking for approximate solutions, (default is 10)",
        metavar='1:10'
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        nargs="?",
        choices=['all','unique'],
        default="unique",
        help="the solutions to output, (default is 'unique')"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        type=int,
        nargs="?",
        choices=range(0,3),
        default=0,
        help="the verbose level for logging, (default is 0)"
    )
    args = parser.parse_args()

    return args