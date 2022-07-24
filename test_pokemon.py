from unittest import TestCase

from pokemon import get_dmg


class Test(TestCase):
    # inputs from mail
    def test1(self):
        type_from = 'fire'
        type_to = ['grass']
        assert get_dmg(type_from, type_to) == 2

    def test2(self):
        type_from = 'fighting'
        type_to = ['ice', 'rock']
        assert get_dmg(type_from, type_to) == 4

    def test3(self):
        type_from = 'psychic'
        type_to = ['poison', 'dark']
        assert get_dmg(type_from, type_to) == 0

    def test4(self):
        type_from = 'water'
        type_to = ['normal']
        assert get_dmg(type_from, type_to) == 1

    def test5(self):
        type_from = 'fire'
        type_to = ['rock']
        assert get_dmg(type_from, type_to) == 0.5




    # some other tests
    def test_times_8(self):
        type_from = 'ice'
        type_to = ['ground', 'grass', 'dragon']
        assert get_dmg(type_from, type_to) == 8

    def test_no_type_to(self):
        type_from = 'ice'
        type_to = []
        assert get_dmg(type_from, type_to) == 1

