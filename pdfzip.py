#! python3

import os
import sys
import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_zip(input1, input2, output, delete=False):
    writer = PdfFileWriter()
    if os.path.isfile(output):
        ans = input("The file '%s' already exists. "
                    "Overwrite? Yes/Abort [Y/a]: " % output).lower()
        if ans == "a":
            return

    outputfile = open(output, "wb")

    try:
        f1, f2 = open(input1, 'rb'), open(input2, 'rb')
        r1, r2 = PdfFileReader(f1), PdfFileReader(f2)
        writer = PdfFileWriter()
        pages1 = [page for page in r1.pages]
        pages2 = [page for page in r2.pages]
        for p1, p2 in zip(pages1, pages2):
            writer.addPage(p1)
            writer.addPage(p2)
        writer.write(outputfile)
        f1.close()
        f2.close()
    except FileNotFoundError as e:
        print(e.strerror + ": " + e.filename)
    finally:
        outputfile.close()

    if delete:
        for filename in inputs:
            os.remove(filename)


def process_arguments(args):
    parser = argparse.ArgumentParser(
        description="Zip the pages of two documents in one output file.")

    #input1
    parser.add_argument('input1',
                        type=str,
                        help='first inputfile')
    #input2
    parser.add_argument('input2',
                    type=str,
                    help='second inputfile')
    #output
    parser.add_argument('-o',
                        '--output',
                        type=str,
                        default=None,
                        help='filename of the output file',
                        required=True)
    #delete
    parser.add_argument('-d',
                        '--delete',
                        action='store_true',
                        help='delete input files after merge')
    return parser.parse_args(args)


if __name__ == "__main__":
    args = process_arguments(sys.argv[1:])
    pdf_zip(args.input1, args.input2, args.output, args.delete)
