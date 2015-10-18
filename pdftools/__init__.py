from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from pdftools.pdftools import pdf_merge, pdf_rotate, pdf_split, pdf_zip, \
    pdf_insert, pdf_remove, pdf_add
