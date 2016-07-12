import numpy as np
import rpy2.robjects.numpy2ri
import rpy2.robjects as ro
rpy2.robjects.numpy2ri.activate()
data = np.load("mesh.npy")

na, nb, nc, nd = data.shape
Br = ro.r.matrix(data, na, nb, nc, nd)

ro.r.assign("B", Br)