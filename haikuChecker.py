import nltk
from nltk.corpus import cmudict

def stress(pronunciation):
    syllables = []
    for syllable in pronunciation:
        for character in syllable:
            if character.isdigit():
                syllables.append(character)
    
    return syllables
    
    
def syllablecounter(syllables):
	return len(syllables)
    
entries = cmudict.entries()   
numberedEntries = list(enumerate(entries))

def filterPunctuationFromSentence(rawSentence):
    punctuationWithoutApostrophe = [',','.','?','/','<','>','"',';',':','[',']','{','}','!','#','$','%','^','&','*','(',')','_','-','+','+','~','`']
    sentence = [char for char in rawSentence if char not in punctuationWithoutApostrophe]
    return sentence

def findIndex(wordString):
	return [ent[0] for ent in numberedEntries if ent[1][0]==wordString][0]


    
def countSyllables(sentence):
	tokens = nltk.word_tokenize(sentence)
	tokens = [w.lower() for w in tokens]
	syllables = []
	for word in tokens:
		pron = entries[findIndex(word)][1]
		syllables.append(syllablecounter(stress(pron)))
	return sum(syllables)

    
def isHaiku(haiku):
	return 17 == countSyllables(haiku)
    
#haiku = "is this a haiku i do not know if it is we will find this out"
