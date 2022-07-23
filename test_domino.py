from unittest import TestCase

from domino import iteration


class Test(TestCase):
    def test_simple_right(self):
        domino = "/||"
        assert iteration(domino) == "//|"

    def test_simple_left(self):
        domino = "||\\"
        assert iteration(domino) == "|\\\\"

    def test_not_falling_right(self):
        domino = "||////"
        assert iteration(domino) == domino

    def test_not_falling_left(self):
        domino = "\\\\\\|||"
        assert iteration(domino) == domino

    def test_example_input(self):
        domino = "||//||\\||/\\|"
        assert iteration(domino) == "||///\\\\||/\\|"
