import numpy.linalg as LA
import numpy as np
from dbg_print import dbg_print
import torch

def isFiniteValued(A):
    """ 
    isFiniteValued:
      Checks whether A only has finite values (no nans/infs).
    """

    #  Using norm(A,1) is much quicker than using any of:
    #    any(), isinf(), isnan(), A(:)
    # tf = np.isnumeric() and np.isfinite(LA.norm(A,1))

    tf =  torch.isfinite(torch.norm(A,1)).item()
    dbg_print("private.isFiniteValued : Skip isnumeric for now")

    return tf