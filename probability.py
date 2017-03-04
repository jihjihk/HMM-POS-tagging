# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 20:10:02 2017

@author: Gabor
"""
import re

class Probab():
    def __init__(self):
        self.words = {}
        self.transitions = {}
        self.prevPOS = 'Start'
        self.unknown = {}
        self.ing = {}
        self.ly = {}
        self.s_ending = {}
        self.er = {}
        self.hyphenated = {}
        self.numbers = {}
    
    def readIntoTable(self, file):
        with open(file, "r") as inputfile:
            for line in inputfile:
                element = line.strip().split('\t')
                if (element[0] == ''):
                    continue
                self.addElem(element)        
        inputfile.close()        
        self.preProcOOV()
        self.calcProb()        
        
    #adding an element to the dictionary to count its frequency
    def addElem(self, element):
        #counting words
        if (element[1] in self.words):
            if (element[0] in self.words[element[1]]):
               self.words[element[1]][element[0]] += 1
            else:
               self.words[element[1]][element[0]] = 1
        else:
           self.words[element[1]] = {element[0]: 1}
        
        #counting transitions
        if (self.prevPOS in self.transitions):
            if (element[1] in self.transitions[self.prevPOS]):
                self.transitions[self.prevPOS][element[1]] += 1
            else:
                self.transitions[self.prevPOS][element[1]] = 1
        else:
            self.transitions[self.prevPOS] = {element[1]: 1}
        
        self.prevPOS = element[1]
    
    #unique strategy to deal with OOV
    #words that only appear once get put into special categories
    def preProcOOV(self):        
        for tag in self.words:
            for word in self.words[tag]:
                if (self.words[tag][word] < 2):                 
                    if (word[-3:] == 'ing'):
                        self.addToDict(self.ing, tag)
                    elif (word[-1] == 's'):
                        self.addToDict(self.s_ending, tag)
                    elif (word[-2:] == 'ly'):
                        self.addToDict(self.ly, tag)
                    elif (word[-2:] == 'er'):
                        self.addToDict(self.er, tag)
                    elif (re.search('\d', word)):
                        self.addToDict(self.numbers, tag)
                    elif (re.search('-', word)):
                        self.addToDict(self.hyphenated, tag)
                    else:
                        self.addToDict(self.unknown, tag)             
    
    #converts all dictionaries to probability from frequency  
    def calcProb(self):       
        for dictionary in [self.words, self.transitions]: 
            for outer_key in dictionary:
                total = 0
                for key in dictionary[outer_key]:
                    total += dictionary[outer_key][key]
                for key in dictionary[outer_key]:
                    dictionary[outer_key][key] = dictionary[outer_key][key]/total
        for dictionary in [self.unknown, self.ing, self.ly, self.s_ending, self.er, self.hyphenated, self.numbers]:
            total = 0
            for tag in dictionary:
                total += dictionary[tag]
            for tag in dictionary:
                dictionary[tag] = dictionary[tag]/total
    
    #get probability function, if word is unknown, gets special treatment    
    def getProb(self, prevState, state, word):
        if (word in self.words[state]):
            word_prob = self.words[state][word]
        #out of vocab word
        elif (word[-3:] == 'ing'):
            if state in self.ing:
                word_prob = self.ing[state] 
        elif (word[-1] == 's'):
            if state in self.s_ending:
                word_prob == self.s_ending[state] 
        elif (word[-2:] == 'ly'):
            if state in self.ly:
                word_prob ==self.ly[state] 
        elif (word[-2:] == 'er'):
            if state in self.er:
                word_prob = self.er[state] 
        elif (re.search('\d', word)):
            if state in self.numbers:
                word_prob = self.numbers[state] 
        elif (re.search('-', word)):
            if state in self.hyphenated:
                word_prob = self.hyphenated[state] 
        elif (state in self.unknown):
            word_prob = self.unknown[state]
        else:
            word_prob = 0.000000000001
            
        return self.transitions[prevState][state] * word_prob
    
    #util function to add something to a dictionary
    def addToDict(self, dictionary, tag):
        if tag in dictionary:
            dictionary[tag] += 1
        else:
            dictionary[tag] = 1
        