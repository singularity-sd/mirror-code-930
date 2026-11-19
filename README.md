# Weight-6 mirror stabilizer code [[930, 5, ≤91]]

A non-CSS stabilizer code with Pauli weight 6 on 930 qubits, from the mirror family of Khesin and Lu
(arXiv:2603.05496).

| | |
|---|---|
| group | Z_930 |
| generator i | X on i + {20, 379, 473}, Z on −i − {79, 316, 355} (mod 930); a qubit in both carries Y |
| n, k | 930, 5 |
| Pauli weight | 6 |
| distance | ≤ 91 (explicit witness in `witness.json`) |

## Files

- `build_code.py`: rebuilds the stabilizer matrix with numpy only, checks commutation, k and the weight, and writes
  `mirror_930_5.npz` (key `s`, the binary symplectic matrix (X | Z)).
- `witness.json`: a logical operator (X, Y and Z supports) of Pauli weight 91.
- `verify_witness.py`: checks with numpy only that the witness commutes with every generator, lies outside the
  stabilizer group and has Pauli weight 91, so the distance is at most 91.

```
python build_code.py
python verify_witness.py
```

## How it was found

By a search over cyclic and two-dimensional mirror codes near the 1000-qubit limit, with distance upper bounds from
information-set searches scored by Pauli weight. The best candidates were re-measured at matched depth against the
best known weight-6 non-CSS code, [[693,6,64]]. On the same measure this code scores kd²/n = 53.8 against 42.4.
A longer witness search then found the logical operator of Pauli weight 91 in `witness.json`, which gives
kd²/n ≤ 5·91²/930 = 44.5 against 35.5 for [[693,6,64]].

Singularity, 2026.
