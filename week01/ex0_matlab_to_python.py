"""
Week 1 · 练习 0：MATLAB / Mathematica → Python 对照
====================================================
为什么有这个文件：
    你的诊断 D = 0/6，但你不是编程新手——你用 MATLAB/Mathematica 做过计算。
    你缺的是 Python 的"说法"，不是编程能力。
    所以这一课不是"教你编程"，而是给你一本**对照词典** + 一套热身练习。

运行：python ex0_matlab_to_python.py
判分：文件末尾有自动检查，全绿就说明你跨过语言关了。
预计耗时：60–90 分钟。
"""

import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import numpy as np

print("=" * 70)
print(" 练习 0：MATLAB → Python 对照词典")
print("=" * 70)

# ======================================================================
# 对照表（先读一遍，后面做题时回来查）
# ======================================================================
CHEATSHEET = [
    ("注释",            "% 这是注释",              "# 这是注释"),
    ("打印",            "disp(x)",                 "print(x)"),
    ("幂运算",          "x^2",                     "x**2"),
    ("不等于",          "~=",                      "!="),
    ("逻辑与/或/非",     "&&  ||  ~",               "and  or  not"),
    ("索引起点",         "从 1 开始",               "从 0 开始  ← 最容易出错"),
    ("取最后一个",       "v(end)",                 "v[-1]"),
    ("区间 1 到 5",      "1:5  (含 5)",            "range(1,6) 或 np.arange(1,6)  ← 左闭右开"),
    ("长度",            "length(v)",               "len(v)"),
    ("形状",            "size(A)",                 "A.shape"),
    ("转置",            "A'",                      "A.T"),
    ("共轭转置",         "A'",                      "A.conj().T"),
    ("矩阵乘法",         "A * B",                   "A @ B   ← A*B 是逐元素相乘！"),
    ("逐元素相乘",       "A .* B",                  "A * B"),
    ("逐元素幂",         "A .^ 2",                  "A ** 2"),
    ("求逆",            "inv(A)",                  "np.linalg.inv(A)"),
    ("特征值",          "eig(A)",                  "np.linalg.eig(A)"),
    ("函数定义",         "function y = f(x)\\n  y = x^2;\\nend",  "def f(x):\\n    return x**2"),
    ("复数单位",         "1i  或  1j",              "1j"),
    ("求和",            "sum(v)",                  "np.sum(v) 或 v.sum()"),
    ("创建数组",         "[1 2 3]",                 "np.array([1, 2, 3])"),
    ("零矩阵",          "zeros(2,2)",              "np.zeros((2,2))"),
    ("单位矩阵",         "eye(2)",                  "np.eye(2)"),
    ("元素个数",         "numel(A)",                "A.size"),
]

print(f"\n{'概念':<12}{'MATLAB':<34}{'Python':<30}")
print("-" * 76)
for concept, matlab, python in CHEATSHEET:
    print(f"{concept:<12}{matlab:<34}{python:<30}")

print("\n【最重要的三个陷阱】")
print("  1. 索引从 0 开始：MATLAB 的 v(1) 在 Python 里是 v[0]")
print("  2. 矩阵乘法：MATLAB 的 A*B 在 Python 里是 A @ B；")
print("     Python 的 A*B 对应 MATLAB 的 A.*B（逐元素）")
print("  3. 区间是左闭右开：MATLAB 的 1:5 在 Python 里是 range(1,6)")


# ======================================================================
# Part 1 · 列表与索引
# ======================================================================
print("\n" + "=" * 70)
print(" Part 1：列表与索引（0-based 陷阱）")
print("=" * 70)

# TODO 1: 创建一个列表 a，内容为 [10, 20, 30, 40, 50]
#   然后取"第 3 个元素"（值是 30），存到变量 third
#   提示：MATLAB 里是 a(3)，Python 里是 a[?]
a = None          # <-- 换成你的代码
third = None      # <-- 换成你的代码

print(f"列表 a      = {a}")
print(f"第 3 个元素 = {third}   (期望 30)")


# ======================================================================
# Part 2 · numpy 数组
# ======================================================================
print("\n" + "=" * 70)
print(" Part 2：numpy 数组（Python 的'矩阵'）")
print("=" * 70)

# TODO 2: 创建 numpy 数组 v = [1, 2, 3, 4, 5]
#   并取它的 shape，存到变量 shape_v
v = None          # <-- 换成你的代码
shape_v = None    # <-- 换成你的代码

# TODO 3: 用切片取 v 的前三个元素，存到 first_three
#   提示：Python 切片是左闭右开，v[0:3] 或简写 v[:3]
first_three = None   # <-- 换成你的代码

print(f"v           = {v}")
print(f"v.shape     = {shape_v}   (期望 (5,))")
print(f"v 前三个    = {first_three}   (期望 [1 2 3])")


# ======================================================================
# Part 3 · 循环（顺便验证 numpy 的向量化）
# ======================================================================
print("\n" + "=" * 70)
print(" Part 3：循环 与 向量化")
print("=" * 70)

# TODO 4: 用 for 循环计算 1 到 10 的和，存到 total_loop
#   提示：for i in range(1, 11):
#             total_loop += i
total_loop = 0
# <-- 在这里写你的循环

