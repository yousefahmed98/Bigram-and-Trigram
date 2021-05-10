import collections
from collections import Counter
import pandas as pd
if __name__ == '__main__':
    df = pd.read_csv("poems.csv")
    poems = df.poem_text
    corpus = [sentence for sentence in list(poems) if isinstance(sentence, str)]
    print(corpus)
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


    bigramModel = buildBigramModel(corpus)
    tigramModel = buildTigramModel(corpus)
    secWord =nextWordBigram('هو', bigramModel)[0][0]
    print(secWord)
    print(nextWordTigram('هو'+ " " + secWord , tigramModel)[0][0])