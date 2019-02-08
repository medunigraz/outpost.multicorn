========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|

.. |requires| image:: https://requires.io/github/medunigraz/outpost.multicorn/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/medunigraz/outpost.multicorn/requirements/?branch=master

.. end-badges

Extensions to Multicorn_ and pyODBC_ used with outpost_.

* Free software: BSD license

To create foreign servers:

    CREATE SERVER sqlalchemy
    FOREIGN DATA WRAPPER multicorn
    OPTIONS (
        wrapper 'outpost.multicorn.fdw.OutpostFdw'
    );

Currently it does two things:

* Register a custom Dialect ``oracle.pyodbc``.
* Monkey-patch ``create_engine()`` to enable ``pool_pre_ping``.

.. _Multicorn: https://multicorn.org/
.. _pyODBC: https://pypi.org/project/pyodbc/
.. _outpost: https://github.com/medunigraz/outpost/
