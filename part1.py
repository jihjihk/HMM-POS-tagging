# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 20:10:02 2017

@author: Gabor
"""

#import re
#import argparse
#Parsing the input/output file name arguments from the terminal
#parser = argparse.ArgumentParser()
#parser.add_argument("input", help="name of input file without .txt")
#parser.add_argument("output", help="name of output file without .txt")
#args = parser.parse_args()
#if (args.output == None or args.input == None):
#    print "incorrect arguments. Type python program_dollars.py <name of input file without .txt> <name of output file without .txt>"
#    exit();

words = {}
transitions = {}
prevPOS = 'Start'
class Probab():
    def __init__(self):
        self.words = {}
        self.transitions = {}
        self.prevPOS = 'Start'
    
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
    
    def calcProb(self):
        self.loopProb(self.words)
        self.loopProb(self.transitions)
    def loopProb(self, dict):
        for outer_key in dict:
            total = 0
            for key in dict[outer_key]:
                total += dict[outer_key][key]
            for key in dict[outer_key]:
                dict[outer_key][key] = dict[outer_key][key]/total
        
        
processor = Probab()       
        
#outputfile = open('workfile.txt', 'w')
#with open(args.input+".txt", "r") as inputfile:
with open("WSJ_24.pos", "r") as inputfile:
    for line in inputfile:
        element = line.strip().split('\t')
        if (element[0] == ''):
            continue
        processor.addElem(element)
        
processor.calcProb()       
        
        
#print(processor.transitions) 
#print(processor.words)    
   
#outputfile.close()
inputfile.close()
