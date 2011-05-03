``{{ module }}`` - quick description
====================================

Introduction
------------

``{{ module }}`` is a `GPL v3`_ licensed module for...

Requirements
------------

``{{ module }}`` does not depend on any modules that aren't included in
Python_'s standard library, and as such should run with Python 2.5 or newer
[#]_.  If ``{{ module }}`` doesn't work with the version of Python you have
installed, file an issue_ and I'll endeavour to fix it.

If you would like coloured terminal output, then you will need termcolor_.

The module has been tested on many UNIX-like systems, including Linux and OS X,
but it should work fine on other systems too.

.. [#] If you still use Python v2.4 only small changes are required, for
       example to the base class definitions and the unrolling of
       conditional expressions.

Example
-------

The simplest way to show how ``{{ module }}`` works is by example, and here
goes:

.. code-block:: pycon

    >>> True
    True

All the class definitions, methods and independent functions contain hopefully
useful usage examples in the docstrings.

Roadmap
-------

Current
'''''''

Future
''''''

Blue sky
''''''''

Technical debt
--------------

Contributing
------------

If you'd like to hack on ``{{ module }}``, start by forking `the repo`_
on GitHub.

The best way to have your changes merged is as follows:

* Create your own fork
* Use topic branches for your changes
* Add tests for your changes
* Push the branches to your fork
* Open a pull request for each logical set of changes

API Stability
-------------

API stability isn't guaranteed across versions, although frivolous changes won't
be made.

When ``{{ module }}`` 1.0 is released the API will be frozen, and any changes
which aren't backwards compatible will force a major version bump.

Limitations
-----------

Bugs
----

If you find any problems, bugs or just have a question about this package either
file an issue_ or drop me a mail_.

If you've found a bug please attempt to include a minimal testcase so that I can
reproduce the problem, or even better a patch!

.. _GPL v3: http://www.gnu.org/licenses/
.. _Python: http://www.python.org/
.. _termcolor: http://pypi.python.org/pypi/termcolor/
.. _mail: jnrowe@gmail.com
.. _issue: https://github.com/JNRowe/{{ module }}/issues
.. _the repo: https://github.com/JNRowe/{{ module }}
