Hacking
=======

Patches are most welcome, but I'd appreciate it if you could follow the
guidelines below to make it easier to integrate your changes.  These are only
guidelines however, and as such can be broken if the need arises or you just
want to convince me that your style is better.

* `PEP 8`_, the style guide, should be followed wherever possible.
* While support for Python versions prior to v2.5 may be added if such a need
  were to arise, you are encouraged to use v2.5 features now.
* All new classes and methods should be accompanied by new ``doctest`` examples,
  and Sphinx_'s ``autodoc`` formatted descriptions if at all possible.
* Tests *must not* span network boundaries, use a mocking framework for
  workarounds.
* ``doctest`` tests in modules are only for general unit testing, and should not
  rely on any modules that aren't in Python's standard library.
* Functional tests should be in the ``doc`` directory in reStructuredText_
  formatted files, with actual tests in ``doctest`` blocks.  Functional tests
  can depend on external modules, but they must be Open Source.

New examples for the ``doc`` directory are as appreciated as code changes.

Tips for contributors
---------------------

{{ module }}'s source code is managed using git_.  Below you'll find some of
examples of  common tasks you'll need to perform when working with ``git``.

Cloning the repository
''''''''''''''''''''''

If you're intending to have your work included in the main repository it is
probably simpler to create a GitHub_ account and click the "fork" button at this
point.  The instructions at Github for working with the fork you create are
quite comprehensive.

If you just wish to play around with the code then you can clone the repository
without a GitHub account with the following command::

    ▶ git clone git://github.com/JNRowe/{{ module }}.git

Making changes
''''''''''''''

If you haven't already told ``git`` your personal details now is the time to do
so::

    ▶ git config --global user.name "Joe Bloggs"
    ▶ git config --global user.email "joe@example.com"

Telling ``git`` your correct details here means you'll be correctly credited in
the project history when your work is merged in.

.. note::

   If you wish to set your personal details for this repository only then simply
   exclude the ``--global`` option.

Now, make the changes you wish to commit and run::

    ▶ git add <file> ...
    ▶ git commit -v

Your chosen editor will pop up, and you can enter a description.  The ``-v``
option tells ``git`` to include your changes in the commit message template, so
you can look at your changes while you write your message.

Publishing your changes
'''''''''''''''''''''''

If you opted to create a fork earlier then you can make your changes public with
ease.  Once you're happy with your changes simply call::

    ▶ git push

If you'd like your changes to be incorporated in to the main repository then you
can click the "pull request" button on your GitHub fork's page.  Doing so will
open a page for you to describe your changes, it will also serve as the review
mechanism should it be needed.

Fetching repository updates
'''''''''''''''''''''''''''

To pull in new upstream changes to the repository call::

    ▶ git pull

``git pull`` performs a merge between your changes and any new upstream changes,
so you may wish to use ``git fetch`` and ``git merge`` separately if you want to
maintain a easily readable history.  Another option is to use ``git pull``'s
``--rebase`` option, see the `git documentation`_ for extensive help on rebasing.

In the event of a merge conflict during the merge ``git`` will walk you through
the steps necessary to resolve the conflict.

Branches
''''''''

If you're comfortable with using ``git`` I'd appreciate changes in feature
branches, but if it isn't that important as I can emulate that when merging if
required.

If you're working in multiple feature branches don't be afraid to open multiple
pull requests at a time!

Release HOWTO
-------------

To make a release:

1. Run all tests

  * lettuce_
  * shelldoctest_

2. Update ``NEWS.rst`` and ``{{ module }}/_version.py``

3. Tag release in repository

4. Prepare release files with ``setup.py sdist``

5. Check release files

  * All files included
  * Successfully passes tests from step 1

6. Upload to PyPI_ with ``setup.py upload``

.. _PEP 8: http://www.python.org/dev/peps/pep-0008/
.. _Sphinx: http://sphinx.pocoo.org/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _git: http://www.git-scm.com/
.. _GitHub: https://github.com/
.. _git documentation: http://www.kernel.org/pub/software/scm/git/docs/
.. _lettuce: http://lettuce.it/
.. _shelldoctest: http://pypi.python.org/pypi/shelldoctest/
.. _PyPI: http://pypi.python.org/pypi
