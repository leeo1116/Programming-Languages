__author__ = 'Liang Li'
from distutils.core import setup
from glob import glob
import py2exe

data_files = [("Microsoft.VC90.CRT", glob(r"Microsoft.VC90.CRT\*.*"))]
setup(data_files = data_files, console=["email_generator_main.py"])


# run in terminal, http://www.py2exe.org/index.cgi/Tutorial
# ..\python setup.py py2exe