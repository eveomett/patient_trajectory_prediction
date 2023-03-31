#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:34:00 2023

@author: erv2
"""

import time
import os



startTime = time.time()


os.system('./MIMIC_smart_splitter.py output.csv')

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))