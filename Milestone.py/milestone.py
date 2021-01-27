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
> make_word_lenghts
> make_words
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

        with open("/home/annemarleen/programming/CS_for_all/Eindopdracht/test.txt") as f:
            self.text = f.read().replace("\n", "").rstrip("")            

        return self.text


    def make_clean_string(self, s):
        """
        This method, make_clean_string(self, s) 
        arguments: s, type string 
        return: string, which has no punctuation or upper-case letters.
        """

        clean_string = ""        

        for p in punctuation:
            s = s.replace(p, "")
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

    
        # def make_word_lengths(self, s):
        #     """
        #     arguments: s, this is the returnvalue of the clean_string method.
        #     return: dictionairy of the lenght of the words.
        #     """

    def make_word_lengths(self, s):
        """     
        De make_word_lengths(self, s) moet parameter s(type string) gebruiken om de
        dictionary self.word_lengths te vullen.
        output: dictionairy of the lenght of the words: self.word_lengths.
        Het resultaat van deze functie is: dictionary: het aantal woorden; lenght of words     

        Dus, het aantal woorden dat uit een bepaald aantal karakters bestaat.
        """   
        print("The whole STRING is:\n", self.s)
        print("")

        cleaned_string = self.s  
        print(cleaned_string)

        self.word_lengths = {}
        #character_count = 0
        words = []
        words = cleaned_string.split()
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


