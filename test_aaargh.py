"""
Aaargh testing module.

This is very basic and not really sufficient.
"""

import shlex

import pytest

import aaargh


@pytest.fixture
def sample_app():
    app = aaargh.App(description="A simple greeting application.")
    app.arg('-r', '--repeat', type=int, default=1, help="How many times?")

    @app.cmd
    def hello(repeat):  # application level "repeat" argument is always passed
        return "Hello, world!"

    @app.cmd(name="hi", help="Say hi")  # override subcommand name
    @app.cmd_arg('--name', '-n', default="stranger",
                 help="Name of the person to greet")
    def say_hi(name, repeat):  # both application and subcommand args
        out = []
        for i in range(repeat):
            out.append("Hi, %s!" % name)
        return "\n".join(out)

    return app


@pytest.mark.parametrize("cmd_line, expected", [
    ("hello", "Hello, world!"),
    ("--repeat 2 hello", "Hello, world!"),
    ("hi", "Hi, stranger!"),
    ("-r2 hi", "Hi, stranger!\nHi, stranger!"),
    ("hi -nfoo", "Hi, foo!"),
    ("hi --name foo", "Hi, foo!"),
    ("hi --name=foo", "Hi, foo!"),
    ("hi --name=foo --name=bar", "Hi, bar!"),
    ("--repeat 2 hi --name=foo", "Hi, foo!\nHi, foo!"),
])
def test_aaargh(sample_app, cmd_line, expected):
    actual = sample_app.run(shlex.split(cmd_line))
    assert actual == expected
