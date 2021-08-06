from pygransoStruct import general_struct
import numpy as np
import numpy.linalg as la

class ci_gradStruct:
    class c1:
        pass

def combinedFunction(X,parameters):
    
    # input variable, matirx form. torch tensor
    q = X.q
    # q.requires_grad_(True)
    
    m = parameters.m
    Y = parameters.Y
    
    # objective function
    Ytq = Y.T @ q
    f = 1/m * la.norm(Ytq,  ord = 1)
    # f = 1/m * np.max(np.sum(np.abs(qtY)))
    
    f_grad = general_struct()
    f_grad.q = 1/m*Y@ np.sign(Ytq)

    # inequality constraint, matrix form
    ci = None
    ci_grad = None

    # equality constraint 
    ce = general_struct()
    ce.c1 = q.T @ q - 1

    ce_grad = ci_gradStruct()
    ce_grad.c1.q = 2*q

    return [f,f_grad,ci,ci_grad,ce,ce_grad]