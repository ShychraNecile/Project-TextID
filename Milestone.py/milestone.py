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
> constructor en __repr__ :: CHECK
> clean_string :: CHECK
> make_word_lenghts :: CHECK
> make_words :: CHECK
> make_stems
"""

from string import punctuation

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

        #return self.text


    def clean_string(self, text):
        """
        This method, make_clean_string(self, s) 
        arguments: s, type string 
        return: string, which has no punctuation or upper-case letters.
        """

        clean_string = ""        

        for p in punctuation:
            s = self.text.replace(p, "")
            clean_string = s.lower()
            
        return clean_string       


    # TEKSTEIGENSCHAPPEN
    def make_sentence_lengths(self, text):
        """        
        De make_sentence_lengths(self) moet parameter text (type string) gebruiken om de
        dictionary self.sentence_lengths te vullen.
        output: dictionary self.sentence_lengths.
        Het resultaat van deze functie is: dictionary: sentence; words     
        """
        print("The whole original string is:\n",self.text)
        print("")
        
        pw = "$"
        LoW = self.text.split()
        count = 0
        zin = []

        total_num_words_text = len(LoW)
        print("Total number of words in text are: ", total_num_words_text)                   

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

        print("sentence lengths")
        return self.sentence_lengths    



    def make_word_lengths(self):
        """     
        De make_word_lengths(self, s) moet parameter s(type string) gebruiken om de
        dictionary self.word_lengths te vullen.
        output: dictionairy of the lenght of the words: self.word_lengths.
        Het resultaat van deze functie is: dictionary: het aantal woorden; lenght of words     

        Dus, het aantal woorden dat uit een bepaald aantal karakters bestaat.
        """
        clean_str = clean_string(self.text)

        self.word_lengths = {}
        #character_count = 0
        words = []
        words = clean_str.split()
        current_word = []

        keys = []
        values = []
        
        print(words)
        total_num_words_clean_string = len(words)
        print("The total number of words in the no-puntuacion string is: ", total_num_words_clean_string)

        for word in words:
            lenght_of_word = len(word)
            print(f"The lenght of the word '{word}' is: ", lenght_of_word)
            keys.append(lenght_of_word)
            character_count = 0
            
            if lenght_of_word not in self.word_lengths:
                self.word_lengths[lenght_of_word] = 1
            else:
                self.word_lengths[lenght_of_word] += 1
            
                return self.word_lengths


# assert tm.word_lengths == {2 karakters: 6 woorden, 3 karakters: 10 woorden, 4: 4, 5: 6, 7: 1}



    def make_words(self, text):
        """
        De methode make_words(self) creeert een dictionary van de opgeschoonde woorden (zelf).
        Output: dictionary van een stam als key, en als value het aantal dat de desbetreffende key voorkomt.
        return: dictionary self.stems
        
        Dus, stam : getal hoe vaak het voorkomt in het opgeschoonde woord.

        assert tm.words == { 'dit': 3, 'is': 3, 'een': 2, 'korte': 2, 'zin': 3, 'geen': 2, 'omdat': 1, 'deze': 1, 'meer': 1, 'dan': 1, '10': 1, 'woorden': 1,
        'en': 1, 'getal': 1, 'bevat': 1, 'vraag': 1, 'of': 1, 'wel': 1}
        """

        self.words = {}
        cleaned_string = tm.make_clean_string(self.text)
        print(cleaned_string)
                
        LoW = cleaned_string.split()
        print(LoW)

        word_count = 0
        
        for word in LoW:
            if word in self.words:
                self.words[word] += 1
            else:
                self.words[word]=1
        return self.words


    def make_stems(self):
        """
        De methode make_stems(self) creëert een dictionary van de stammen van 
        de opgeschoonde woorden.
        Output: dictionary van een stam als key, en als value het aantal dat de desbetreffende key voorkomt.
        return: dictionary self.words
        
        Dus, woord : getal hoe vaak het voorkomt in de opgeschoonde string.
      
        assert tm.stems == {'dit': 3, 'is': 3, 'een': 2, 'kort': 2, 'zin': 3, 'gen': 2,
        'omdat': 1, 'dez': 1, 'mer': 1, 'dan': 1, '10': 1, 'woord': 1, 'en': 1, 'getal': 1,
        'bevat': 1, 'vrag': 1, 'of': 1, 'wel': 1 }


        Om make_stems te implementeren, moet je een functie schrijven die woorden als invoer krijgt en stammen als uitvoer geeft. Je mag hierbij:.
        """




        # _TESTS

tm = TextModel()
print('TextModel:\n', tm)
tm.read_text_from_file("/home/annemarleen/programming/CS_for_all/Eindopdracht/test.txt")
# tm = TextModel()
# tm.make_sentence_lengths("/home/annemarleen/programming/CS_for_all/Eindopdracht/test.txt")
# #assert tm.sentence_lengths == {16: 1, 5: 1, 6: 1}
# tm = TextModel()
# tm.make_clean_string("/home/annemarleen/programming/CS_for_all/Eindopdracht/test.txt")
# #assert clean_s == clean_text

# test make_word_lengths
tm = TextModel()
tm.read_text_from_file("/home/annemarleen/programming/CS_for_all/Eindopdracht/test.txt")
tm.make_word_lengths("/home/annemarleen/programming/CS_for_all/Eindopdracht/test.txt")
assert tm.word_lengths == {2: 6, 3: 10, 4: 4, 5: 6, 7: 1}


