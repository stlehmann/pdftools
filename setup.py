#!/usr/bin/env python
from setuptools import setup
import versioneer

setup(
    name='pdftools',
    version=versioneer.get_version(),
    packages=['pdftools'],
    scripts=['pdfsplit.py', 'pdfmerge.py', 'pdfrotate.py', 'pdfzip.py',
             'pdfinsert.py', 'pdfremove.py', 'pdfadd.py'],
    url='https://github.com/MrLeeh/pdftools',
    license='MIT',
    author='Stefan Lehmann',
    author_email='Stefan.St.Lehmann@gmail.com',
    description='A collection of convenience scripts for pdf manipulation, '
                'based on the PyPdf2 package.',
    install_requires=['PyPdf2'],
    maintainer='Stefan Lehmann',
    cmdclass=versioneer.get_cmdclass()
)
