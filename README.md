pdftools
========
* **Copyright (c)** 2015 Stefan Lehmann
* **License:** MIT
* **Description:** This is a collection of convenience python scripts
for fast and painless pdf manipulation via commandline. It is based on the
PyPdf2 package.

[![Build Status](https://travis-ci.org/stlehmann/pdftools.svg?branch=master)](https://travis-ci.org/stlehmann/pdftools)

## Features

* add, insert, remove and rotate pages
* split PDF files in multiple documents
* copy specific pages in a new document
* merge or zip PDF files into one document

## Usage

*pdftools* adds some scripts to your existing Python installation that
can be called via the commandline. The description for each script is
listed below.

### pdfadd.py

Add pages from a source pdf file to a destination file. The output is either
written in a new file or to the destination file.

```
usage: pdfadd.py [-h] [--version] [-p PAGES [PAGES ...]] [-o OUTPUT]
                 dest source

Add pages from a source file to an output PDF file. If the output file does
not exist a new file will be created.

positional arguments:
  dest                  destination pdf file
  source                pdf source file

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -p PAGES [PAGES ...], --pages PAGES [PAGES ...]
                        list of pages to add to the output. Examples: 5 1-9 1-
                        -9
  -o OUTPUT, --output OUTPUT
                        name of the output file, if None the destinationfile
                        will be overwritten
```

### pdfcopy.py

Copy specific pages of a PDF file in a new file.

```
usage: pdfcopy.py [-h] [--version] [-o OUTPUT] [-p PAGES [PAGES ...]] [-y]
                  input

Copy specific pages of a PDF file in a new file.

positional arguments:
  input                 input file containing the source pages

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -o OUTPUT, --output OUTPUT
                        filename of the output file
  -p PAGES [PAGES ...], --pages PAGES [PAGES ...]
                        list of pages to copy in the new file. Examples: "5 8
                        10": Pages 5, 8, 10; "1-9": Pages 1 to 9; "5-": Pages
                        from 5 to last page; "-9": Pages from beginning to 9
  -y                    yes to all

```

### pdfinsert.py

Insert pages from one source file into a destination file.

```
usage: pdfinsert.py [-h] [--version] [-o OUTPUT] [-p PAGES [PAGES ...]]
                    [-i INDEX]
                    dest source

Insert pages of one file in another.

positional arguments:
  dest                  destination pdf file
  source                source pdf file

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -o OUTPUT, --output OUTPUT
                        filename of the output files, if None given dest will
                        be used as output
  -p PAGES [PAGES ...], --pages PAGES [PAGES ...]
                        list of page numbers (start with 1) which will be
                        inserted, if None all pages will be rotated (default),
                        Examples: 5 1-9 1- -9
  -i INDEX, --index INDEX
                        page number (start with 1) of destination file where
                        the pages will be inserted, if None they will be added
                        at the end of the file
```

### pdfremove.py

Remove pages from a source pdf file.

```
usage: pdfremove.py [-h] [--version] -p PAGES [PAGES ...] [-o OUTPUT] source

Remove pages from a PDF file.

positional arguments:
  source                pdf source file

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -p PAGES [PAGES ...], --pages PAGES [PAGES ...]
                        list of pages to remove from file. Examples: 5 1-9 1-
                        -9
  -o OUTPUT, --output OUTPUT
                        name of the output file, if None the source file will
                        be overwritten

```

### pdfrotate.py

Rotate pages of one input file clockwise or counterclockwise.

```
usage: pdfrotate.py [-h] [--version] [-c] [-p PAGES [PAGES ...]] [-o OUTPUT]
                    input

Rotate the pages of a PDF files by 90 degrees.

positional arguments:
  input                 input file

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -c                    rotate pages counterclockwise
  -p PAGES [PAGES ...], --pages PAGES [PAGES ...]
                        list of page numbers which will be rotated, if None
                        all pages will be rotated (default). Examples: 5 1-9
                        1- -9
  -o OUTPUT, --output OUTPUT
                        name of the output file, if None the source filewill
                        be overwritten
```

### pdfsplit.py

With *pdfsplit* one PDF file can be split in multiple documents.
The new documents are named according to the *-o* argument. The page number
and the file ending *pdf* are added to the name automatically.

```
usage: pdfsplit.py [-h] [--version] [-o OUTPUT] [-s STEPSIZE]
                   [-q SEQUENCE [SEQUENCE ...]]
                   input

Split a PDF file in multiple documents.

positional arguments:
  input                 input file that shall be splitted

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -o OUTPUT, --output OUTPUT
                        filename of the output files
  -s STEPSIZE, --stepsize STEPSIZE
                        defines how many pages are packed in each output file
  -q SEQUENCE [SEQUENCE ...], --sequence SEQUENCE [SEQUENCE ...]
                        sequence of numbers describing how many pages to put
                        in each outputfile
```

### pdfmerge.py

This tool merges multiple input files to one output file.
The page order is according to the order of the input files.

```
usage: pdfmerge.py [-h] -o OUTPUT [-d] inputs [inputs ...]

Merge the pages of multiple input files in one output file.

positional arguments:n
  inputs                list of input files

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        filename of the output file
  -d, --delete          delete input files after merge
```

### pdfzip.py

Zip the pages of two input files in one output file. This is useful when
dealing with scanned documents where even pages are in one docuemnt and
odd pages in the other.

To merge a multiple page document which was scanned with a non-duplex-scanner
one can use the *--revert* option. In this case one gets e.g. one pdf with pages
1,3 and 5 and another pdf with the pages 6,4 and 2. In order to merge/zip them
correctly the second pdf needs to be reversed.

```
usage: pdfzip.py [-h] -o OUTPUT [-d] input1 input2

Zip the pages of two documents in one output file.

positional arguments:
input1                first inputfile
input2                second inputfile

optional arguments:
-h, --help            show this help message and exit
-o OUTPUT, --output OUTPUT
filename of the output file
-d, --delete          delete input files after merge
-r, --revert          revert the pages of second input file
```
