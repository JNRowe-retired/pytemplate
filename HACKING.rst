Hacking
=======

Patches are most welcome, but I'd appreciate it if you could follow the
guidelines below to make it easier to integrate your changes.  These are
guidelines however, and as such can be broken if the need arises or you
just want to convince me that your style is better.

    * `PEP 8`_, the style guide, should be followed where possible.
    * While support for Python versions prior to v2.5 may be added in
      the future if such a need were to arise, you are encouraged to use
      v2.5 features now.
    * All new classes and methods should be accompanied by new ``doctest``
      examples, and Sphinx_'s ``autodoc`` formatted descriptions if at all
      possible.
    * Tests *must not* span network boundaries, see ``test.mock`` for
      workarounds.
    * ``doctest`` tests in modules are only for unit testing in general,
      and should not rely on any modules that aren't in Python's
      standard library.
    * Functional tests should be in the ``doc`` directory in
      reStructuredText_ formatted files, with actual tests in
      ``doctest`` blocks.  Functional tests can depend on external
      modules, but they must be Open Source.

New examples for the ``doc`` directory are as appreciated as code
changes.
