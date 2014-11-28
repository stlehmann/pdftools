#! python3
from setuptools import setup

setup(
    name='pdftools',
    version='1.0.0',
    packages=[''],
    scripts=['pdfsplit.py', 'pdfmerge.py', 'pdfrotate.py'],
    url='',
    license='GPL',
    author='Stefan Lehmann',
    author_email='Stefan.St.Lehmann@gmail.com',
    description='small collection of pdf tools',
    install_requires=['PyPdf2']
)
