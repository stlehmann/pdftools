import os
import argparse
from glob import glob
from tempfile import NamedTemporaryFile
from shutil import move
from PyPDF2 import PdfFileReader, PdfFileWriter
from pdftools import __version__


parentparser = argparse.ArgumentParser(add_help=False)
parentparser.add_argument(
    '--version',
    action='version',
    version='%(prog)s (pdftools) ' + __version__
)


def pdf_merge(inputs: [str], output: str, delete: bool=False):
    """
    Merge multiple Pdf input files in one output file.
    :param inputs: input files
    :param output: output file
    :param delete: delete input files after completion if true

    """
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


def pdf_rotate(inputs: [str], counter_clockwise: bool=False):
    """
    Rotate the given Pdf files clockwise or counter clockwise.
    :param inputs: pdf files
    :param counter_clockwise: rotate counter clockwise if true else clockwise

    """
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


def pdf_split(input: str, output: str, stepsize: int=1, sequence: [int]=None):
    """
    Split the input file in multiple output files
    :param input: name of the input file
    :param output: name of the output files
    :param stepsize: how many pages per file, only if sequence is None
    :param sequence: list with number of pages per file

    """
    output = output or os.path.splitext(input)[0]
    if not os.path.isfile(input):
        print("Error. The file '%s' does not exist." % input)
        return
    with open(input, "rb") as inputfile:
        reader = PdfFileReader(inputfile)
        pagenr = 0
        outputfile = None
        if sequence is None:
            for i, page in enumerate(reader.pages):
                if not i % stepsize:
                    pagenr += 1
                    outputfile = open(output + "_%i.pdf" % pagenr, "wb")
                    writer = PdfFileWriter()
                writer.addPage(page)
                if not (i + 1) % stepsize:
                    writer.write(outputfile)
                    outputfile.close()
        else:
            sequence = map(int, sequence)
            iter_pages = iter(reader.pages)
            for filenr, pagecount in enumerate(sequence):
                with open(output + "_%i.pdf" % (filenr + 1), "wb") as outputfile:
                    writer = PdfFileWriter()
                    for i in range(pagecount):
                        try:
                            page = next(iter_pages)
                            writer.addPage(page)
                        except StopIteration:
                            writer.write(outputfile)
                            return
                    writer.write(outputfile)

        if not outputfile.closed:
            writer.write(outputfile)
            outputfile.close()


def pdf_zip(input1: str, input2: str, output: str, delete: bool=False):
    """
    Zip pages of input1 and input2 in one output file. Useful for putting
    even and odd pages together in one document.
    :param input1: first input file
    :param input2: second input file
    :param output: output file
    :param delete: if true the input files will be deleted after zipping

    """
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
        os.remove(input1)
        os.remove(input2)


def pdf_insert(input1: str, input2: str, output: str=None):
    pass
