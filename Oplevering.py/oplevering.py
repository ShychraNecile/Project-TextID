#
# Oplevering.py
#
# Opdracht: Tekstidentificatie
#
# Naam: Annemarleen Bosma
#

from collections import Counter

class TextModel:
    """A class supporting complex models of text."""

    def __init__(self):
        """Create an empty TextModel."""
        #
        # Maak dictionary's voor elke eigenschap
        #
        self.words = {}             # Om woorden te tellen
        self.word_lengths = {}      # Om woordlengtes te tellen
        self.stems = {}             # Om stammen te tellen
        self.sentence_lengths = {}  # Om zinslengtes te tellen
        #
        # Maak een eigen dictionary
        #
        self.my_feature = {}        # Om ... te tellen

    def __repr__(self):
        """Display the contents of a TextModel."""
        s = 'Woorden:\n' + str(self.words) + '\n\n'
        s += 'Woordlengtes:\n' + str(self.word_lengths) + '\n\n'
        s += 'Stammen:\n' + str(self.stems) + '\n\n'
        s += 'Zinslengtes:\n' + str(self.sentence_lengths) + '\n\n'
        s += 'MIJN EIGENSCHAP:\n' + str(self.my_feature)
        return s

    # Voeg hier andere methodes toe.
    # Je hebt in het bijzonder methodes nodig die het model vullen.


def nomalize_dictionary(d):
    """
    input d, niet genormaliseerde dictionary
    output dn1: genormaliseerde dictionary
    """

    result = {}
    # totaal aan waardes. Resultaat.
    total = sum(d.values())
   
    for key, value in d.items():      # tuple unpacking  
        result[key] = value / total

    return result


# Hier kan je dingen testen...
tm = TextModel()
# Zet hier aanroepen neer die het model vullen met informatie
print('TextModel:', tm)