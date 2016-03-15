import os
from tempfile import NamedTemporaryFile
from shutil import move
from PyPDF2 import PdfFileReader, PdfFileWriter
from pdftools.parseutil import parse_rangearg, limit


def overwrite_dlg(filename):
    ans = input("Overwrite file '%s'? Yes/No [Y/n]: " % filename).lower()
    if ans in ['y', '']:
        return True
    return False


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


def pdf_rotate(input: str, counter_clockwise: bool=False, pages: [str]=None,
               output: str=None):
    """
    Rotate the given Pdf files clockwise or counter clockwise.
    :param inputs: pdf files
    :param counter_clockwise: rotate counter clockwise if true else clockwise
    :param pages: list of page numbers to rotate, if None all pages will be
        rotated
    """
    infile = open(input, 'rb')
    reader = PdfFileReader(infile)
    writer = PdfFileWriter()

    # get pages from source depending on pages parameter
    if pages is None:
        source_pages = reader.pages
    else:
        pages = parse_rangearg(pages, len(reader.pages))
        source_pages = [reader.getPage(i) for i in pages]

    # rotate pages and add to writer
    for i, page in enumerate(source_pages):
        if pages is None or i in pages:
            if counter_clockwise:
                writer.addPage(page.rotateCounterClockwise(90))
            else:
                writer.addPage(page.rotateClockwise(90))
        else:
            writer.addPage(page)

    # Open output file or temporary file for writing
    if output is None:
        outfile = NamedTemporaryFile(delete=False)
    else:
        if not os.path.isfile(output) or overwrite_dlg(output):
            outfile = open(output, 'wb')
        else:
            return

    # Write to file
    writer.write(outfile)
    infile.close()
    outfile.close()

    # If no output defined move temporary file to input
    if output is None:
        if overwrite_dlg(input):
            os.remove(input)
            move(outfile.name, input)
        else:
            os.remove(outfile.name)


def pdf_copy(input: str, output: str, pages: [int], yes_to_all=False):
    """
    Copy pages from the input file in a new output file.
    :param input: name of the input pdf file
    :param output: name of the output pdf file
    :param pages: list containing the page numbers to copy in the new file

    """
    if not os.path.isfile(input):
        print("Error. The file '%s' does not exist." % input)
        return
    if (os.path.isfile(output)
            and not yes_to_all
            and not overwrite_dlg(output)):
        return

    with open(input, 'rb') as inputfile:
        reader = PdfFileReader(inputfile)
        outputfile = open(output, "wb")
        writer = PdfFileWriter()
        if pages is None:
            pages = range(len(reader.pages))
        else:
            pages = parse_rangearg(pages, len(reader.pages))
        for pagenr in sorted(pages):
            page = reader.getPage(pagenr)
            writer.addPage(page)
            writer.write(outputfile)
        outputfile.close()


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


def pdf_zip(input1: str, input2: str, output: str, delete: bool=False,
            revert: bool=False):
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
        if ans not in ['y', '']:
            return
    outputfile = open(output, "wb")
    try:
        f1, f2 = open(input1, 'rb'), open(input2, 'rb')
        r1, r2 = PdfFileReader(f1), PdfFileReader(f2)
        writer = PdfFileWriter()
        pages1 = [page for page in r1.pages]
        pages2 = [page for page in r2.pages]
        if not revert:
            for p1, p2 in zip(pages1, pages2):
                writer.addPage(p1)
                writer.addPage(p2)
        else:
            for p1, p2 in zip(pages1, reversed(pages2)):
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


