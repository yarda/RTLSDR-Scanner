import os
from setuptools import setup

def local_file(fname):
    return os.path.relpath(os.path.join(os.path.dirname(__file__), fname))

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(local_file(fname)).read()

with open(local_file("src/version.py")) as o:
        exec(o.read())

setup(
    name = "rtlsdr_scanner",
    version = __version__,
    author = "Al Brown",
    author_email = "al@eartoearoak.com",
    description = ("A cross platform Python frequency scanning GUI for the "
                   "OsmoSDR library."),
    license = "GPLv3",
    url = "http://eartoearoak.com/software/rtlsdr-scanner",
    packages=["rtlsdr_scanner"],
    package_dir={"rtlsdr_scanner": "src"},
    scripts=["src/rtlsdr_scan.py"],
    install_requires=["wxPython",
                      "matplotlib",
                      "numpy",
                      "Pillow",
                      "pyserial",
                      "pyrtlsdr"
    ],
    long_description=read("readme.md"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
