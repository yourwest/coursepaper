# -*- coding: utf-8 -*-
__author__ = 'angelinaprisyazhnaya'

import codecs, re

def get_words(text):
    words = []
    stopSymbols = u'.,!?:;-\n\r()'

    for token in text.read().strip(stopSymbols):
        words.append(token)

    return words


def get_shingles(words, shingleSize):

    wordsNumber = len(words)
    shingles = []

    if wordsNumber < shingleSize:
        return words

    for i in range(0, wordsNumber - shingleSize + 1):
        shingle = u''
        for j in range(i, i + shingleSize):
            shingle += u' ' + words[j]
        shingles.append(shingle)

    return shingles


def genshingle(shingles):
    import binascii
    out = []
    for i in shingles:
        out.append(binascii.crc32(' '.join(i).encode('utf-8')))

    return out

def compaire (source1, source2):
    same = 0
    for i in range(len(source1)):
        if source1[i] in source2:
            same += 1

    return same*2/float(len(source1) + len(source2))*100

def main():
    text1 = codecs.open(u'2.txt', 'r', 'utf-8')
    text2 = codecs.open(u'3.txt', 'r', 'utf-8')

    cmp1 = genshingle(get_shingles(get_words(text1), 10))
    cmp2 = genshingle(get_shingles(get_words(text2), 10))

    print compaire(cmp1, cmp2)

main()
