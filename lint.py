#!/usr/bin/env python
"""
Lint the pdftools.

:author: Stefan Lehmann <stlm@posteo.de>
:license: MIT, see license file or https://opensource.org/licenses/MIT

:created on 2018-04-14 20:27:44
:last modified by:   Stefan Lehmann
:last modified time: 2018-04-14 21:07:37

"""
from subprocess import call


print("--- Running Flake8 ---")
res = call(["flake8", "."])
if res == 0:
    print("OK")
else:
    print("Errors")
