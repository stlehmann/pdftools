#! python3

import os
import sys
import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_merge(input1, input2, output):
    inputfile1 = open(input1, "rb")
    inputfile2 = open(input2, "rb")
    output = output or input1

    writer = PdfFileWriter()
    reader1 = PdfFileReader(inputfile1)
    for page in reader1.pages:
        writer.addPage(page)

    reader2 = PdfFileReader(inputfile2)
    for page in reader2.pages:
        writer.addPage(page)

    outputfile = open(output, "wb")
    writer.write(outputfile)
    inputfile1.close()
    inputfile2.close()
    outputfile.close()


def process_arguments(args):
    parser = argparse.ArgumentParser(description="Merge the pages of two PDF files.")
    #input
    parser.add_argument('input1',
                        type=str,
                        default=None,
                        help='input file 1')
    #output
    parser.add_argument('input2',
                        type=str,
                        default=None,
                        help='input file 2')
    #output
    parser.add_argument('-o',
                        '--output',
                        type=str,
                        default=None,
                        help='filename of the output file')

    return parser.parse_args(args)


if __name__ == "__main__":
    args = process_arguments(sys.argv[1:])
    pdf_merge(args.input1, args.input2, args.output)