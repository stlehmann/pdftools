#! python3

import sys
import argparse
from pdftools import parentparser, pdf_insert


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
                        type=int,
                        nargs='+',
                        help='list of pages to insert (start with 0), if None given all '
                             'pages of source will be inserted')
    # index
    parser.add_argument('-i',
                        '--index',
                        type=int,
                        default=None,
                        help='page index of destination file where the pages '
                             'will be inserted, if None they will be added at '
                             'the end of the file')

    return parser.parse_args(args)


if __name__ == "__main__":
    args = process_arguments(sys.argv[1:])
    print(args)
    pdf_insert(args.dest, args.source, args.pages, args.index, args.output)
