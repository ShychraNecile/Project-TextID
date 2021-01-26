#
# Milestone.py
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
        self.words = {}             # Om woorden te tellen
        self.word_lengths = {}      # Om woordlengtes te tellen
        self.stems = {}             # Om stammen te tellen
        self.sentence_lengths = {}  # Om zinslengtes te tellen
        
        # Maak een eigen dictionary:
        
        self.my_feature = {}        # Om ... te tellen

        
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
    def read_text_from_file(self, filename):
        """
        methode:    read_text_from_file(self, filename) 
        argument:   self; verwijst naar de klasse TextModel en maakt hiervan 'a instance of a class'
        argument:   filename; van het type string. 
                    self.text: variabele waaraan de inhoud toegekend is 
                    van het bestand filename. Type: 1 hele lange string.   
        """

        with open("/home/annemarleen/programming/CS_for_all/Eindopdracht/test.txt") as f:
            self.text = f.read().replace("\n", "").rstrip("")            

        return self.text


        def cleanString(self, s):
            """cleanString should accept a string s and return a string withno punctuation and 
            no upper-case letters.
            """
            for p in string.punctuation:
                s = s.replace(p, '')
                s = s.lower()
                return s