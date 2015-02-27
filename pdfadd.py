#!/usr/bin/env python


import sys
import argparse
from pdftools import pdf_add
from pdftools.parseutil import parentparser


def process_arguments(args):
    parser = argparse.ArgumentParser(
        parents=[parentparser],
        description="Add pages from a source file to an output PDF file. "
                    "If the output file does not exist a new file will be "
                    "created.")

    # destination
    parser.add_argument('dest',
                        type=str,
                        help='destination pdf file')

    # source
    parser.add_argument('source',
                        type=str,
                        default=None,
                        help='pdf source file')

    # pages
    parser.add_argument('-p',
                        '--pages',
                        nargs='+',
                        help='list of pages to add to the output. '
                             'Examples: 5 1-9 1- -9')
    # output
    parser.add_argument('-o',
                        '--output',
                        type=str,
                        default=None,
                        help='name of the output file, if None the destination'
                             'file will be overwritten')

    return parser.parse_args(args)


if __name__ == "__main__":
    args = process_arguments(sys.argv[1:])
    pdf_add(args.dest, args.source, args.pages, args.output)
