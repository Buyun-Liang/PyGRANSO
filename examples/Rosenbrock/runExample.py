import time
import numpy as np
import torch
import numpy.linalg as la
from scipy.stats import norm
import sys
## Adding PyGRANSO directories. Should be modified by user
sys.path.append(r'C:\Users\Buyun\Documents\GitHub\PyGRANSO')
from pygranso import pygranso
from pygransoStruct import Options, Parameters

# Please read the documentation on https://pygranso.readthedocs.io/en/latest/

# variables and corresponding dimensions.
var_in = {"x1": (1,1), "x2": (1,1)}

# user defined options
opts = Options()
opts.QPsolver = 'osqp'
opts.maxit = 100
opts.print_level = 1
opts.print_frequency = 1
opts.x0 = np.ones((2,1))

#  main algorithm  
start = time.time()
soln = pygranso(var_in, user_opts = opts)
end = time.time()
print("Total Wall Time: {}s".format(end - start))

print(soln.final.x)