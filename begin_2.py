#
# textmodel.py
#
# Opdracht: Tekstidentificatie
#
# Naam:
#


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

    def read_text_from_file(self, filename):
        """Kopieert tekst uit TXT bestand en zet deze als string in een variabele"""
        with open(filename, 'r') as file:
            self.text=file.read().replace('\n', ' ').rstrip(" ")


    import random
    from string import punctuation

    #def make_sentence_lengths(self):



    # functie #1
    
    def make_sentence_lengths(self, text):
        """HEADER"""
        pw = "$"
        LoW = text.split()
        count = 0
        zin = []
        
        for nw in LoW:
            if nw not in ".?!" or pw == "$":
                count +=1            
            if nw[-1] in ".?!":
              #  pw = "$" 
                zin += [count]
                count = 0
            else:
                pw=nw

        for number in zin:
            if number not in self.sentence_lengths: 
                self.sentence_lengths[number] = 1
            else: 
                self.sentence_lengths[number] += 1
            
        return self.sentence_lengths


# Hier kan je dingen testen...
tm = TextModel()
# Zet hier aanroepen neer die het model vullen met informatie
print('TextModel:', tm)