# 对照：numpy 一行搞定（这就是"向量化"）
total_vectorized = np.sum(np.arange(1, 11))

print(f"循环求和     = {total_loop}   (期望 55)")
print(f"向量化求和   = {total_vectorized}   (期望 55)")
print("→ 两者结果相同，但数据量大时向量化快几十到几百倍。")


# ======================================================================
# Part 4 · 函数
# ======================================================================
print("\n" + "=" * 70)
print(" Part 4：函数定义")
print("=" * 70)

# TODO 5: 定义函数 square_plus_one(x)，返回 x**2 + 1
#   要求：既能在标量上工作，也能直接在 numpy 数组上工作
#   MATLAB 写法： function y = square_plus_one(x);  y = x^2 + 1;  end
def square_plus_one(x):
    # <-- 在这里写你的代码
    pass

print(f"f(3)        = {square_plus_one(3)}   (期望 10)")
print(f"f([1,2,3])  = {square_plus_one(np.array([1, 2, 3]))}   (期望 [2 5 10])")


# ======================================================================
# Part 5 · 矩阵运算（最重要的陷阱）
# ======================================================================
print("\n" + "=" * 70)
print(" Part 5：矩阵乘法 vs 逐元素相乘（最容易出错的地方）")
print("=" * 70)

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# TODO 6a: 逐元素相乘（对应 MATLAB 的 A .* B），存到 elementwise
elementwise = None   # <-- 换成你的代码

# TODO 6b: 矩阵乘法（对应 MATLAB 的 A * B），存到 matmul
#   提示：用 @ 运算符
matmul = None        # <-- 换成你的代码

print(f"A = \n{A}")
print(f"B = \n{B}")
print(f"\nA * B  (逐元素，对应 MATLAB .*) = \n{elementwise}")
print(f"  期望 [[ 5 12] [21 32]]")
print(f"\nA @ B  (矩阵乘法，对应 MATLAB *) = \n{matmul}")
print(f"  期望 [[19 22] [43 50]]")


# ======================================================================
# Part 6 · 复数与共轭转置（量子态的雏形）
# ======================================================================
print("\n" + "=" * 70)
print(" Part 6：复数与共轭转置（之后量子门要用）")
print("=" * 70)

print(f"1j ** 2        = {1j ** 2}        (期望 (-1+0j))")
print(f"np.exp(1j*pi)  = {np.exp(1j * np.pi)}   (期望 -1，欧拉恒等式)")

M = np.array([[1, 1j],
              [0, 2]], dtype=complex)

# TODO 7: 计算 M 的共轭转置（MATLAB 的 M'），存到 M_dagger
#   提示：先 .conj() 再 .T
M_dagger = None   # <-- 换成你的代码

print(f"\nM = \n{M}")
print(f"M 的共轭转置 = \n{M_dagger}")
print("  期望 [[1, 0], [-1j, 2]]")
print("→ 这个操作叫 'dagger'，在量子力学里到处都是（U†U = I）。")


# ======================================================================
# 自动检查（不用改）
# ======================================================================
print("\n" + "=" * 70)
print(" 自动检查")
print("=" * 70)

checks = []

def check(name, condition):
    try:
        checks.append((name, bool(condition)))
    except Exception:
        checks.append((name, False))

check("TODO 1  列表 a 正确", a == [10, 20, 30, 40, 50])
check("TODO 1  third = 30（注意 0-based）", third == 30)
check("TODO 2  v 是 numpy 数组且值正确",
      v is not None and isinstance(v, np.ndarray) and np.array_equal(v, [1, 2, 3, 4, 5]))
check("TODO 2  shape_v = (5,)", shape_v == (5,))
check("TODO 3  first_three = [1,2,3]",
      first_three is not None and np.array_equal(first_three, [1, 2, 3]))
check("TODO 4  total_loop = 55", total_loop == 55)
check("TODO 5  f(3) = 10", square_plus_one(3) == 10)
check("TODO 5  f 能作用于数组",
      np.array_equal(square_plus_one(np.array([1, 2, 3])), [2, 5, 10]))
check("TODO 6a 逐元素相乘正确",
      elementwise is not None and np.array_equal(elementwise, [[5, 12], [21, 32]]))
check("TODO 6b 矩阵乘法正确",
      matmul is not None and np.array_equal(matmul, [[19, 22], [43, 50]]))
check("TODO 7  共轭转置正确",
      M_dagger is not None and np.allclose(M_dagger, [[1, 0], [-1j, 2]]))

passed = sum(1 for _, ok in checks if ok)
for name, ok in checks:
    print(f"  {'[OK]  ' if ok else '[TODO]'} {name}")

print(f"\n通过 {passed} / {len(checks)}")

if passed == len(checks):
    print("\n全部通过。你已经跨过 MATLAB → Python 的语言关了。")
    print("接下来做 ex1（复数与态矢），那才是量子信息的开始。")
elif passed >= len(checks) - 3:
    print("\n很接近了。把剩下的 TODO 补完。")
else:
    print("\n还有不少没完成。别急——这一课的目的就是踩坑。")
    print("哪个 TODO 卡住了，把报错原文发我。")
