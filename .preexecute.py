import os
import random
import math
from uuid import uuid4
from hashlib import sha256

import numpy as np
from sympy import *
from sympy.plotting import *
import matplotlib.pyplot as plt
from matplotlib import cm

from calcly import Calcly, Constant


def split_by_list(txt, seps):
    # https://stackoverflow.com/questions/4697006/python-sp
    lit-string-by-list-of-separators
    default_sep = seps[0]
    for sep in seps[1:]:
    	txt = txt.replace(sep, default_sep)
    #return [i.strip() for i in txt.split(default_sep)]
    return [i for i in txt.split(default_sep)]

def sha(in_str):
	print('hashed with sha256')
	return sha256(in_str.encode('utf-8')).hexdigest()


a, b, c, d, e, f = symbols('a b c d e f')
g, h, i, j, k, l = symbols('g h i j k l')
m, n, o, p, q, r = symbols('m n o p q r')
s, t, u, v, w = symbols('s t u v w')
x, y, z = symbols('x y z')
# init_printing(use_unicode=True)

def contour(f, fill=True, 
	  xlim=(-10, 10), ylim=(-10, 10), 
	  acc=1000, cmap="inferno", **kwargs):
	# fig = plt.figure()
	# ax = fig.add_subplot(111)
	xl = np.linspace(xlim[0],xlim[1],acc)
	yl = np.linspace(ylim[0],ylim[1],acc)
	x, y = np.meshgrid(xl, yl)
	z = f(x, y)
	# ax.contourf(x,y,z)
	fig, ax = plt.subplots()
	if fill:
		plt.contourf(x,y,z, cmap=cmap, **kwargs)
	else:
		plt.contour(x,y,z, cmap=cmap, **kwargs)
	plt.colorbar()
	plt.show()

# plt.style.use('ggplot')
# plt.style.use('dark_background')
# plt.rcParams['figure.figsize'] = 15, 10
# plt.rcParams['legend.fontsize'] = 10

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

def start(font="random"):
	if font=="random":
		print(random.choice(list(Calcly.fonts.values())))
	else:
		print(Calcly.fonts[font])

def clear():
	"""
	clear function with start print
	to clear completely use ctrl+L
	"""
	os.system('clear')
	#os.system('cls' if os.name == 'nt' else 'clear')
	start()

start()
