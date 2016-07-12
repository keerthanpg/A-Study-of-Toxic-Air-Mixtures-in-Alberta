import numpy as np

mesh = np.load("Mesh33.npy")

for j in range(mesh.shape[1]):
  for k in range (mesh.shape[2]):
    mesh[7][j][k]+=mesh[1][j][k]
    mesh[7][j][k]+=mesh[2][j][k]
    mesh[7][j][k]+=mesh[3][j][k]
    mesh[7][j][k]+=mesh[4][j][k]
    mesh[7][j][k]+=mesh[5][j][k]
    mesh[7][j][k]+=mesh[6][j][k]
    mesh[7][j][k]+=mesh[0][j][k]
    mesh[7][j][k]/=7

np.save("Mesh33", data)
