#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 12:40:19 2017

@author: jihyunkim
"""

with open("workfile.txt", "r") as work:
    pos= []
    for line in work:
        element = line.strip().split('\t')
        if element[0][:-1] not in pos:
            pos.append(element[0][:-1])

pos.remove('NNS:financing')
print(pos)