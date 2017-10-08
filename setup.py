# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import hashron
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=hashron.__title__,
    version='0.0.1a1',
    description=long_description,
    url=hashron.__homepage__,
    author=hashron.__author__,
    author_email=hashron.__email__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers, Security',
        'Topic :: Hash Testing :: Hash Bruteforce ',
        'License :: OSI Approved :: GNU GPLv2',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='hashlib hashron hashcrack',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=["setuptools >= 0.7.0"],
)
