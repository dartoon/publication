#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 09:59:07 2021

@author: Dartoon
"""

import numpy as np
import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
import shutil
import glob
j = 1
for i in range(702, 761):
    file = glob.glob('sim_lens_AGN_{0}'.format(i))
    if file != []:
        shutil.move('sim_lens_AGN_{0}'.format(i), 'sim_lens_AGN_ID{0}'.format(j))
        shutil.move('sim_lens_transient_{0}'.format(i), 'sim_lens_transient_ID{0}'.format(j))
        j = j + 1