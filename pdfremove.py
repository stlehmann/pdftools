#!/usr/bin/env python


import sys
import argparse
from pdftools import pdf_remove
from pdftools.parseutil import parentparser


def process_arguments(args):
    parser = argparse.ArgumentParser(
        parents=[parentparser],
        description="Remove pages from a PDF file.")
    # input
    parser.add_argument('source',
                        type=str,
                        default=None,
                        help='pdf source file')

    # pages
    parser.add_argument('-p',
                        '--pages',
                        nargs='+',
                        required=True,
                        help='list of pages to remove from file. '
                             'Examples: 5 1-9 1- -9')
    # output
    parser.add_argument('-o',
                        '--output',
                        type=str,
                        default=None,
                        help='name of the output file, if None the source file '
                             'will be overwritten')

    return parser.parse_args(args)


if __name__ == "__main__":
    args = process_arguments(sys.argv[1:])
    pdf_remove(args.source, args.pages, args.output)