def pdf_insert(dest: str, source: str,
               pages: [str]=None, index: int=None,
               output: str=None):
    """
    Insert pages from one file into another.
    :param dest: Destination file
    :param source: Source file
    :param pages: list of page numbers to insert
    :param index: index in destination file where to insert the pages
    :param output: output file

    """
    if output is not None and os.path.isfile(output):
        ans = input("The file '%s' already exists. "
                    "Overwrite? Yes/Abort [Y/a]: " % output).lower()
        if ans not in ['y', '']:
            return

    writer = PdfFileWriter()
    # read pages from file1
    destfile = open(dest, 'rb')
    destreader = PdfFileReader(destfile)
    for page in destreader.pages:
        writer.addPage(page)

    # read pages from file2
    srcfile = open(source, 'rb')
    srcreader = PdfFileReader(srcfile)

    # if no page numbers are given insert all pages
    index = limit(index - 1, 0, len(destreader.pages))
    if pages is None:
        for i, page in enumerate(srcreader.pages):
            if index is None:
                writer.addPage(page)
            else:
                writer.insertPage(page, index + i)
    else:
        pages = parse_rangearg(pages, len(srcreader.pages))
        for i, pagenr in enumerate(pages):
            page = srcreader.getPage(pagenr)
            if index is None:
                writer.addPage(page)
            else:
                writer.insertPage(page, index + i)

    if output is None:
        # Write into Temporary File first and then overwrite dest file
        ans = input("Overwrite the file '%s'? Yes/Abort [Y/a]: " %
                    dest).lower()
        if ans in ['y', '']:
            tempfile = NamedTemporaryFile(delete=False)
            writer.write(tempfile)
            tempfile.close()
            move(tempfile.name, dest)
    else:
        with open(output, "wb") as outfile:
            writer.write(outfile)
    destfile.close()
    srcfile.close()


def pdf_remove(source: str, pages: [str], output: str=None):
    """
    Remove pages from a PDF source file.
    :param source: pdf source file
    :param pages: list of page numbers or range expressions
    :param output: pdf output file

    """
    if output is not None and os.path.isfile(output):
        if overwrite_dlg(output) is False:
            return

    writer = PdfFileWriter()
    srcfile = open(source, 'rb')
    srcreader = PdfFileReader(srcfile)

    # Add pages, leave out removed pages
    pages = parse_rangearg(pages, len(srcreader.pages))
    for pagenr, page in enumerate(srcreader.pages):
        if pagenr not in pages:
            writer.addPage(page)

    # Open output file or temporary file for writing
    if output is None:
        outfile = NamedTemporaryFile(delete=False)
    else:
        outfile = open(output, 'wb')

    # Write file and close
    writer.write(outfile)
    srcfile.close()
    outfile.close()

    # Move temporary file to source
    if output is None:
        if overwrite_dlg(source):
            os.remove(source)
            move(outfile.name, source)
        else:
            os.remove(outfile)


def pdf_add(dest: str, source: str, pages: [str], output: str):
    """
    Add pages from a source pdf file to an output file. If the output
    file does not exist a new file will be created.
    :param source: source pdf file
    :param dest: destination pdf file
    :param pages: list of page numbers or range expressions
    :param output: output pdf file

    """
    if output is not None and os.path.isfile(output):
        if not overwrite_dlg(output):
            return

    writer = PdfFileWriter()

    # read pages from destination file
    destfile = open(dest, 'rb')
    destreader = PdfFileReader(destfile)
    for page in destreader.pages:
        writer.addPage(page)

    # read pages from source file
    srcfile = open(source, 'rb')
    srcreader = PdfFileReader(srcfile)

    # if no page numbers are given add all pages from source
    if pages is None:
        for i, page in enumerate(srcreader.pages):
            writer.addPage(page)
    else:
        pages = parse_rangearg(pages, len(srcreader.pages))
        for pagenr in pages:
            page = srcreader.getPage(pagenr)
            writer.addPage(page)

    if output is None:
        # Write into Temporary File first and then overwrite dest file
        if overwrite_dlg(dest):
            tempfile = NamedTemporaryFile(delete=False)
            writer.write(tempfile)
            tempfile.close()
            destfile.close()
            srcfile.close()
            os.remove(dest)
            move(tempfile.name, dest)
    else:
        with open(output, "wb") as outfile:
            writer.write(outfile)
            destfile.close()
            srcfile.close()

