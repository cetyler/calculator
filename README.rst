==========
calculator
==========

A simple calculator.

* Free software: MIT license

Install and Usage Instructions
------------------------------

To use, clone this repo.
Create a virtual environment and ``pip install -r requirements.txt``.
Run ``python -m calculator`` to bring up the CLI.
Type ``help`` to get a list of functions.

To use as an library, import ``calculation.py``.

Development Instructions
------------------------

After installing ``requirements.txt``, install ``requirements_dev.txt`` as well
to be able to run tests and build documentation.

Build Documentation
-------------------

Go to ``docs`` and run ``make html`` to build documentation.

Features
--------

* Able to do simple calculations such as addition, subtraction, division and
  multiplication.

* Use previous answer in the operation.

* Show history.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
