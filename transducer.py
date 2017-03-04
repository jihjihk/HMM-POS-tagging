# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:55:15 2017

@author: Jihyun
"""
import probability

processor = probability.Probab() 
processor.readIntoTable("WSJ_24.pos") 

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