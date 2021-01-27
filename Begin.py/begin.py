#
# Begin.py
#
# Opdracht: Tekstidentificatie
#
# Naam: Annemarleen Bosma
#

"""
De methode __repr__(self) geeft een overzicht terug van alle dictionary’s in het model.
Doel: zodat je ermee kan testen en kan controleren dat ze werken.
> constructor en __repr__
> read_text_from_file
> make_sentence_lengths
"""

from string import punctuation


class TextModel:
    """A class supporting complex models of text."""

    def __init__(self):
        """
        Constructor.
        Create an empty TextModel.
        """

        # Maak dictionary's voor elke eigenschap

        # attributes:
        self.words = {}  # Om woorden te tellen
        self.word_lengths = {}  # Om woordlengtes te tellen
        self.stems = {}  # Om stammen te tellen
        self.sentence_lengths = {}  # Om zinslengtes te tellen

        # Maak een eigen dictionary:

        self.my_feature = {}  # Om ... te tellen

    def __repr__(self):
        """
        Display the contents of a TextModel.
        """
        s = 'Woorden:\n' + str(self.words) + '\n\n'
        s += 'Woordlengtes:\n' + str(self.word_lengths) + '\n\n'
        s += 'Stammen:\n' + str(self.stems) + '\n\n'
        s += 'Zinslengtes:\n' + str(self.sentence_lengths) + '\n\n'
        s += 'MIJN EIGENSCHAP:\n' + str(self.my_feature)
        return s

    # Voeg hier andere methodes toe.
    # Je hebt in het bijzonder methodes nodig die het model vullen.

    # METHODS

    @staticmethod
    def read_text_from_file(filename):
        """
        methode:    read_text_from_file(self, filename)
        argument:   self; verwijst naar de klasse TextModel en maakt hiervan 'a instance of a class'
        argument:   filename; van het type string.
                    self.text: variabele waaraan de inhoud toegekend is
                    van het bestand filename. Type: 1 hele lange string.
        """

        file = open(filename)
        text = file.read().replace("\n", "").rstrip("")

        return text

    def make_sentence_lengths(self, text):
        """
        De make_sentence_lengths(self) moet parameter text (type string) gebruiken om de
        dictionary self.sentence_lengths te vullen.
        output: dictionary self.sentence_lengths.
        Het resultaat van deze functie is: dictionary: sentence; words

        assert tm.sentence_lengths == {16: 1, 5: 1, 6: 1} => 1 zin met 16 woorden, 1 zin met 5 woorden, 1 zin met 6 woorden

        """
        # dus, je moet het aantal zinnen tellen, én het aantal woorden in de zin.
        # als x is zin, return True. If True, count words. if word endswhith '.?!' dan
        # count_words. If word endswith '.?!' dan return is_sentence. count_sentence =+ 1
        # het resultaat hiervan wordt dmv een dictionary getoond.

        print("The whole original string is:\n", text)
        print("")

        previous_word = "$"
        words = text.split()
        sentences = []
        word_length = 0

        # print(LoW)

        for word in words:
            if word not in ".?!" or previous_word == "$":
                word_length += 1
            if word[-1] in ".?!":
                sentences += [word_length]
                word_length = 0
            else:
                previous_word = word

        for number in sentences:
            if number not in self.sentence_lengths:
                self.sentence_lengths[number] = 1
            else:
                self.sentence_lengths[number] += 1

        return self.sentence_lengths

    # _TESTS


def run():
    model = TextModel()

    # Toon model voor het vullen
    print('TextModel:\n', model)
    # de text ophalen
    text = model.read_text_from_file("../test.txt")
    # Aanroepen die het model vullen met informatie
    model.make_sentence_lengths(text)

    # Toon model met gevulde waarden
    print('TextModel:\n', model)

    # assert tm.text == test_text


run()
