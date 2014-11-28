#! python3

import os
import sys
import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_merge(inputs, output, delete=False):
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

    if delete:
        for filename in inputs:
            os.remove(filename)


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

    #delete
    parser.add_argument('-d',
                        '--delete',
                        action='store_true',
                        help='delete input files after merge')

    return parser.parse_args(args)


if __name__ == "__main__":
    args = process_arguments(sys.argv[1:])
    print(args)
    #pdf_merge(args.inputs, args.output, args.delete)