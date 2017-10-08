Hashron (pyHashron)
===================

Hash Testing and Fetching using hashlib

How i use this ?
----------------

is tool for testing and fetching hash
with generated char inputed in keyword.
the goal is guess information from hash.

   .. code-block:: python

	from hashron import *

Import hashron to you script

   .. code-block:: python

	# hashron.begin(<str>,<int>,<str>)
	hashron.begin('<Keyword String>',<Long key predict>,'<Target Hash>')

these function will try all posibility as 
long <Long key predict> char from <Keyword String>
and hashed to fetching with <Target Hash> hash.


   .. code-block:: python

	#hashron.benchmark(<str>)
	hashron.benchmark(<keyword>)


these function for test average hash processing 
time on your machine.

Installation
------------

you can download this packages from
* `master zip<https://github.com/sqmus/pyhashron/archive/master.zip>`_

extract it to a directory
open terminal on the directory
Linux 
.. code-block:: bash

    $ sudo python setup.py install
    
Windows
.. code-block:: batch

    setup.py install
    
Mac same like Linux command

Or if you familiar with git

.. code-block:: bash

    $ git clone http://github.com/sqmus/pyhashron
    $ cd pyhashron-master
    $ sudo python setup.py install


Resources
---------

* `GitHub repository <https://github.com/sqmus/pyhashron>`_
