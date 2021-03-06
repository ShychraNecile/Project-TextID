#
# Begin.py
#
# Opdracht: Tekstidentificatie
#
# Naam: Annemarleen Bosma en Johan Kamps
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
        
        with open(filename) as f:            
            self.text = f.read().replace("\n", "").rstrip("")        

        #return self.text
    
  
    def make_sentence_lengths(self):
        """        
        De make_sentence_lengths(self) moet parameter text (type string) gebruiken om de
        dictionary self.sentence_lengths te vullen.
        output: dictionary self.sentence_lengths.
        Het resultaat van deze functie is: dictionary: sentence; words 

        assert tm.sentence_lengths == {16: 1, 5: 1, 6: 1} => 1 zin met 16 woorden, 1 zin met 5 woorden, 1 zin met 6 woorden
        
        """

        print("The whole original string is:\n",self.text)
        print("")
        
        pw = "$"
        LoW = self.text.split()
        count = 0
        zin = []

        total_num_words_text = len(LoW)
        print("The total number of words in the text is: ", total_num_words_text)
         

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


# _TESTS
tm = TextModel()

# Zet hier aanroepen neer die het model vullen met informatie
print('TextModel:\n', tm)
