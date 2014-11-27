#! python3

import os
import sys
import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter


def split_pdf(input, output, stepsize=1):
    output = output or os.path.splitext(input)[0]
    if not os.path.isfile(input):
        print("Error. The file '%s' does not exist." % input)
        return
    with open(input, "rb") as inputfile:
        reader = PdfFileReader(inputfile)
        pagenr = 0
        outputfile = None
        for i, page in enumerate(reader.pages):
            if not i % stepsize:
                pagenr += 1
                outputfile = open(output + "_%i.pdf" % pagenr, "wb")
                writer = PdfFileWriter()
            writer.addPage(page)
            if not (i + 1) % stepsize:
                writer.write(outputfile)
                outputfile.close()
        if not outputfile.closed:
            writer.write(outputfile)
            outputfile.close()

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
    split_pdf(args.input, args.output, args.stepsize)