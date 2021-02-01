#
# Oplevering.py
#
# Opdracht: Tekstidentificatie
#
# Naam: Annemarleen Bosma en Johan Kamps
#


"""
De methode __repr__(self) geeft een overzicht terug van alle dictionary’s in het model.
Doel: zodat je ermee kan testen en kan controleren dat ze werken.
> constructor en __repr__ :: CHECK
> clean_string :: CHECK
> make_word_lenghts
> make_words
> make_stems
"""

from string import punctuation
from nltk.stem import PorterStemmer
from math import log2
ps = PorterStemmer()

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
        self.list_of_log_probs = []
        # Maak een eigen dictionary:
        
        self.punctuation = {}       # Interpunctie tellen

        
    def __repr__(self):
        """
        Display the contents of a TextModel.
        """
        s = 'Woorden:\n' + str(self.words) + '\n\n'
        s += 'Woordlengtes:\n' + str(self.word_lengths) + '\n\n'
        s += 'Stammen:\n' + str(self.stems) + '\n\n'
        s += 'Zinslengtes:\n' + str(self.sentence_lengths) + '\n\n'
        s += 'Interpunctie:\n' + str(self.punctuation)
        return s



    # METHODES

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

        return self.text


    def clean_string(self, s):
        """
        This method, make_clean_string(self, s) 
        arguments: s, type string 
        return: string, which has no punctuation or upper-case letters.
        """
        clean_string = str.maketrans('','',punctuation)        
        return self.text.translate(clean_string) 


    # TEKSTEIGENSCHAPPEN
    def make_sentence_lengths(self):
        """        
        De make_sentence_lengths(self) moet parameter text (type string) gebruiken om de
        dictionary self.sentence_lengths te vullen.
        output: dictionary self.sentence_lengths.
        Het resultaat van deze functie is: dictionary: sentence; words     
        """
   
        pw = "$"
        LoW = self.text.split()
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

    
      
    def make_word_lengths(self):
        """     
        Make_word_lengths(self) geeft de het aantal woorden in de text weer en 
        de lengte er van.
        """   
        LoW = self.text.split()   

        for woord in LoW:
            number = len(woord)
            if number not in self.word_lengths:
                self.word_lengths[number] = 1
            else:
                self.word_lengths[number] += 1
        return self.word_lengths


    def make_words(self):
        """     
        TEXT
        """   
        ctxt = self.clean_string(self.text)
        LoW = ctxt.split() 

        for word in LoW:
            if word not in self.words:
                self.words[str(word)] = 1
            else:
                self.words[str(word)] += 1
            
        return self.words


    def make_stems(self):
        """geeft de "stam" weer van een woord en telt het voorkomen"""
        ctxt = self.clean_string(self.text)
        LoW = ctxt.split() 
        for word in LoW:
            if ps.stem(word) not in self.stems:
                self.stems[ps.stem(word)] = 1
            else:
                self.stems[ps.stem(word)] += 1
        return self.stems
        

    def make_punctuation(self):
        """     
        make_punctuation geeft de interpunctie en het voorkomen ervan weer.
        """   
        LoW = self.text.split() 
        for word in LoW:
            for letter in word:
                    if letter in punctuation:
                        if letter not in self.punctuation:
                            self.punctuation[letter] = 1
                        else:
                            self.punctuation[letter] += 1       
        return self.punctuation


    def normalize_dictionary(self, d):
        """Zet het absolute aantal voorkomens om naar een relatief deel"""
        total = sum(d.values())
        for key, value in d.items():
            d[key] = value / total
        return d


    def smallest_value(self, nd1, nd2):
        """Kleinste waarde tussen twee dictionaries"""
        min_nd1 = min(nd1.values())
        min_nd2 = min(nd2.values())
        return min(min_nd1, min_nd2)

    
    def compare_dictionaries(self, d, nd1, nd2):
        """ De method compare_dictionaries moet twee kansen berekenen: de kans dat 
        de dictionary d voortkomt uit de verdeling van de gegevens in de 
        genormaliseerde dictionary nd1, en dezelfde kans, maar dan voor nd2."""
        total_nd1 = 0.0
        total_nd2 = 0.0
        epsilon = self.smallest_value(nd1, nd2) / 2

        for key, value in d.items():
            if key not in nd1.keys():
                total_nd1 += 1 * log2(epsilon)   
            else:
                for key1, value1 in nd1.items():
                    if key == key1:
                        total_nd1 += value * log2(value1)
            
        for key, value in d.items():
            if key not in nd2.keys():
                total_nd2 += 1 * log2(epsilon)           
            else:
                for key1, value1 in nd2.items():
                    if key == key1:
                        total_nd2 += value * log2(value1)   
            
        self.list_of_log_probs = [total_nd1, total_nd2]
       



    def create_all_dictionaries(self) :
        """Draait alle methodes die dictionaries vullen"""
        self.make_sentence_lengths()
        self.make_word_lengths()
        self.make_words()
        self.make_stems()
        self.make_punctuation()

# assert tm.word_lengths == {2 karakters: 6 woorden, 3 karakters: 10 woorden, 4: 4, 5: 6, 7: 1}



tm=TextModel()

print(' +++++++++++ Model 1 +++++++++++ ')
tm1 = TextModel()
tm1.read_text_from_file('train1.txt')
tm1.create_all_dictionaries()  # deze is hierboven gegeven
print(tm1)

print(' +++++++++++ Model 2+++++++++++ ')
tm2 = TextModel()
tm2.read_text_from_file('train2.txt')
tm2.create_all_dictionaries()  # deze is hierboven gegeven
print(tm2)


print(' +++++++++++ Onbekende tekst +++++++++++ ')
tm_unknown = TextModel()
tm_unknown.read_text_from_file('unknown.txt')
tm_unknown.create_all_dictionaries()  # deze is hierboven gegeven
print(tm_unknown)