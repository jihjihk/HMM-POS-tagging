# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:55:15 2017

@author: Jihyun
"""
import probability

processor = probability.Probab() 
processor.readIntoTable("WSJ_24.pos")       
processor.calcProb() 

print(processor.getTran('NNS'))
print(processor.getWord('NNS'))