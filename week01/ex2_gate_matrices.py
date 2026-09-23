"""
Week 1 · 练习 2：量子门就是矩阵
================================
目的：把"物理系的算符/哈密顿量"翻译成"量子信息的门矩阵"，
      并亲手验证酉性、厄米性、自逆性、对易关系。

运行：python ex2_gate_matrices.py

对你（理论物理背景）的特别说明：
  你熟悉的"厄米算符 = 可观测量"、"时间演化算符是幺正的"，
  在这里就是 "Hermitian 矩阵" 和 "Unitary 矩阵"。
  这一节是纯翻译，你应该会觉得很快。
"""

import sys

# Windows 控制台兼容：强制 UTF-8 输出，避免 GBK 编码报错
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import numpy as np

print("=" * 62)
print(" 练习 2：量子门矩阵")
print("=" * 62)

# ======================================================================
# Part A · 单量子比特门（示范，读懂即可）
# ======================================================================
# 物理语言：算符 / 矩阵                 ->  量子信息：门（Gate）
# 物理语言：时间演化 e^{-iHt/hbar}      ->  量子信息：酉变换 U
print("\n--- Part A：六个基本门 ---")

I2 = np.eye(2, dtype=complex)

X = np.array([[0, 1],
              [1, 0]], dtype=complex)          # 比特翻转（泡利 sigma_x）

Y = np.array([[0, -1j],
              [1j, 0]], dtype=complex)         # 泡利 sigma_y

Z = np.array([[1, 0],
              [0, -1]], dtype=complex)         # 相位翻转（泡利 sigma_z）

H = np.array([[1, 1],
              [1, -1]], dtype=complex) / np.sqrt(2)   # Hadamard，产生叠加

S = np.array([[1, 0],
              [0, 1j]], dtype=complex)         # 相位门

T = np.array([[1, 0],
              [0, np.exp(1j * np.pi / 4)]], dtype=complex)  # pi/8 门

for name, gate in [("I", I2), ("X", X), ("Y", Y), ("Z", Z), ("H", H), ("S", S), ("T", T)]:
    print(f"\n{name} =\n{gate}")

# 态矢
ket0 = np.array([1, 0], dtype=complex)
ket1 = np.array([0, 1], dtype=complex)


# ======================================================================
# Part B · 判断酉性与厄米性（你来写）
# ======================================================================
print("\n--- Part B：酉性与厄米性 ---")

def is_unitary(matrix, tol=1e-10):
    """
    判断矩阵是否酉：U† U = I，其中 † 表示共轭转置。
    提示：
      - 共轭转置用 matrix.conj().T
      - 矩阵乘法用 @ 运算符
      - 容差比较用 np.allclose(A, B, atol=tol)
    返回 True / False
    """
    # TODO 1: 实现这个函数
    pass


def is_hermitian(matrix, tol=1e-10):
    """
    判断矩阵是否厄米：M† = M（也就是"可观测量"）。
    提示：与上面类似，但这次比较高阶共轭转置与原矩阵本身。
    返回 True / False
    """
    # TODO 2: 实现这个函数
    pass


# 所有量子门都必须是酉的（因为量子演化必须保持内积/概率守恒）
# 只有"可观测量"才必须是厄米的（X, Y, Z 既是酉的、又是厄米的）
print(f"\n{'门':<4}{'酉性 Unitary':<18}{'厄米 Hermitian':<18}")
print("-" * 40)
for name, gate in [("I", I2), ("X", X), ("Y", Y), ("Z", Z), ("H", H), ("S", S), ("T", T)]:
    print(f"{name:<4}{str(is_unitary(gate)):<18}{str(is_hermitian(gate)):<18}")

print("\n思考：为什么 S 和 T 是酉的但不是厄米的？")
print("      为什么 X / Y / Z 既是酉的又是厄米的？")


# ======================================================================
# Part C · 门作用在态上（你来写）
# ======================================================================
print("\n--- Part C：门作用于态 ---")

# TODO 3: 计算 H 作用于 |0>，即 H|0>
#   提示：矩阵乘向量用 @
#   期望结果：(|0> + |1>)/sqrt(2)，即 [0.7071, 0.7071]
H_on_ket0 = None  # <-- 换成你的代码

# TODO 4: 计算 X 作用于 |0>，期望 |1> = [0, 1]
X_on_ket0 = None  # <-- 换成你的代码

