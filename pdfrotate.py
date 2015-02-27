#!/usr/bin/env python

import sys
import argparse
from pdftools import pdf_rotate
from pdftools.parseutil import parentparser


def process_arguments(args):
    parser = argparse.ArgumentParser(
        parents=[parentparser],
        description="Rotate the pages of a PDF files by 90 degrees. ")
    # input
    parser.add_argument('input',
                        type=str,
                        default=None,
                        help='input file')
    # counterClockwise
    parser.add_argument('-c',
                        action='store_true',
                        dest='counter_clockwise',
                        help='rotate pages counterclockwise')

    # pages
    parser.add_argument('-p',
                        '--pages',
                        nargs='+',
                        default=None,
                        help='list of page numbers which will be rotated, '
                             'if None all pages will be rotated (default). '
                             'Examples: 5 1-9 1- -9')

    # output
    parser.add_argument('-o',
                        '--output',
                        type=str,
                        default=None,
                        help='name of the output file, if None the source file'
                             'will be overwritten')

    return parser.parse_args(args)


if __name__ == "__main__":
    args = process_arguments(sys.argv[1:])
    pdf_rotate(args.input, args.counter_clockwise, args.pages, args.output)
