******
Aaargh
******

*Aaargh*: an astonishingly awesome application argument helper.

*Aaargh* is a Python module that makes building friendly command line
applications really easy. Applications built with *Aaargh* provide a single
executable with a subcommand for each exposed Python function. Each subcommand
may have its own command line arguments. This is similar to the way version
control systems provide many different commands using a single entry point.
(Examples include ``bzr commit`` and ``git checkout``).

*Aaargh* is named after one of the castles in the movie *Monty Python and the
Holy Grail*. The acronym *Aaargh* expands to *an astonishingly awesome
application argument helper*, but omits a few letters to make it triple A.

*Aaargh* works with both Python 2.6+ and Python 3.


Rationale
=========

The Python standard library contains the `optparse`, `getopt`, and `argparse`
modules, and out in the wild you will find many alternative command line
interface libraries stacked on top of these, such as *Cliff*, *Cement*,
*opster*, *plac*, and many others. These libraries either separate the CLI part
of your application from the actual code, force yet another API upon you, or
even force you to hide your code in non-obvious framework constructs.

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
   @app.cmd_defaults(who="my friend")  # overrides "visitor" for this command only
   def greetings(who):
       print("Greetings, %s." % who)


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

Now verify that it works::

   (yourenv) $ python
   >>> import aaargh
   >>> help(aaargh)

.. note:

   For Python 2.6 you also need to install the `argparse` module.


History
=======

Version 0.2 (2012-05-17)
------------------------

* Add support for Python 3

Version 0.1 (2012-05-17)
------------------------

* Initial release
