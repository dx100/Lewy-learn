#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:34:59 2017

@author: dx100
"""

import menpo3d

mesh = menpo3d.io.import_builtin_asset('james.obj')

mesh.view()
