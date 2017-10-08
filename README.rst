Hashron (pyHashron)
===================

Hash Testing and Fetching using hashlib

How i use this ?
----------------

is tool for testing and fetching hash
with generated char inputed in keyword.
the goal is guess information from hash.

   .. code-block:: bash

	from hashron import *

Import hashron to you script

   .. code-block:: bash

	# hashron.begin(<str>,<int>,<str>)
	hashron.begin('<Keyword String>',<Long key predict>,'<Target Hash>')

these function will try all posibility as 
long <Long key predict> char from <Keyword String>
and hashed to fetching with <Target Hash> hash.


   .. code-block:: bash

	#hashron.benchmark(<str>)
	hashron.benchmark(<keyword>)


these function for test average hash processing 
time on your machine.

Installation
------------

.. code-block:: bash

    $ pip install hashron


Resources
---------

* `GitHub repository <https://github.com/sqmus/pyhashron>`_
