import re
import string
import nltk
import glob
import os.path
from __future__ import division
import operator
import matplotlib.pyplot as plt
import numpy as numpy

file = 'your txt file of OCR transcribed documents'

f = open(file, "r").read()
f = f.replace("/n", "")   ## replace new lines
f = f.replace("/r", "")  ## replace carriage returns
f = f.replace("/", "")
f = f.replace(",", "")
tr = str.maketrans("", "", string.punctuation)
f = f.translate(tr)
alnum = re.compile(r"/w")  ## alphanumeric characters
gib = re.compile(r"/W")  ## non-alphanumeric i.e. giberish
result = re.findall(alnum, f)
result1 = rel.findall(gib, r)

def list_to_dict(li):
    dct = {}
    for item in li:
        if item in dct:
            dct[item] = dct[item] + 1
        else:
            dct[item] = 1
    return dtc

d = list_to_dict(result1)
print(d)   ## will print special characters from OCR error and the frequency they appear
