******
Aaargh
******

*Aaargh*: an astonishingly awesome application argument helper.

*Aaargh* is a Python module that makes building friendly command line
applications really easy. Applications built with *Aaargh* provide a single
executable with a subcommand for each exposed Python function. Each subcommand
may have its own command line arguments. This is similar to the way version
control systems provide multiple commands using a single entry point. (Examples
include ``bzr commit`` and ``git checkout``).

*Aaargh* is named after one of the castles in the movie *Monty Python and the
Holy Grail*. The acronym *Aaargh* stands for *an astonishingly awesome
application argument helper*, but omits a few letters to make it triple A.

*Aaargh* is compatible with both Python 2.6+ and Python 3.


Rationale
=========

The Python standard library contains the *optparse*, *getopt*, and *argparse*
modules, and out in the wild you will find many alternative command line
interface libraries stacked on top of these, such as *cliff*, *cement*,
*opster*, *plac*, and many others. Some of these libraries separate the command
line interface setup of your application from the actual code, some force yet
another argument parsing API upon you, some force you to hide your code in
non-obvious framework constructs, and some even add dependencies on other
modules.

This makes you scream *aaargh*. And, lo and behold, here it is!


Usage
=====

*Aaargh* delegates almost all of its work to the `argparse` module, which does
a great job handling arguments and printing usage information. However,
`argparse` is a bit verbose and cumbersome for many simple applications, so
*Aaargh* lets application authors minimize boilerplate code by wrapping
commonly used `argparse` features in a few non-intrusive decorators. *Aaargh*
does not hide the `argparse` API, since the decorators have *exactly the same
API* as their `argparse` counterparts. This is a deliberate design decision,
and this is what makes *Aaargh* different from its many alternatives.

The docstrings in the `aaargh.py` file contain all information you need to use
*Aaargh*. Refer to the `argparse` documentation for information on specifying
arguments, providing defaults, adding help texts, and so on.


Example
=======

A simple command line application that exposes a few functions looks like
this::

   #!/usr/bin/env python

   import aaargh

   app = aaargh.App(description="A simple greeting application.")

   # Application level arguments:
   app.arg('--name', help="Name of the person to greet", default="stranger")

   # Application level defaults:
   app.defaults(name="visitor")  # overrides "stranger"


   @app.cmd
   def hello(name):  # application level "name" argument is always passed
       print("Hello, world!")


   @app.cmd(name="hi", help="Say hi")  # override subcommand name
   @app.cmd_arg('-r', '--repeat', type=int, default=1, help="How many times?")
   def say_hi(name, repeat):  # both application and subcommand args
       for i in range(repeat):
           print("Hi, %s!" % name)


   @app.cmd
   @app.cmd_defaults(name="my friend")  # overrides "visitor" for this command only
   def greetings(name):
       print("Greetings, %s." % name)


   if __name__ == '__main__':
       app.run()

The command line interface for this application behaves like this::

   $ ./example.py hello
   Hello, world!

   $ ./example.py hi --repeat=3
   Hi, visitor!
   Hi, visitor!
   Hi, visitor!

   $ ./example.py --help
   usage: example.py [-h] [--name NAME] {hello,hi,greetings} ...

   A simple greeting application.

   optional arguments:
     -h, --help            show this help message and exit
     --name NAME           Name of the person to greet

   Subcommands:
     {hello,hi,greetings}
       hello
       hi                  Say hi
       greetings

   $ ./example.py hi --help
   usage: example.py hi [-h] [-r REPEAT]

   optional arguments:
     -h, --help            show this help message and exit
     -r REPEAT, --repeat REPEAT
                           How many times?


Installation
============

Installation using `pip` is trivial, especially when using `virtualenv`::

   (yourenv) $ pip install aaargh

After succesful installation, this should work::

   (yourenv) $ python
   >>> import aaargh
   >>> help(aaargh)

.. note:

   For Python 2.6 you also need to install the `argparse` module.


History
=======

Version 0.6 (2014-02-16)
------------------------

* No longer use `pbr` for packaging (issue #12)
* Add proper licensing file (issue #9)
* Fix error message when calling the program without a subcommand under Python 3

Version 0.5 (2013-09-23)
------------------------

* No longer add global args to subcommands  (issues #3 and #5)
* Switch to `pbr` for packaging

Version 0.4 (2012-10-17)
------------------------

* Fix automatic `argparse` dependency installation when using `pip install` with
  Python 2.6.

Version 0.3 (2012-06-10)
------------------------

* Also accept global args after the subcommand

Version 0.2 (2012-05-17)
------------------------

* Add support for Python 3

Version 0.1 (2012-05-17)
------------------------

* Initial release


.. image:: https://d2weczhvl823v0.cloudfront.net/wbolster/aaargh/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free
