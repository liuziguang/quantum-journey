"""
Week 1 · 练习 1 参考解（做完再看！）
====================================
先自己做完 ex1，卡住或做完后再对照这个文件。

运行：python ex1_solution.py
"""

import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import numpy as np

ket0 = np.array([1, 0], dtype=complex)
ket1 = np.array([0, 1], dtype=complex)

# ---- TODO 1 ----
ket_plus = (ket0 + ket1) / np.sqrt(2)

# ---- TODO 2 ----
# np.vdot(a, b) 会先对 a 取共轭，所以它就是 <a|b>
inner_0_plus = np.vdot(ket0, ket_plus)

# ---- TODO 3 ----
norm_plus_sq = np.vdot(ket_plus, ket_plus)

# ---- TODO 4 ----
# 注意用 bool() 包一层：np.isclose 返回的是 numpy.bool_，
# 直接和 True 比较（is True）会失败。
are_orthogonal = bool(np.isclose(np.vdot(ket0, ket1), 0.0))

# ---- TODO 5 ----
ket01 = np.kron(ket0, ket1)

# ---- TODO 6 ----
ket_plus_plus = np.kron(ket_plus, ket_plus)

# ---- TODO 7 ----
norm_pp = np.vdot(ket_plus_plus, ket_plus_plus)

# ---- TODO 8 的参考答案 ----
# |+> 和 |-> 的差别只在相对相位：
#   |+> = (|0>+|1>)/sqrt2      |-> = (|0>-|1>)/sqrt2
# 在计算基 {|0>,|1>} 下测量，两者的概率分布完全相同（各 50%），
# 因此单看测量结果无法区分它们——这是"相位不可直接观测"的体现。
# 但这个相位是物理上真实存在的：在 X 基下测量，|+> 是 +1 本征态、
# |-> 是 -1 本征态，可以干净地区分。所以相位可以通过"换基测量"
# 或者在干涉/后续门操作中被观测到。这就是量子计算里相位门的价值。

print("=" * 62)
print(" 练习 1 参考解")
print("=" * 62)
print(f"|+>            = {ket_plus}")
print(f"<0|+>          = {inner_0_plus}")
print(f"<+|+>          = {norm_plus_sq}")
print(f"<0|1> 正交?    = {are_orthogonal}")
print(f"|01>           = {ket01}")
print(f"|+>⊗|+>        = {ket_plus_plus}")
print(f"<++|++>        = {norm_pp}")

assert np.allclose(ket_plus, [1 / np.sqrt(2)] * 2), "TODO 1"
assert np.isclose(inner_0_plus, 1 / np.sqrt(2)), "TODO 2"
assert np.isclose(norm_plus_sq, 1.0), "TODO 3"
assert are_orthogonal is True, "TODO 4"
assert np.allclose(ket01, [0, 1, 0, 0]), "TODO 5"
assert np.allclose(ket_plus_plus, [0.5] * 4), "TODO 6"
assert np.isclose(norm_pp, 1.0), "TODO 7"

print("\n[OK] 参考解全部通过 —— 说明练习里的期望值是正确的。")
