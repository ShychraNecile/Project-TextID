#
# Oplevering.py
#
# Opdracht: Tekstidentificatie
#
# Naam: Annemarleen Bosma en Johan Kamps
#

import re
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
       
        self.words = {}             # Om woorden te tellen
        self.word_lengths = {}      # Om woordlengtes te tellen
        self.stems = {}             # Om stammen te tellen
        self.sentence_lengths = {}  # Om zinslengtes te tellen

        self.list_of_log_probs = []
                
        self.punctuation = {}       # Interpunctie tellen
        self.syllables = {}         # Lettergrepen tellen
        self.dialog_lengths = {}    # Lengtes van dialoogzinnen te tellen
        self.gedeelte_dialoog = 0   # Deel van de tekst dat dialoog is


    def __repr__(self):
        """
        Display the contents of a TextModel.
        """
        s = 'Woorden:\n' + str(self.words) + '\n\n'
        s += 'Woordlengtes:\n' + str(self.word_lengths) + '\n\n'
        s += 'Stammen:\n' + str(self.stems) + '\n\n'
        s += 'Zinslengtes:\n' + str(self.sentence_lengths) + '\n\n'
        s += 'Interpunctie:\n' + str(self.punctuation) + '\n\n'
        s += 'Lettergrepen:\n' + str(self.syllables) + '\n\n'
        s += 'Dialooglengte:\n' + str(self.dialog_lengths) + '\n\n'
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
            data = f.read().replace("\n", "").rstrip("")            
            data = data.replace('\xad', '')
            data = data.replace('\xad-', '')
            data = data.replace('\u00ad', '')
            data = data.replace('\N{SOFT HYPHEN}', '')
            self.text = data
        return self.text


    def clean_string(self, s):
        """
        This method, make_clean_string(self, s) 
        arguments: s, type string 
        return: string, which has no punctuation or upper-case letters.
        """
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

    def make_dialog(self):
        """
        telt het aantal zinnen dialoog in de tekst
        """ 

        pw = "^"
        dLoW = self.text.split()
        count = 0
        zin = []
        LoW = []
        totaal = 0
        tot_word = 0
        
        for word in dLoW:
            tot_word += 1
            LoW += [word.strip()]

        for word in LoW:
            if len(word) < 3 and pw == "$": #korter dan drie kan geen "zin" zijn
                count +=1
            elif len(word) < 3 and pw == "^": #korter dan drie kan geen "zin" zijn
                None
            elif word[0] == '"' and word[-1] == '"' and word[-2] in punctuation: #zin van 1 woord           
                zin += [1]
                pw = "^"
            elif word[0] == '"' and word[-1] == '"' and word[-2] not in punctuation: #zin van 1 woord zonder interpunctie,dus waarsch geen zin
                count = 0
                pw = "^"
            elif word[0] == '"' and word[-1] != '"': #begin van de zin
                count += 1
                pw = "$"
            elif word[0] != '"' and word[-1] != '"' and pw == "$": #woord in de zin
                count +=1
            elif word[0] != '"' and word[-1] == '"' and word[-2] in punctuation and pw == "$": #einde van geldige zin
                count += 1
                zin += [count]
                pw = "^" 
                count = 0
            elif word[0] != '"' and word[-1] == '"' and word[-2] not in punctuation and pw == "$": #einde van ongeldige zin (niet afgesloten met interpunctie)
                count = 0
                pw = "^"
            else:
                None
        
        for number in zin:
            if number not in self.dialog_lengths: 
                self.dialog_lengths[number] = 1
            else: 
                self.dialog_lengths[number] += 1
        
        for key, value in self.dialog_lengths.items():
            totaal += (int(key) * int(value))

        deel = totaal/tot_word
        self.gedeelte_dialoog = '%.2f' % deel
        


    def make_syllables(self):
        """telt lettergrepen per woord"""
        LoW = self.text.split()
        LoS = []
        for word in LoW:
            if len(re.findall('(?!e$)[aeiouy]+', word, re.I) + re.findall('^[^aeiouy]*e$', word, re.I)) == 0:
                LoS += str(1)
            else: 
                LoS += str(len(
                re.findall('(?!e$)[aeiouy]+', word, re.I) +
                re.findall('^[^aeiouy]*e$', word, re.I)
                ))
        for number in LoS:
            if number not in self.syllables:
                self.syllables[number] = 1
            else:
                self.syllables[number] += 1 



    def normalize_dictionary(self, d):
        """Zet het absolute aantal voorkomens om naar een relatief deel"""
        total = sum(d.values())
        for key, value in d.items():
            d[key] = value / total
        return d


    def smallest_value(self, nd1, nd2):
        """Kleinste waarde tussen twee dictionaries"""
        min_nd1 = min(nd1.values(), default=0)
        min_nd2 = min(nd2.values(), default=0)
        
        if min_nd1 == min_nd2:
            return min_nd1
        else:
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
            if key == 0:
                total_nd1 = 0.01
            elif key not in nd1.keys():
                total_nd1 += 1 * log2(epsilon)   
            else:
                for key1, value1 in nd1.items():
                    if key == key1:
                        total_nd1 += value * log2(value1)
            
        for key, value in d.items():
            if key == 0:
                total_nd2 = 0.01
            elif key not in nd2.keys():
                total_nd2 += 1 * log2(epsilon)           
            else:
                for key1, value1 in nd2.items():
                    if key == key1:
                        total_nd2 += value * log2(value1)   
            
        self.list_of_log_probs = [total_nd1, total_nd2]

        return self.list_of_log_probs


    def compare_text_with_two_models(self, model1, model2):
        """Vergelijkt twee teksten met een andere tekst en geeft terug wat het meeste overeen komt"""
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
        syllables_list = self.compare_dictionaries(self.syllables, model1.syllables, model2.syllables)
        syllables = ['%.2f' % elem for elem in syllables_list]
        dialog_lengths_list = self.compare_dictionaries(self.dialog_lengths, model1.dialog_lengths, model2.dialog_lengths)
        dialog_lengths = ['%.2f' % elem for elem in dialog_lengths_list]
        var_list = (words_list, word_lengths_list, sentence_lengths_list,stems_list, punctuation_list, syllables_list, dialog_lengths_list)
        win1 = 0  
        win2 = 0
        Model= 0

        for var in var_list:
            if max(var) == var[0] and max(var) != var[1]:
                win1 += 1
            elif max(var) == var[1] and max(var) != var[0]:
                win2 += 1
            else:
                None
                
        if abs(float(tm_unknown.gedeelte_dialoog)-float(tm1.gedeelte_dialoog)) < abs(float(tm_unknown.gedeelte_dialoog)-float(tm2.gedeelte_dialoog)):
            win1 += 1
        elif tm1.gedeelte_dialoog == tm2.gedeelte_dialoog:
            None
        else:
            win2 += 1
            
        if win1 > win2:
            Model += 1
        elif win2 > win1:
            Model += 2
            

        print(
            "Vergelijkingsresultaten:\n"
            "\n"
            "naam" + "\t\t\t" + "Model1" + "\t\t\t" + "Model2\n"
            "----" + "\t\t\t" + "----" + "\t\t\t" + "----\n"
            "words" + "\t\t\t" + (words[0])+ "\t\t" + (words[1]) + "\n"
            "word_lengths" + "\t\t" + (word_lengths[0])+ "\t\t" + (word_lengths[1]) + "\n"
            "sentence_lengths" + "\t" + (sentence_lengths[0])+ "\t\t" + (sentence_lengths[1]) + "\n"
            "stems" + "\t\t\t" + (stems[0])+ "\t\t" + (stems[1]) + "\n"
            "punctuation" + "\t\t" + (punctuation[0])+ "\t\t" + (punctuation[1]) + "\n"
            "syllables" + "\t\t" + (syllables[0])+ "\t\t" + (syllables[1]) + "\n"
            "dialog_lengths" + "\t\t" + (dialog_lengths[0])+ "\t\t\t" + (dialog_lengths[1]) + "\n"
            "dialog_gedeelte" + "\t\t" + tm1.gedeelte_dialoog + "\t\t\t" + tm2.gedeelte_dialoog + "\n"
            "\n"
            "-->  Model 1 wint op "+str(win1)+" features\n"
            "-->  Model 2 wint op "+str(win2)+" features\n"
            "\n"
            "+++++     Model "+str(Model)+" komt beter overeen!     +++++"
            )

    #, word_lengths, sentence_lengths, stems, punctuation



    def create_all_dictionaries(self) :
        """Draait alle methodes die dictionaries vullen"""
        self.make_sentence_lengths()
        self.make_word_lengths()
        self.make_words()
        self.make_stems()
        self.make_punctuation()
        self.make_syllables()
        self.make_dialog()

    def normalize(self):
        self.normalize_dictionary(self.words)
        self.normalize_dictionary(self.word_lengths)
        self.normalize_dictionary(self.sentence_lengths)
        self.normalize_dictionary(self.stems)
        self.normalize_dictionary(self.punctuation)
        self.normalize_dictionary(self.syllables)
        self.normalize_dictionary(self.dialog_lengths)

# assert tm.word_lengths == {2 karakters: 6 woorden, 3 karakters: 10 woorden, 4: 4, 5: 6, 7: 1}


print(' +++++++++++ Model 1 +++++++++++ ')
tm1 = TextModel()
tm1.read_text_from_file('adams.txt') #vijf hitchhikersguide boeken
tm1.create_all_dictionaries()  # deze is hierboven gegeven
print(tm1)

print(' +++++++++++ Model 2+++++++++++ ')
tm2 = TextModel()
tm2.read_text_from_file('colfer.txt') # 4 ARTEMIS FOWL boeken
tm2.create_all_dictionaries()  # deze is hierboven gegeven
print(tm2)


print(' +++++++++++ Onbekende tekst +++++++++++ ')
tm_unknown = TextModel()
tm_unknown.read_text_from_file('mostly_harmless.txt') # colfer.txt :6e hitchhikersboek geschreven door Colfer / mostly_harmless.txt : Douglas Adams 5e HHGTG boek
tm_unknown.create_all_dictionaries()  # deze is hierboven gegeven
print(tm_unknown)

# de hoofdvergelijkingsmethode
tm_unknown.compare_text_with_two_models(tm1, tm2)

tm=TextModel()

