#! python3

import os
import sys
import argparse
from tempfile import NamedTemporaryFile
from shutil import move
from glob import glob
from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_rotate(inputs, counter_clockwise=False):
    for input_name in inputs:
        filenames = glob(input_name)
        for filename in filenames:
            with open(filename, 'rb') as f:
                writer = PdfFileWriter()
                tempfile = NamedTemporaryFile(delete=False)
                reader = PdfFileReader(f)
                for page in reader.pages:
                    if counter_clockwise:
                        writer.addPage(page.rotateCounterClockwise(90))
                    else:
                        writer.addPage(page.rotateClockwise(90))
                writer.write(tempfile)
            f.close()
            tempfile.close()
            os.remove(filename)
            move(tempfile.name, filename)


def process_arguments(args):
    parser = argparse.ArgumentParser(
        description="Rotate the pages of multiple input files by 90 degrees. "
                    "Wildcards can be used.")
    #input
    parser.add_argument('inputs',
                        type=str,
                        default=None,
                        nargs='+',
                        help='list of input files')
    #counterClockwise
    parser.add_argument('-c',
                        action='store_true',
                        dest='counter_clockwise',
                        help='rotate pages counterclockwise')

    return parser.parse_args(args)


if __name__ == "__main__":
    args = process_arguments(sys.argv[1:])
    pdf_rotate(args.inputs, args.counter_clockwise)