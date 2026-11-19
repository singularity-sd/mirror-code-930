"""Build the [[930,5]] weight-6 mirror stabilizer code on Z_930 and check it (numpy only).

Generator i (i in Z_930): X on qubits i + A, Z on qubits -i - B (mod 930); a qubit in both carries Y.
A = {20, 379, 473}, B = {79, 316, 355}.  Mirror family of Khesin and Lu (arXiv:2603.05496)."""
import json
import numpy as np

N = 930
A = [20, 379, 473]
B = [79, 316, 355]


def stabilizer_matrix():
    i = np.arange(N)
    Sx = np.zeros((N, N), dtype=np.uint8)
    Sz = np.zeros((N, N), dtype=np.uint8)
    for a in A:
        Sx[i, (i + a) % N] ^= 1
    for b in B:
        Sz[i, (-i - b) % N] ^= 1
    return Sx, Sz


def gf2_rank(M):
    M = M.copy() % 2
    r = 0
    for c in range(M.shape[1]):
        p = np.nonzero(M[r:, c])[0]
        if p.size == 0:
            continue
        p = r + p[0]
        M[[r, p]] = M[[p, r]]
        rows = np.nonzero(M[:, c])[0]
        M[rows[rows != r]] ^= M[r]
        r += 1
        if r == M.shape[0]:
            break
    return r


if __name__ == "__main__":
    Sx, Sz = stabilizer_matrix()
    comm = (Sx.astype(np.int64) @ Sz.T + Sz.astype(np.int64) @ Sx.T) % 2
    assert not comm.any(), "generators do not commute"
    S = np.hstack([Sx, Sz])
    k = N - gf2_rank(S)
    w = max(int(((Sx[r] | Sz[r]) > 0).sum()) for r in range(N))
    print(json.dumps({"n": N, "k": k, "max_pauli_weight": w}))
    np.savez_compressed("mirror_930_5.npz", s=S)
