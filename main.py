import collections
from collections import Counter
if __name__ == '__main__':
    corpus = [
        'I am yousef ahmed student at fcai',
        'sam i am',
        'i dont like green eggs and ham',
        'i am yousef ehab',
        'The web has become an indispensible resource with a vast amount of information available'
    ]

    def buildBigramModel(corpus):
        bigramModel = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))
        corpus = [word.lower() for word in corpus]
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
        corpus = [word.lower() for word in corpus]
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
    print(nextWordBigram('i', bigramModel)[0][0])
    secWord =nextWordBigram('i', bigramModel)[0][0]
    thword=nextWordTigram("i" + " " + secWord, tigramModel)
    print(nextWordTigram("i"+ " " + secWord , tigramModel)[0][0])