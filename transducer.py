# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:55:15 2017

@author: Jihyun
"""
import probability
import pandas as pd

processor = probability.Probab() 
processor.readIntoTable("WSJ_24.pos")

def unique_pos_tags(file):
    pos= []
    with open(file, "r") as work:
        for line in work:
            element = line.strip().split('\t')
            if element[0][:-1] not in pos:
                pos.append(element[0][:-1])
    work.close()
    return pos

pos_list = unique_pos_tags('workfile.txt')

def viterbi(testfile, processor):
    with open(testfile, "r") as test:
        mat = pd.DataFrame(index=pos_list)
            for line in test:
                if line is "":
                    mat = mat.drop(mat[0:], axis=1)
                else:
                    

viterbi('WSJ_24.words', processor)

outputfile = open('workfile.txt', 'w')
for tag in processor.words:
    for word in processor.words[tag]:
        outputfile.write(tag + ':\t' + word + '\t\t' + str(processor.words[tag][word]) + '\n')
outputfile.write(tag + ':' + word + '\n')
outputfile.close()

"""
Use processor.getProb(<prev-state>, <current-state>, <word>) to get: 
    the probability of transition from prev to current state
    times
    the probability of current state's manifestation as the word 
    IF word is new to the dictionary, special rules determine its probability
"""
print(processor.getProb('NNS', 'NN', 'getuling'))