#! python3

import sys
import argparse
from pdftools import pdf_split


def process_arguments(args):
    parser = argparse.ArgumentParser(description="Split a PDF file in multiple documents.")
    #input
    parser.add_argument('input',
                        type=str,
                        default=None,
                        help='input file that shall be splitted')
    #output
    parser.add_argument('-o',
                        '--output',
                        type=str,
                        default=None,
                        help='filename of the output files')
    #stepsize
    parser.add_argument('-s',
                        '--stepsize',
                        dest='stepsize',
                        type=int,
                        default=1,
                        help='defines how many pages are packed in one file')

    return parser.parse_args(args)


if __name__ == "__main__":
    args = process_arguments(sys.argv[1:])
    pdf_split(args.input, args.output, args.stepsize)
