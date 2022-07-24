from unittest import TestCase

from reverse_domino import iteration


class Test(TestCase):
    def test_simple_right(self):
        domino = "/||"
        assert iteration(domino) == "|||"

    def test_simple_left(self):
        domino = "||\\"
        assert iteration(domino) == "|||"

    def test_example_input(self):
        domino = "||////\\\\\\|////|"
        assert iteration(iteration(domino)) == "||//||||\\|//|||"

    def test_leaning(self):
        domino = "/\\"
        assert iteration(domino) == "||"

    def test_leaning2(self):
        domino = "///\\\\\\"
        assert iteration(domino) == "//||\\\\"

    def test_middle(self):
        domino = "/|\\"
        assert iteration(domino) == "|||"

    def test_middle2(self):
        domino = "/////////|\\"
        assert iteration(domino) == "////////|||"

    def test_ten_iterations(self):
        domino = "///////////////|||||"
        for i in range(10):
            domino = iteration(domino)
        assert domino == "/////|||||||||||||||"

    def test_only_right(self):
        domino = "///"
        assert iteration(domino) == "//|"

    def test_only_lef(self):
        domino = "\\\\\\"
        assert iteration(domino) == "|\\\\"