# TODO 5: 计算 H 作用于 H|0>，也就是 H(H|0>)
#   期望结果回到 |0> —— 这说明 H 是"自逆"的（H² = I）
H_twice_on_ket0 = None  # <-- 换成你的代码

print(f"H|0>   = {H_on_ket0}   (期望 ≈ [0.7071, 0.7071])")
print(f"X|0>   = {X_on_ket0}   (期望 = [0, 1])")
print(f"HH|0>  = {H_twice_on_ket0}   (期望回到 [1, 0])")


# ======================================================================
# Part D · 对易关系（你的物理主场）
# ======================================================================
# 物理语言：[sigma_x, sigma_y] = 2i sigma_z
# 这在量子信息里同样是量子比特控制的代数基础。
print("\n--- Part D：对易关系 ---")

# TODO 6: 计算对易子 [X, Y] = XY - YX
#   提示：X @ Y - Y @ X
commutator_XY = None  # <-- 换成你的代码

# TODO 7: 计算 2j * Z，用来和对易子比较
expected = None  # <-- 换成你的代码

print(f"[X, Y]  = \n{commutator_XY}")
print(f"2i·Z    = \n{expected}")
print("两者应该相同。")


# ======================================================================
# Part E · 两个"反直觉"验证（选做，但强烈建议）
# ======================================================================
print("\n--- Part E：两个反直觉验证（选做）---")

# TODO 8（选做）: 验证 H 是自逆的，即 H @ H ≈ I2
#   把结果存成布尔值
H_is_self_inverse = None  # <-- 换成你的代码

# TODO 9（选做）: 验证 S @ S ≈ Z
#   （因为 S 是相位门的平方根，S² = Z）
S_squared_is_Z = None  # <-- 换成你的代码

print(f"H @ H == I ? {H_is_self_inverse}")
print(f"S @ S == Z ? {S_squared_is_Z}")


# ======================================================================
# 自动检查（不用改）
# ======================================================================
print("\n" + "=" * 62)
print(" 自动检查")
print("=" * 62)

checks = []

def _as_bool(value):
    """把 numpy 的 bool_ / None 统一成 Python 的 True/False。

    为什么需要它：如果你写 np.isclose(...)，返回的是 numpy.bool_，
    而 `np.bool_(True) is True` 在 Python 里是 False，会误判成答错。
    """
    try:
        return bool(value)
    except Exception:
        return False

def check(name, condition):
    try:
        checks.append((name, bool(condition)))
    except Exception:
        checks.append((name, False))

check("TODO 1 is_unitary 实现正确",
      _as_bool(is_unitary(X))
      and not _as_bool(is_unitary(np.array([[1, 1], [0, 1]], dtype=complex))))
check("TODO 2 is_hermitian 实现正确",
      _as_bool(is_hermitian(X)) and not _as_bool(is_hermitian(S)))
check("TODO 3 H|0> ≈ [0.7071, 0.7071]",
      H_on_ket0 is not None and np.allclose(H_on_ket0, [1/np.sqrt(2), 1/np.sqrt(2)]))
check("TODO 4 X|0> = [0, 1]",
      X_on_ket0 is not None and np.allclose(X_on_ket0, [0, 1]))
check("TODO 5 HH|0> 回到 [1, 0]",
      H_twice_on_ket0 is not None and np.allclose(H_twice_on_ket0, [1, 0]))
check("TODO 6 [X,Y] ≈ 2i·Z",
      commutator_XY is not None and np.allclose(commutator_XY, 2j * Z))
check("TODO 7 2i·Z 正确",
      expected is not None and np.allclose(expected, 2j * Z))
check("TODO 8（选做）H 自逆",
      _as_bool(H_is_self_inverse))
check("TODO 9（选做）S² = Z",
      _as_bool(S_squared_is_Z))

passed = sum(1 for _, ok in checks if ok)
for name, ok in checks:
    print(f"  {'[OK]  ' if ok else '[TODO]'} {name}")

print(f"\n通过 {passed} / {len(checks)}")

if passed == len(checks):
    print("\n全部通过。你已经能用 numpy 操作量子门了。")
    print("这是 Week 1 的第二个产物，记得 git commit。")
else:
    print("\n还有 TODO 没完成（选做的两个可以先跳过，但建议做）。")
    print("卡住了就把报错发给我。")
