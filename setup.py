#!/usr/bin/env python
"""
Setupfile for pdftools.

:author: Stefan Lehmann <stlm@posteo.de>
:license: MIT, see license file or https://opensource.org/licenses/MIT

:created on 2018-04-14 20:40:27
:last modified by:   Stefan Lehmann
:last modified time: 2018-04-14 21:03:58

"""
import ast
import re
from setuptools import setup, find_packages


def extract_version():
    """Extract the version from the package."""
    # Regular expression for the version
    _version_re = re.compile(r"__version__\s+=\s+(.*)")
    with open("pdftools/__init__.py", "r") as f:
        content = f.read()

    version_match = _version_re.search(content)
    version = str(ast.literal_eval(version_match.group(1)))
    return version


setup(
    name="pdftools",
    version=extract_version(),
    packages=find_packages(),
    entry_points={"console_scripts": ["pdftools=pdftools._cli:main"]},
    url="https://github.com/stlehmann/pdftools",
    license="MIT",
    author="Stefan Lehmann",
    author_email="stlm@posteo.de",
    description="A collection of convenience scripts for PDF manipulation, based on the PyPdf2 package",
    install_requires=["PyPdf2"],
    maintainer="Stefan Lehmann",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Office/Business",
    ],
    zip_safe=True,
)
