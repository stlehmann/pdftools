#! python3
from setuptools import setup

setup(
    name='pdftools',
    version='1.0.2',
    packages=['pdftools'],
    scripts=['pdfsplit.py', 'pdfmerge.py', 'pdfrotate.py', 'pdfzip.py'],
    url='https://github.com/MrLeeh/pdftools',
    license='MIT',
    author='Stefan Lehmann',
    author_email='Stefan.St.Lehmann@gmail.com',
    description='small collection of convenience scripts for pdf manipulation',
    install_requires=['PyPdf2'],
    maintainer='Stefan Lehmann'
)
