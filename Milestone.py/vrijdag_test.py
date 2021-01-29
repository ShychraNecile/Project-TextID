from collections import Counter


class TextModel:
    """A class supporting complex models of text."""

    def __init__(self):
        """
        Constructor.
        Creates an empty TextModel.
        """
        
        # Maak dictionary's voor elke eigenschap
        
        # attributes: 
        self.words = {}             # Om woorden te tellen
        self.word_lengths = {}      # Om woordlengtes te tellen
        self.stems = {}             # Om stammen te tellen
        self.sentence_lengths = {}  # Om zinslengtes te tellen
        
        # Maak een eigen dictionary:
        
        self.my_feature = {}        # Om ... te tellen

        #self.punctuation = {}


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