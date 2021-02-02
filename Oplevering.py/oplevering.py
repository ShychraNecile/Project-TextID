#
# Oplevering.py
#
# Opdracht: Tekstidentificatie
#
# Naam: Annemarleen Bosma en Johan Kamps
#


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
        
        # Dictionary's voor elke eigenschap:
        
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

        with open("./test.txt") as f:
            self.text = f.read().replace("\n", "").rstrip("")            

        return self.text


    def clean_string(self, s):
        """
        This method, make_clean_string(self, s) 
        arguments: s, type string 
        return: string, which has no punctuation or upper-case letters.
        """        
        # clean_string = ""        

        # for p in punctuation:
        #     s = self.text.replace(p, "")
        #     clean_string = s.lower()
            
        # return clean_string      

        clean_string = str.maketrans('','',punctuation)          
        clean_str = self.text.translate(clean_string) 
        clean_txt = ""

        for word in clean_str:
            clean_txt += word.lower()

        return clean_txt


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
                pw = nw

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
        LoW = self.clean_string(self.text).split()   

        for woord in LoW:
            number = len(woord)
            if number not in self.word_lengths:
                self.word_lengths[number] = 1
            else:
                self.word_lengths[number] += 1

        return self.word_lengths


    def make_words(self):
        """
        De methode make_words(self) creeert een dictionary van de opgeschoonde woorden (zelf).
        Output: dictionary van een woord als key, en als value het aantal dat de desbetreffende key voorkomt.
        return: dictionary self.words
        
        Dus, woord : getal hoe vaak het voorkomt in de opgeschoonde string.
        assert tm.words == { 'dit': 3, 'is': 3, 'een': 2, 'korte': 2, 'zin': 3, 'geen': 2, 'omdat': 1, 'deze': 1, 'meer': 1, 'dan': 1, '10': 1, 'woorden': 1,
        'en': 1, 'getal': 1, 'bevat': 1, 'vraag': 1, 'of': 1, 'wel': 1}
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
        """
        Zet het absolute aantal voorkomens om naar een relatief deel
        """
        total = sum(d.values())

        for key, value in d.items():
            d[key] = value / total

        return d


    def smallest_value(self, nd1, nd2):
        """
        Kleinste waarde tussen twee dictionaries
        """
        min_nd1 = min(nd1.values())
        min_nd2 = min(nd2.values())

        return min(min_nd1, min_nd2)

    
    def compare_dictionaries(self, d, nd1, nd2):
        """ 
        De method compare_dictionaries moet twee kansen berekenen: 

        1) de kans dat de dictionary d voortkomt uit de verdeling van de gegevens in de 
        genormaliseerde dictionary nd1
        2) dezelfde kans, maar dan voor nd2.

        return: Lijst aan log-waarschijnlijkheden van biede dictionaries.
        Bijvoorbeeld [log1, log2] (de eerste is de log-waarschijnlijkheden voor nd1 en de tweede voor nd2).
        """
        
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

        return self.list_of_log_probs


    def compare_text_with_two_models(self, model1, model2):
        """
        Functie moet:
        - compare_dictionaries aanroepen voor elke teksteigenschapsictionary.
        - de teksteigenschapdictionary vergelijken met de corresponderende,
        genormaliserende dictionaries in model1 en model2.

        Dus, Vergelijkt twee teksten met een andere tekst en geeft terug
        wat het meeste overeen komt
        """

        words_list = self.compare_dictionaries(self.words, model1.words, model2.words)
        words = ['%.2f' % elem for elem in words_list]

        word_lengths_list = self.compare_dictionaries(self.word_lengths, model1.word_lengths, model2.word_lengths)
        word_lengths = ['%.2f' % elem for elem in word_lengths_list]

        sentence_lengths_list = self.compare_dictionaries(self.sentence_lengths, model1.sentence_lengths, model2.sentence_lengths)
        sentence_lengths = ['%.2f' % elem for elem in sentence_lengths_list]

        stems_list = self.compare_dictionaries(self.stems, model1.stems, model2.stems)
        stems = ['%.2f' % elem for elem in stems_list]

        punctuation_list = self.compare_dictionaries(self.punctuation, model1.punctuation, model2.punctuation)
        punctuation = ['%.2f' % elem for elem in punctuation_list]

        var_list = (words_list, word_lengths_list, sentence_lengths_list, stems_list, punctuation_list)

        print("DIT IS EEN LIJST VAN: ", var_list)

        win1 = 0  
        win2 = 0
        Model = 0

        for var in var_list:
            if max(var) == var[0]:
                win1 += 1
            else:
                win2 += 1
        
        if win1 > win2:
            Model += 1
        else:
            Model += 2

        print(
            "Vergelijkingsresultaten:\n"
            "\n"
            "naam" + "\t\t\t" + "Model1" + "\t\t\t" + "Model2\n"
            "----" + "\t\t\t" + "----" + "\t\t\t" + "----\n"
            "words" + "\t\t\t" + (words[0])+ "\t\t\t" + (words[1]) + "\n"
            "word_lengths" + "\t\t" + (word_lengths[0])+ "\t\t\t" + (word_lengths[1]) + "\n"
            "sentence_lengths" + "\t" + (sentence_lengths[0])+ "\t\t\t" + (sentence_lengths[1]) + "\n"
            "stems" + "\t\t\t" + (stems[0])+ "\t\t\t" + (stems[1]) + "\n"
            "punctuation" + "\t\t" + (punctuation[0])+ "\t\t\t" + (punctuation[1]) + "\n"
            "\n"
            "-->  Model 1 wint op "+str(win1)+" features\n"
            "-->  Model 2 wint op "+str(win2)+" features\n"
            "\n"
            "+++++     Model "+str(Model)+" komt beter overeen!     +++++"
            )


    def create_all_dictionaries(self) :
        """
        Draait alle methodes die ervoor zorgen dat de dictionaries
        gevuld worden.
        """
        self.make_sentence_lengths()
        self.make_word_lengths()
        self.make_words()
        self.make_stems()
        self.make_punctuation()


    def normalize(self):
        self.normalize_dictionary(self.words)
        self.normalize_dictionary(self.word_lengths)
        self.normalize_dictionary(self.sentence_lengths)
        self.normalize_dictionary(self.stems)
        self.normalize_dictionary(self.punctuation)



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

# de hoofdvergelijkingsmethode
tm_unknown.compare_text_with_two_models(tm1, tm2)

tm=TextModel()

# print(' +++++++++++ Model 1 +++++++++++ ')
# tm1 = TextModel()
# tm1.read_text_from_file('test.txt')
# tm1.create_all_dictionaries()  # deze is hierboven gegeven
# tm1.normalize()
# print(tm1)

# print(' +++++++++++ Model 2+++++++++++ ')
# tm2 = TextModel()
# tm2.read_text_from_file('another.txt')
# tm2.create_all_dictionaries()  # deze is hierboven gegeven
# tm2.normalize()
# print(tm2)

# print(' +++++++++++ Onbekende tekst +++++++++++ ')
# tm_unknown = TextModel()
# tm_unknown.read_text_from_file('output.txt')
# tm_unknown.create_all_dictionaries()  # deze is hierboven gegeven
# print(tm_unknown) 