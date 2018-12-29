# Import sastrawi module
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# Reading from file
def readTextFromNotepad(file):
    files = open("keluhan.txt", "r")

    readTextResult = files.readlines()

    resultText = ''.join(readTextResult)

    return resultText

# Format string as lowercase
def sentenceCaseString(string):
    newString = string.lower()
    return newString

def tokenizeString(string):
    newTokenGenerated = string.split()

    return newTokenGenerated

# Sastrawi modified from parameters
def removedWordFromString(string):
    stop_factory = StopWordRemoverFactory()
    more_stopword = ['asam']

    # Tambahkan Stopword Baru
    data = stop_factory.get_stop_words() + more_stopword

    stopword = stop_factory.create_stop_word_remover()
    stopWordRemover = stopword.remove(string)

    return stopWordRemover

# Calling reading files
readingText = readTextFromNotepad("keluhan.txt")

print(readingText)

convertToLowercase = sentenceCaseString(readingText)

print(convertToLowercase)

newTokens = tokenizeString(convertToLowercase)

# Manually removed items
new_list = []

# ini dari parameter yang kamu kirim
arrays = ['asam', 'lambung']

for e in newTokens:
    if e not in (arrays):
        new_list.append(e)

# Filtered token list
newTokens = new_list


print("Halo token :", newTokens)


