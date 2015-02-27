#!/usr/bin/env python

import sys
import argparse
from pdftools import pdf_insert
from pdftools.parseutil import parentparser


def process_arguments(args):
    parser = argparse.ArgumentParser(
        parents=[parentparser],
        description="Insert pages of one file in another."
    )
    # destination
    parser.add_argument('dest',
                        type=str,
                        help='destination pdf file')

    # source
    parser.add_argument('source',
                       type=str,
                       help='source pdf file')
    # output
    parser.add_argument('-o',
                        '--output',
                        type=str,
                        default=None,
                        help='filename of the output files, if None given '
                             'dest will be used as output')
    # pages
    parser.add_argument('-p',
                        '--pages',
                        nargs='+',
                        help='list of page numbers (start with 1) which will be'
                             ' inserted, if None all pages will be rotated '
                             '(default), Examples: 5 1-9 1- -9')
    # index
    parser.add_argument('-i',
                        '--index',
                        type=int,
                        default=None,
                        help='page number (start with 1) of destination file '
                             'where the pages will be inserted, if None they '
                             'will be added at the end of the file ')

    return parser.parse_args(args)


if __name__ == "__main__":
    args = process_arguments(sys.argv[1:])
    pdf_insert(args.dest, args.source, args.pages, args.index, args.output)
