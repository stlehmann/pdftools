#!/usr/bin/env python

import sys
import argparse
from pdftools import pdf_merge
from pdftools.parseutil import parentparser


def process_arguments(args):
    parser = argparse.ArgumentParser(
        parents=[parentparser],
        description="Merge the pages of multiple input files in one output file.")
    # input
    parser.add_argument('inputs',
                        type=str,
                        default=None,
                        nargs='+',
                        help='list of input files')

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

    return parser.parse_args(args)


if __name__ == "__main__":
    args = process_arguments(sys.argv[1:])
    pdf_merge(args.inputs, args.output, args.delete)
