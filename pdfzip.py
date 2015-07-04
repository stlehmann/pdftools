#!/usr/bin/env python

import sys
import argparse
from pdftools import pdf_zip
from pdftools.parseutil import parentparser


def process_arguments(args):
    parser = argparse.ArgumentParser(
        parents=[parentparser],
        description="Zip the pages of two documents in one output file.")

    # input1
    parser.add_argument('input1',
                        type=str,
                        help='first inputfile')
    # input2
    parser.add_argument('input2',
                        type=str,
                        help='second inputfile')
    # output
    parser.add_argument('-o',
                        '--output',
                        type=str,
                        default=None,
                        help='filename of the output file',
                        required=True)
    # delete
    parser.add_argument('-d',
                        '--delete',
                        action='store_true',
                        help='delete input files after merge')
    # revert
    parser.add_argument('-r',
                        '--revert',
                        action='store_true',
                        help='revert the pages of second input file')
    return parser.parse_args(args)


if __name__ == "__main__":
    args = process_arguments(sys.argv[1:])
    pdf_zip(args.input1, args.input2, args.output, args.delete, args.revert)
