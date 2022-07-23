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

    def test_leaning(self):
        domino = "/\\"
        assert iteration(domino) == domino

    def test_leaning2(self):
        domino = "///\\\\\\"
        assert iteration(domino) == domino

    def test_middle(self):
        # middle block should not fall to either side
        domino = "/|\\"
        assert iteration(domino) == domino

    def test_middle2(self):
        # middle block should not fall to either side, even when there is more blocks pushing it
        domino = "/////////|\\"
        assert iteration(domino) == domino

    def test_two_iterations_right(self):
        domino = "/||"
        assert iteration(iteration(domino)) == "///"

    def test_two_iterations_left(self):
        domino = "||\\"
        assert iteration(iteration(domino)) == "\\\\\\"

    def test_ten_iterations(self):
        domino = "/||||||||||||||||||||||||||||"
        for i in range(10):
            domino = iteration(domino)
        assert domino == "///////////||||||||||||||||||"
