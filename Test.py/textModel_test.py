from begin import Textmodel
from unittest import TestCase


class PersonTest(TestCase): # klasse TestCase heeft een aantal eigen methoden
    def make_sentence_lengths(self, text):

        tm = TextModel()
        # zorg dat deze tekst in een bestand genaamd test.txt staat
        test_text = """Dit is een korte zin. Dit is geen korte zin, omdat
        deze zin meer dan 10 woorden en een getal bevat! Dit is
        geen vraag, of wel?"""

        tm.read_text_from_file('test.txt')
        assert tm.text == test_text