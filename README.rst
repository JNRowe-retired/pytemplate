``module``` - quick description
===============================

Introduction
------------

``module`` is a collection of `GPL v3`_ licensed modules for...

Requirements
------------

``module`` does not depend on any modules that aren't included
in Python_'s standard library, and as such should run with Python 2.5 or
newer [#]_.  If ``module`` doesn't work with the version of
Python you have installed, drop me a mail_ and I'll endeavour to fix it.

The modules have been tested on many UNIX-like systems, including Linux,
Solaris and OS X, but it should work fine on other systems too.  The
modules and scripts contain a large collection of ``doctest`` tests that
can be checked with ``./setup test_code``, and the code examples in the
documentation can be tested with ``./setup test_doc``.

.. [#] If you still use Python v2.4 only small changes are required, for
       example to the base class definitions and the unrolling of
       conditional expressions.

.. [#] Some tests may fail due to rounding errors depending on the
       system the tests are being run on, but such instances should be
       obvious even to the casual user and some effort has been put in
       to reduce the likelihood of such failures.

Example
-------

The simplest way to show how ``module`` works is by example, and
here goes:

.. code-block:: pycon

    >>> True
    True

All the class definitions, methods and independent functions contain
hopefully useful usage examples in the docstrings.

All the examples in the ``doc/`` directory can be executed using 
``./setup.py test_doc``.

Roadmap
-------

<Ideas for future versions>

Thanks
------

The following people have submitted patches, testing and feedback:

    * You? - Your name here

API Stability
-------------

API stability isn't guaranteed across versions, although frivolous
changes won't be made.

When ``module`` 1.0 is released the API will be frozen, and any
changes which aren't backwards compatible will force a major version
bump.

Limitations
-----------

Bugs
----

If you find any problems, bugs or just have a question about this
package either drop me an mail_ or file an issue_.

If you've found please attempt to include a minimal testcase so I can
reproduce the problem, or even better a patch!

.. _GPL v3: http://www.gnu.org/licenses/
.. _Python: http://www.python.org/
.. _PEP 8: http://www.python.org/dev/peps/pep-0008/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _mail: jnrowe@gmail.com
.. _issue: http://github.com/JNRowe/``module``/issues
.. _Sphinx: http://sphinx.pocoo.org/
