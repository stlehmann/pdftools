import os
from glob import glob
from tempfile import NamedTemporaryFile
from shutil import move
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


def pdf_split(input, output, stepsize=1):
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
        os.remove(input1)
        os.remove(input2)
