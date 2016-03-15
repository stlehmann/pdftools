#!/usr/bin/env python
"""
pdfcopy.py,
copyright (c) 2016 by Stefan Lehmann

"""
import sys
import argparse
from pdftools.pdftools import pdf_copy
from pdftools.parseutil import parentparser


def process_arguments(args):
    parser = argparse.ArgumentParser(
        parents=[parentparser],
        description="Copy specific pages of a PDF file in a new file."
    )
    # input
    parser.add_argument('input',
                        type=str,
                        default=None,
                        help='input file containing the source pages')
    # output
    parser.add_argument('-o',
                        '--output',
                        type=str,
                        default=None,
                        help='filename of the output file')
    # stepsize
    parser.add_argument('-p',
                        '--pages',
                        dest='pages',
                        type=str,
                        nargs='+',
                        default=1,
                        help='list of pages to copy in the new file. '
                             'Examples: \n'
                             '"5 8 10": Pages 5, 8, 10; '
                             '"1-9":    Pages 1 to 9; '
                             '"5-":     Pages from 5 to last page; '
                             '"-9":     Pages from beginning to 9'
                        )

    parser.add_argument('-y',
                        action='store_true',
                        help='yes to all'
                        )

    return parser.parse_args(args)


if __name__ == "__main__":
    args = process_arguments(sys.argv[1:])
    pdf_copy(args.input, args.output, args.pages, args.y)
