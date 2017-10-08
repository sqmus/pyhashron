#!/usr/bin/python3
("""hashron module - Hash testing and fetching using hashlib module


basicly hashron goals if guess infromation from hash, what the
information before hash using generated and fetch all posibility
from input keyword and predicted length

How i use this ?
----------------

is tool for testing and fetching hash
with generated char inputed in keyword.
the goal is guess information from hash.


	from hashron import *

Import hashron to you script


	# hashron.begin(<str>,<int>,<str>)
	hashron.begin('<Keyword String>',<Long key predict>,'<Target Hash>')

these function will try all posibility as 
long <Long key predict> char from <Keyword String>
and hashed to fetching with <Target Hash> hash.


	#hashron.benchmark(<str>)
	hashron.benchmark(<keyword>)


these function for test average hash processing 
time on your machine.

Installation
------------

    $ git clone http://github.com/sqmus/pyhashron
    $ cd pyhashron-master
    $ sudo python setup.py install

Resources
---------

GitHub repository <https://github.com/sqmus/pyhashron>
""")

import hashron
__title__ = ("hashron")
__summary__ = ("Hash testing and fetching using hashlib library")
__version__ =("0.1-alpha")
__description__ = __summary__
__author__ = ("sqmus")
__email__ = ("m3k4n5@protonmail.com")
__homepage__ = ("https://github.com/sqmus/pyhashron")

__license__ = ("GNU GPL License, Version 2")
__copyright__ = ("Copyright 2017 sqmus")

# this alpha
