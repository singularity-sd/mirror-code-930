"""Check the witness in witness.json: it commutes with every generator, lies outside the stabilizer group,
and has the stated Pauli weight (a Y counts once). numpy only."""
import json
import numpy as np
from build_code import stabilizer_matrix, gf2_rank, N

Sx, Sz = stabilizer_matrix()
w = json.load(open("witness.json"))
vx = np.zeros(N, dtype=np.int64)
vz = np.zeros(N, dtype=np.int64)
for q in w["X"]:
    vx[q] = 1
for q in w["Z"]:
    vz[q] = 1
for q in w["Y"]:
    vx[q] = 1
    vz[q] = 1
commutes = not ((Sx.astype(np.int64) @ vz + Sz.astype(np.int64) @ vx) % 2).any()
S = np.hstack([Sx, Sz])
v = np.concatenate([vx, vz]).astype(np.uint8)
outside = gf2_rank(np.vstack([S, v])) > gf2_rank(S)
weight = int(((vx | vz) > 0).sum())
print(json.dumps({"commutes_with_all_generators": bool(commutes), "outside_stabilizer_group": bool(outside),
                  "pauli_weight": weight}))
