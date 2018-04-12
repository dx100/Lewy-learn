#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 12:29:24 2017

@author: dx100
"""

import torch
from torch.autograd import Variable

x = Variable(torch.ones(2,2), requires_grad = True)

y = x + 2

z = y * y * 3

out = z.mean()
