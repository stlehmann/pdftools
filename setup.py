#! python3
from setuptools import setup
from pdftools import __version__

setup(
    name='pdftools',
    version=__version__,
    packages=['pdftools'],
    scripts=['pdfsplit.py', 'pdfmerge.py', 'pdfrotate.py', 'pdfzip.py',
             'pdfinsert.py'],
    url='https://github.com/MrLeeh/pdftools',
    license='MIT',
    author='Stefan Lehmann',
    author_email='Stefan.St.Lehmann@gmail.com',
    description='A collection of convenience scripts for pdf manipulation',
    install_requires=['PyPdf2'],
    maintainer='Stefan Lehmann'
)
