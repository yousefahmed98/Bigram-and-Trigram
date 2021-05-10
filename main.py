import collections
from collections import Counter
import pandas as pd

import tkinter  as tk

if __name__ == '__main__':
    df = pd.read_csv("poems.csv")
    poems = df.poem_text
    corpus = [sentence for sentence in list(poems) if isinstance(sentence, str)]
    #print(corpus)
    #print(len(corpus))
    def buildBigramModel(corpus):
        bigramModel = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))
       #corpus = [word.lower() for word in corpus if word.isaplha()]
        for sentence in corpus:
            sentence = sentence.split()
            for i in range(len(sentence) - 1):
                bigramModel[sentence[i]][sentence[i + 1]] += 1
        for firstWord in bigramModel:
            totalSecWords = float(sum(bigramModel[firstWord].values()))
            for secWord in bigramModel[firstWord]:
                bigramModel[firstWord][secWord] /= totalSecWords

        return bigramModel
    ###################################################

    def nextWordBigram(firstWord,bigramModel):
        secWords = bigramModel[firstWord]
        return Counter(secWords).most_common(1)

    ######   Tigram  #########

    def buildTigramModel(corpus):
        TigramModel = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))
        for sentence in corpus:
            sentence = sentence.split()
            for i in range(len(sentence) - 2):
                key = sentence[i]+" "+sentence[i + 1]
                TigramModel[key][sentence[i + 2]] += 1
        for sentence in TigramModel:
            totalSecWords = float(sum(TigramModel[sentence].values()))
            for secWord in TigramModel[sentence]:
                TigramModel[sentence][secWord] /= totalSecWords

        return TigramModel
    ###################################################

    def nextWordTigram(sentence,TigramModel):
        sentence = TigramModel[sentence]
        return Counter(sentence).most_common(1)

    ###################### GUI ##########################
    bigramModel = buildBigramModel(corpus)
    tigramModel = buildTigramModel(corpus)
    root = tk.Tk()

    user_input = tk.StringVar(root)
    answer = 3


    def verify():
        sentence = str(user_input.get())
        sentenceLen = len(sentence.split())
        if(sentenceLen== 1):
            secWord=nextWordBigram(sentence,bigramModel)
            print(secWord)
        elif(sentenceLen== 2):
            thirdWord = nextWordTigram(sentence, tigramModel)
            print(thirdWord)

    entry = tk.Entry(root, textvariable=user_input)
    entry.pack()
    check = tk.Button(root, text='get next word', command=verify)
    check.pack()

    root.mainloop()


