# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 13:25:05 2025

@author: fergu
"""
import os
import matplotlib
import glob
import pandas as pd

files  = glob.glob('*.txt')
print(files)
colspecs = [(0, 10), (12, 21)]
for x in range(len(files)):
    name = str(os.path.splitext(str(files[x]))[0])
    df = pd.read_fwf(files[x], colspecs=colspecs, header=4, index_col=0)
    plot = df.plot(xlim=[4000,500],xlabel="Wavenumber cm^-1", ylabel="Intensity", title=name)

    plot.figure.savefig(name+" IRSPECTRA.png")