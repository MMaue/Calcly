import random
import math
from uuid import uuid4

import numpy as np
from sympy import *
from sympy.plotting import *
#import matplotlib.pyplot as plt

from calcly import Calcly, Constant


def split_by_list(txt, seps):
    # https://stackoverflow.com/questions/4697006/python-sp
    lit-string-by-list-of-separators
    default_sep = seps[0]
    for sep in seps[1:]:
    	txt = txt.replace(sep, default_sep)
    #return [i.strip() for i in txt.split(default_sep)]
    return [i for i in txt.split(default_sep)]


a, b, c, d, e, f = symbols('a b c d e f')
g, h, i, j, k, l = symbols('g h i j k l')
m, n, o, p, q, r = symbols('m n o p q r')
s, t, u, v, w = symbols('s t u v w')
x, y, z = symbols('x y z')
# init_printing(use_unicode=True)

# plt.style.use('ggplot')
# plt.style.use('dark_background')

# Load Constants
const_txt = ""
for key, value in Calcly.const.items():
	exec(f"{key}={value}")
	const_txt += value.__repr__() + '\n'

def const():
	print(const_txt)

# dir()
# globals()
# locals()
# to clear use ctrl+L

def start(font="random"):
	if font=="random":
		print(random.choice(list(Calcly.fonts.values())))
	else:
		print(Calcly.fonts[font])

start()
