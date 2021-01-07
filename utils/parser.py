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