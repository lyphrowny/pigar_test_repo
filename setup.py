from setuptools import setup
from Cython.Build import cythonize

setup(
    name='kalah',
    version="0.1.0"
    ext_modules=cythonize("kalah.pyx"),
    zip_safe=False,
)
