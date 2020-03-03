import os.path as path
import argparse
import re
from . import __version__


def main():
    PARSER = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    # global options
    PARSER.add_argument(
        "-V", "--version", action="store_true", help="Print version number and exit"
    )

    SUBPARSERS = PARSER.add_subparsers(
        title="Sub-commands", dest="command", metavar="<command>"
    )

    # Add
    # --------------------------------------------
    parser_add = SUBPARSERS.add_parser(
        "add",
        help="Add pages from a source file to an output PDF file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser_add.add_argument("dest", type=str, help="Destination PDF file")
    parser_add.add_argument("src", type=str, default=None, help="PDF source file")
    parser_add.add_argument(
        "-p",
        "--pages",
        nargs="+",
        help="list of pages to add to the output. Examples: 5; 1-9; 1-; -9",
    )
    # output
    parser_add.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,
        help="name of the output file, if None the destination file will be overwritten",
    )

    # Copy
    # --------------------------------------------
    parser_copy = SUBPARSERS.add_parser(
        "copy",
        help="Copy specific pages of a PDF file in a new file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser_copy.add_argument(
        "src", type=str, default=None, help="Source PDF containing pages to copy"
    )
    parser_copy.add_argument(
        "-o", "--output", type=str, default=None, help="filename of the output file"
    )
    parser_copy.add_argument(
        "-p",
        "--pages",
        dest="pages",
        type=str,
        nargs="+",
        default=1,
        help="list of pages to copy in the new file. "
        "Examples: \n"
        '"5 8 10": Pages 5, 8, 10; '
        '"1-9":    Pages 1 to 9; '
        '"5-":     Pages from 5 to last page; '
        '"-9":     Pages from beginning to 9',
    )
    parser_copy.add_argument("-y", action="store_true", help="yes to all")

    # Insert
    # --------------------------------------------
    parser_insert = SUBPARSERS.add_parser(
        "insert",
        help="Insert pages of one file into another",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser_insert.add_argument("dest", type=str, help="Destination PDF file")
    parser_insert.add_argument("src", type=str, help="Source PDF file")
    parser_insert.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,
        help="Output file name. If None given, `dest` will be used as output and overwritten",
    )
    parser_insert.add_argument(
        "-p",
        "--pages",
        nargs="+",
        help="List of page numbers (start with 1) which will be inserted. If None, all pages will be inserted (default). Examples: 5; 1-9; 1-; -9",
    )
    parser_insert.add_argument(
        "-i",
        "--index",
        type=int,
        default=None,
        help="Page number (1-indexed) of destination file where the pages will be inserted. If None they will be added at the end of the file",
    )

    parser_merge = SUBPARSERS.add_parser(
        "merge",
        help="Merge the pages of multiple input files into one output file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser_remove = SUBPARSERS.add_parser(
        "remove",
        help="Remove pages from a PDF file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser_rotate = SUBPARSERS.add_parser(
        "rotate",
        help="Rotate the pages of a PDF files by 90 degrees",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser_split = SUBPARSERS.add_parser(
        "split",
        help="Split a PDF file into multiple documents",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser_zip = SUBPARSERS.add_parser(
        "zip",
        help="Python-like zipping (interleaving) the pages of two documents in one output file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # parse arguments from command line
    ARGS = PARSER.parse_args()

    # validate command line arguments for the give sub-command
    # import packages after parsing to speed up command line responsiveness
    if ARGS.version:
        print("pdftools v{}".format(__version__))
        return

    if ARGS.command == "add":
        from pdftools.pdftools import pdf_add

        pdf_add(ARGS.dest, ARGS.src, ARGS.pages, ARGS.output)
    elif ARGS.command == "copy":
        from pdftools.pdftools import pdf_copy

        pdf_copy(ARGS.input, ARGS.output, ARGS.pages, ARGS.y)
    elif ARGS.command == "insert":
        from pdftools.pdftools import pdf_insert

        pdf_insert(ARGS.dest, ARGS.src, ARGS.pages, ARGS.index, ARGS.output)
    elif ARGS.command == "merge":
        from pdftools.pdftools import pdf_merge

        pdf_merge()
    elif ARGS.command == "remove":
        from pdftools.pdftools import pdf_remove

        pdf_remove()
    elif ARGS.command == "rotate":
        from pdftools.pdftools import pdf_rotate

        pdf_rotate()
    elif ARGS.command == "split":
        from pdftools.pdftools import pdf_split

        pdf_split()
    elif ARGS.command == "zip":
        from pdftools.pdftools import pdf_zip

        pdf_zip()
