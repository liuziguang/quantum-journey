"""
Week 1 · 练习 2 参考解（做完再看！）
====================================
运行：python ex2_solution.py
"""

import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import numpy as np

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
S = np.array([[1, 0], [0, 1j]], dtype=complex)
T = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]], dtype=complex)

ket0 = np.array([1, 0], dtype=complex)


# ---- TODO 1 ----
def is_unitary(matrix, tol=1e-10):
    # 酉：U† U = I（† 就是共轭转置 .conj().T）
    return bool(np.allclose(matrix.conj().T @ matrix, np.eye(matrix.shape[0]), atol=tol))


# ---- TODO 2 ----
def is_hermitian(matrix, tol=1e-10):
    # 厄米：M† = M（可观测量）
    return bool(np.allclose(matrix.conj().T, matrix, atol=tol))


# ---- TODO 3 ----
H_on_ket0 = H @ ket0

# ---- TODO 4 ----
X_on_ket0 = X @ ket0

# ---- TODO 5 ----
H_twice_on_ket0 = H @ (H @ ket0)

# ---- TODO 6 ----
commutator_XY = X @ Y - Y @ X

# ---- TODO 7 ----
expected = 2j * Z

# ---- TODO 8 ----
H_is_self_inverse = bool(np.allclose(H @ H, I2))

# ---- TODO 9 ----
S_squared_is_Z = bool(np.allclose(S @ S, Z))

print("=" * 62)
print(" 练习 2 参考解")
print("=" * 62)
print(f"\n{'门':<4}{'酉性':<8}{'厄米':<8}")
print("-" * 22)
for name, gate in [("I", I2), ("X", X), ("Y", Y), ("Z", Z), ("H", H), ("S", S), ("T", T)]:
    print(f"{name:<4}{str(is_unitary(gate)):<8}{str(is_hermitian(gate)):<8}")

print(f"\nH|0>   = {H_on_ket0}")
print(f"X|0>   = {X_on_ket0}")
print(f"HH|0>  = {H_twice_on_ket0}")
print(f"\n[X,Y] =\n{commutator_XY}")
print(f"2i·Z  =\n{expected}")
print(f"\nH@H == I ? {H_is_self_inverse}")
print(f"S@S == Z ? {S_squared_is_Z}")

print("\n为什么 S 酉但不厄米？")
print("  酉性保证概率守恒（量子演化必须满足）；厄米性对应'可观测量'。")
print("  S = diag(1, i)，共轭转置是 diag(1, -i) ≠ S，所以不厄米，")
print("  但它满足 S†S = I，所以是合法的量子门。")
print("X/Y/Z 恰好既酉又厄米，因为它们同时是演化算符和可观测量（自逆且本征值为 ±1）。")

assert is_unitary(X) and is_unitary(Y) and is_unitary(Z), "X/Y/Z 应酉"
assert is_unitary(H) and is_unitary(S) and is_unitary(T), "H/S/T 应酉"
assert not is_unitary(np.array([[1, 1], [0, 1]], dtype=complex)), "非酉矩阵应判 False"
assert is_hermitian(X) and is_hermitian(Y) and is_hermitian(Z) and is_hermitian(H), "应厄米"
assert not is_hermitian(S), "S 不应厄米"
assert not is_hermitian(T), "T 不应厄米"
assert np.allclose(H_on_ket0, [1 / np.sqrt(2)] * 2), "TODO 3"
assert np.allclose(X_on_ket0, [0, 1]), "TODO 4"
assert np.allclose(H_twice_on_ket0, [1, 0]), "TODO 5"
assert np.allclose(commutator_XY, 2j * Z), "TODO 6"
assert np.allclose(expected, 2j * Z), "TODO 7"
assert H_is_self_inverse, "TODO 8"
assert S_squared_is_Z, "TODO 9"

print("\n[OK] 参考解全部通过 —— 说明练习里的期望值是正确的。")
