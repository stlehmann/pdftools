pdftools
========

small collection of python scripts for pdf manipulation

## Features

* split PDF files in multiple documents
* merge PDF files into one document
* rotate PDF files

## Usage

### pdfsplit
With *pdfsplit* one PDF file can be split in multiple documents. The new documents are named according to the *-o* argument. The page number and the file ending *pdf* are added to the name automatically.

```bash
usage: pdfsplit.py [-h] [-o OUTPUT] [-s STEPSIZE] input

Split a PDF file in multiple documents.


positional arguments:
  input                 input file that shall be splitted

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        filename of the output files
  -s STEPSIZE, --stepsize STEPSIZE
                        defines how many pages are packed in one file
```

### pdfmerge
This tool merges multiple input files to one output file. The page order is according to the order of the input files.

```bash
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

### pdfrotate
Rotate the pages of one or multiple input files clockwise or counterclockwise. The source file will be overwritten.
```bash
usage: pdfrotate.py [-h] [-c] inputs [inputs ...]

Rotate the pages of multiple input files by 90 degrees. Wildcards can be used.

positional arguments:
  inputs      list of input files

optional arguments:
  -h, --help  show this help message and exit
  -c          rotate pages counterclockwise
```
