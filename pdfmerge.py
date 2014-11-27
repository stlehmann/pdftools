#! python3

import os
import sys
import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_merge(inputs, output):
    writer = PdfFileWriter()
    if os.path.isfile(output):
        ans = input("The file '%s' already exists. "
                    "Overwrite? Yes/Abort [Y/a]: " % output).lower()
        if ans == "a":
            return

    outputfile = open(output, "wb")

    try:
        infiles = []
        for filename in inputs:
            f = open(filename, 'rb')
            reader = PdfFileReader(f)
            for page in reader.pages:
                writer.addPage(page)
            infiles.append(f)
        writer.write(outputfile)
    except FileNotFoundError as e:
        print(e.strerror + ": " + e.filename)
    finally:
        outputfile.close()
        for f in infiles:
            f.close()


def process_arguments(args):
    parser = argparse.ArgumentParser(
        description="Merge the pages of multiple input files in one output file.")
    #input
    parser.add_argument('inputs',
                        type=str,
                        default=None,
                        nargs='+',
                        help='list of input files')

    #output
    parser.add_argument('-o',
                        '--output',
                        type=str,
                        default=None,
                        help='filename of the output file',
                        required=True)

    return parser.parse_args(args)


if __name__ == "__main__":
    args = process_arguments(sys.argv[1:])
    pdf_merge(args.inputs, args.output)