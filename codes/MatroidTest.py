import numpy as np
from sage.all import *

A = Matrix([[1, 1, 0], [1, 0, 1], [0, 1, -1]])

M = Matroid([0, 1, 2, 3, 4, 5], A)

print(M.is_valid())


