#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:08:48 2018

Different from Sendex, where he models different better with different dice, 
I uses the same dice for all the betters.
@author: dx100
"""
import random
import matplotlib
import matplotlib.pyplot as plt
#
import time
import numpy as np

results = np.empty((0, 3), dtype=float64)
alphas = np.array([1, 1.5, 2], dtype=float64)


def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
        return True
    
    
def doubler_bettor(funds,initial_wager,dx_ratio, wager_count):
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1

    # since we'll be betting based on previous bet outcome #
    previousWagers_win = np.array([True, True, True], dtype=bool)

    # since we'll be doubling #
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        ttt = np.empty((0, 3), dtype=float64)
        
        # for each better
        for i, alpha in enumarate(alphas):
            if previousWagers_win[i] : #Win
            if rollDice():
                value += wager
                print value
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager  
                previousWager = 'loss'
                print value
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    print 'went broke after',currentWager,'bets'
                    currentWager += wager_count # stop the loop by making currentWager > wager_count
        elif previousWager == 'loss':
            print 'we lost the last one, so we will be super smart & double up!'
            if rollDice():
                wager = previousWagerAmount * dx_ratio
                print 'we won',wager
                value += wager
                print value
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * dx_ratio
                print 'we lost',wager
                value -= wager
                if value < 0:
                    print 'went broke after',currentWager,'bets'
                    currentWager += wager_count
                print value
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    print 'went broke after',currentWager,'bets'
                    currentWager += wager_count

        currentWager += 1

    print value
    plt.plot(wX,vY)
