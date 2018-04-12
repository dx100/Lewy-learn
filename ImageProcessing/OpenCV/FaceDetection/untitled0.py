#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 20:28:59 2018

@author: dx100
"""

RMB2STL = 0.11254825

Total = 400000

STL = RMB2STL * Total

EX2 = 1.0/8.98732

STL2 = Total * EX2

Loss = STL2 - STL

print("Loss = {}".format(Loss))

Stage1
