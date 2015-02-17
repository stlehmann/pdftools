#! python3
from setuptools import setup

setup(
    name='pdftools',
    version='1.0.1',
    packages=[],
    scripts=['pdfsplit.py', 'pdfmerge.py', 'pdfrotate.py', 'pdfzip.py'],
    url='https://github.com/MrLeeh/pdftools',
    license='GPL',
    author='Stefan Lehmann',
    author_email='Stefan.St.Lehmann@gmail.com',
    description='small collection of pdf tools',
    install_requires=['PyPdf2']
)
