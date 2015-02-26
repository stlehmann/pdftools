pdftools
========
* **Version** 1.0.3
* **Copyright (c)** 2015 Stefan Lehmann
* **License:** MIT
* **Description:** This is a small collection of convenience python scripts for fast pdf manipulation via commandline.

## Features

* insert pages
* split PDF files in multiple documents
* merge PDF files into one document
* rotate PDF files
* zip PDF files in one document

## Usage

*pdftools* adds some scripts to your existing Python installation that
can be called via the commandline. The description for each script is
listed below.

### pdfsplit.py
With *pdfsplit* one PDF file can be split in multiple documents. The new documents are named according to the *-o* argument. The page number and the file ending *pdf* are added to the name automatically.

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
This tool merges multiple input files to one output file. The page order is according to the order of the input files.

```
usage: pdfmerge.py [-h] -o OUTPUT [-d] inputs [inputs ...]

Merge the pages of multiple input files in one output file.

positional arguments:
  inputs                list of input files

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        filename of the output file
  -d, --delete          delete input files after merge
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

### pdfzip.py
Zip the pages of two input files in one output file. This is useful when
dealing with scanned documents where even pages are in one docuemnt and
odd pages in the other.

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