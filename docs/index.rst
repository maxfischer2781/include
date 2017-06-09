.. include documentation master file, created by
   sphinx-quickstart on Wed Feb 22 14:45:32 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

#################################
include - Dynamic Module Importer
#################################

.. image:: https://travis-ci.org/maxfischer2781/include.svg?branch=master
   :target: https://travis-ci.org/maxfischer2781/include
   :alt: Build Status
.. image:: https://landscape.io/github/maxfischer2781/include/master/landscape.svg?style=flat
   :target: https://landscape.io/github/maxfischer2781/include/master
   :alt: Code Health
.. image:: https://codecov.io/gh/maxfischer2781/include/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/maxfischer2781/include
   :alt: Test Coverage
.. image:: https://readthedocs.org/projects/include/badge/?version=latest
   :target: http://include.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. toctree::
    :maxdepth: 1
    :caption: Documentation Topics Overview:

    Public Interface <source/api/include>
    source/bootstrap
    Module Index <source/api/modules>

The :py:mod:`include` library is built to use code from arbitrary sources in your application.
In contrast to ``eval``, ``exec`` and other code execution, :py:mod:`include` creates fully featured modules.
This makes code viable for pickling, multiprocessing, IPC and more.

Using :py:mod:`include` is straight forward - you only need the top level functions of the module:

.. code:: python

   import include
   my_config = include.path('/etc/sysconfig/app_conf.py')

All ugly bits are handled by :py:mod:`include` - once a module is imported, it works as normal.
Even in other processes, the import machinery is bootstrapped without manual intervention.

For all supported import methods, check out the public inteface of the :py:mod:`include` module.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

----------

Documentation built from include |version| at |today|.
