#!/usr/bin/env python
import os
import sys
from setuptools import setup
import versioneer


# use pandoc to convert README.md to README.rst
if any(s in sys.argv for s in ("upload", "register")):
    os.system("pandoc {0} -o {1}".format("README.md", "README.rst"))


if os.path.exists("README.rst"):
    long_description = open("README.rst").read()
    os.remove("README.rst")
else:
    long_description = ""


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
    long_description=long_description,
    install_requires=['PyPdf2'],
    maintainer='Stefan Lehmann',
    cmdclass=versioneer.get_cmdclass()
)
