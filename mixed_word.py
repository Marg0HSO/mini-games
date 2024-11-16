import random as r

def getWordList(file:str)->list:
    with open(file, "r") as f:
        files = f.read()
        wordList = files.split(",")
    f.close
    return wordList

wordList = getWordList("MixedWord\words.txt")
word = r.choice(wordList)

def mixingWord(word:str)->str:
    assert type(word) == str, "Il faut un mot sous le type String"
    letters = []
    for letter in word:
        letters.append(letter)
    r.shuffle(letters)
    temp = ""
    for elt in letters:
        temp += elt
    return temp

def mainloop(word:str):
    mixed_word = mixingWord(word)
    player_word = ""
    while player_word != word:
        print(mixed_word)
        player_word = input("Votre proposition --> ")
        if player_word == word:
            print("gg")
        else:
            print("pas encore")

mainloop(word)