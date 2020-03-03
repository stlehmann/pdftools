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
        "--version", action="store_true", help="Print version number and exit"
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
    parser_add.add_argument("source", type=str, default=None, help="PDF source file")
    parser_add.add_argument(
        "-p",
        "--pages",
        nARGS="+",
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

    parser_copy = SUBPARSERS.add_parser(
        "copy",
        help="Copy specific pages of a PDF file in a new file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser_insert = SUBPARSERS.add_parser(
        "insert",
        help="Insert pages of one file into another",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
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
    ARGS = PARSER.parse_ARGS()

    # validate command line arguments for the give sub-command
    # import packages after parsing to speed up command line responsiveness
    if ARGS.version:
        print("pdftools v{}".format(__version__))
        return

    if ARGS.command == "add":
        from pdftools import pdf_add

        pdf_add(ARGS.dest, ARGS.source, ARGS.pages, ARGS.output)
