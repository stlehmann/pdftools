#! python3

import sys
import argparse
from pdftools import parentparser, pdf_rotate


def process_arguments(args):
    parser = argparse.ArgumentParser(
        parents=[parentparser],
        description="Rotate the pages of multiple input files by 90 degrees. "
                    "Wildcards can be used.")
    #input
    parser.add_argument('inputs',
                        type=str,
                        default=None,
                        nargs='+',
                        help='list of input files')
    #counterClockwise
    parser.add_argument('-c',
                        action='store_true',
                        dest='counter_clockwise',
                        help='rotate pages counterclockwise')

    return parser.parse_args(args)


if __name__ == "__main__":
    args = process_arguments(sys.argv[1:])
    pdf_rotate(args.inputs, args.counter_clockwise)
