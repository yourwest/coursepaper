# -*- coding: utf-8 -*-
__author__ = 'angelinaprisyazhnaya'

import codecs, json, re, difflib


def distance(a, b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n

    current_row = range(n+1)
    for i in range(1, m+1):
        previous_row, current_row = current_row, [i]+[0]*n
        for j in range(1, n+1):
            add, delete, change = previous_row[j]+1, current_row[j-1]+1, previous_row[j-1]
            if a[j-1] != b[i-1]:
                change += 1
            current_row[j] = min(add, delete, change)
    try:
        value = current_row[n] / float(len(a)) * 100
    except:
        value = 100

    return value


text1 = codecs.open(u'1.txt', 'r', 'utf-8')
text2 = codecs.open(u'2.txt', 'r', 'utf-8')

changes = {}
k = 0
i = 0
insertion = u''
deletion = u''

sentences1 = re.split(u'\.|!|\?', text1.read())
sentences2 = re.split(u'\.|!|\?', text2.read())

#sentences1 = text1.read().replace(u'!', u'.').replace(u'?', u'.').split(u'.')
#sentences2 = text2.read().replace(u'!', u'.').replace(u'?', u'.').split(u'.')

while i < len(sentences1):

    #if distance(sentences1[i], sentences2[k]) >= 50:

    for l in sentences2:
        if distance(sentences1[i], l) <= 50:
            changes[i] = [sentences1[i], sentences2.index(l)]

            words1 = sentences1[i].split()
            words2 = l.split()

            for word in words1:
                if word not in words2:
                    changes[word] = [u'удаление']

            for word in words2:
                if word not in words1:
                    changes[word] = [u'вставка']

            break
        else:
            changes[i] = [u'удаление', sentences1[i]]
    i += 1

while k < len(sentences2):
    existence = False
    for l in sentences1:
        if distance(sentences2[k], l) <= 50:
            existence = True

    if existence is False:
        changes[str(k) + u'вставка'] = [sentences2[k], k]
    k += 1

changesJson = json.dumps(changes, ensure_ascii=False, indent=2)
diff = codecs.open(u'diff.json', 'w', 'utf-8')


diff.write(changesJson)

text1.close()
text2.close()
diff.close()

