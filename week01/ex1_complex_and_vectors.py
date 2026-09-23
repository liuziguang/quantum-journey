"""
Week 1 · 练习 1：复数、态矢与张量积
====================================
目的：把"物理系的波函数语言"翻译成"量子信息的态矢语言"。

运行：python ex1_complex_and_vectors.py
判分：脚本末尾有自动检查，全部通过会打印 "全部通过"。

怎么用：
  - Part A 是示范，读一遍即可，不用改
  - Part B / C / D 有 TODO，把代码补上
  - 补完后运行，看末尾的检查结果
"""

import sys

# Windows 控制台兼容：强制 UTF-8 输出，避免 GBK 编码报错
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import numpy as np

print("=" * 62)
print(" 练习 1：复数、态矢与张量积")
print("=" * 62)

# ======================================================================
# Part A · 复数（示范，不用改，读懂即可）
# ======================================================================
# 量子力学必须用复数，因为存在"相位"这种不可直接观测、但会影响干涉的量。
print("\n--- Part A：复数 ---")

z = 3 + 4j
print(f"z          = {z}")
print(f"|z|        = {abs(z)}          <- 模长（复数取绝对值）")
print(f"conj(z)    = {np.conj(z)}      <- 共轭")
print(f"z * conj(z)= {z * np.conj(z)}  <- 模的平方，一定是实数")

# 欧拉公式 e^{iθ} = cosθ + i·sinθ  —— 这是量子相位门的数学基础
theta = np.pi / 4
print(f"e^(i·pi/4) = {np.exp(1j * theta)}")
print(f"cos+isin   = {np.cos(theta) + 1j * np.sin(theta)}   <- 应该与上一行相同")
print(f"e^(i·pi)   = {np.exp(1j * np.pi)}   <- 应该是 -1（欧拉恒等式）")


# ======================================================================
# Part B · 态矢与内积
# ======================================================================
# 物理语言：波函数 ψ(x)        ->  量子信息语言：态矢 |ψ>
# 基态 |0> 和 |1> 就是二维复向量空间的一组正交基。
print("\n--- Part B：态矢与内积 ---")

ket0 = np.array([1, 0], dtype=complex)
ket1 = np.array([0, 1], dtype=complex)

print(f"|0> = {ket0}")
print(f"|1> = {ket1}")

# TODO 1: 构造叠加态 |+> = (|0> + |1>) / sqrt(2)
#   提示：直接用 + 号相加，再除以 np.sqrt(2)
ket_plus = None  # <-- 把 None 换成你的代码


# TODO 2: 计算内积 <0|+>
#   提示：np.vdot(a, b) 会先对 a 取共轭再求内积，也就是 <a|b>
#   <0|+> 的期望结果是 1/sqrt(2) ≈ 0.7071
inner_0_plus = None  # <-- 把 None 换成你的代码


# TODO 3: 计算 |+> 的模方 <+|+>，用来检查归一化
#   期望结果是 1.0（归一化）
norm_plus_sq = None  # <-- 把 None 换成你的代码


# TODO 4: 判断 |0> 与 |1> 是否正交
#   正交意味着内积为 0
#   提示：用 np.isclose(...) 返回 True/False
are_orthogonal = None  # <-- 把 None 换成你的代码


print(f"\n|+>         = {ket_plus}")
print(f"<0|+>       = {inner_0_plus}   (期望 ≈ 0.7071)")
print(f"<+|+>       = {norm_plus_sq}   (期望 = 1.0)")
print(f"<0|1> 正交? = {are_orthogonal}   (期望 True)")


# ======================================================================
# Part C · 张量积（多量子比特的语言）
# ======================================================================
# 两个量子比特的态空间是 2x2 = 4 维。
# 物理语言里叫"两个粒子的直积态"，量子信息里叫 Kronecker 积。
print("\n--- Part C：张量积 ---")

# 示范：|00> = |0> ⊗ |0>
ket00 = np.kron(ket0, ket0)
print(f"|00> = {ket00}")

# TODO 5: 构造 |01> = |0> ⊗ |1>，期望 [0, 1, 0, 0]
ket01 = None  # <-- 把 None 换成你的代码


# TODO 6: 构造 |+> ⊗ |+>，期望 [0.5, 0.5, 0.5, 0.5]
ket_plus_plus = None  # <-- 把 None 换成你的代码


# TODO 7: 验证 |+>⊗|+> 也是归一化的（模方应为 1.0）
norm_pp = None  # <-- 把 None 换成你的代码


print(f"|01>         = {ket01}")
print(f"|+>⊗|+>      = {ket_plus_plus}")
print(f"<++|++>      = {norm_pp}   (期望 = 1.0)")


# ======================================================================
# Part D · 一个"物理直觉"问题（写在注释里回答）
# ======================================================================
# 问题：|+> = (|0>+|1>)/sqrt(2) 和 |-|> = (|0>-|1>)/sqrt(2)
#       这两个态在"测量"上有什么区别？在"相位"上有什么区别？
#
# 你的回答：
# TODO 8: 在这里写下你的答案（用注释，中文即可）
#
#


# ======================================================================
# 自动检查（不用改）
# ======================================================================
print("\n" + "=" * 62)
print(" 自动检查")
print("=" * 62)

checks = []

def check(name, condition):
    checks.append((name, bool(condition)))

try:
    check("TODO 1  构造 |+> 形状正确",
          ket_plus is not None and np.shape(ket_plus) == (2,))
    check("TODO 1  |+> 数值正确",
          ket_plus is not None and np.allclose(ket_plus, [1/np.sqrt(2), 1/np.sqrt(2)]))
    check("TODO 2  <0|+> ≈ 0.7071",
          inner_0_plus is not None and np.isclose(inner_0_plus, 1/np.sqrt(2)))
    check("TODO 3  <+|+> = 1.0",
          norm_plus_sq is not None and np.isclose(norm_plus_sq, 1.0))
    check("TODO 4  |0> 与 |1> 正交",
          are_orthogonal is not None and bool(are_orthogonal) is True)
    check("TODO 5  |01> = [0,1,0,0]",
          ket01 is not None and np.allclose(ket01, [0, 1, 0, 0]))
    check("TODO 6  |+>⊗|+> = [0.5]*4",
          ket_plus_plus is not None and np.allclose(ket_plus_plus, [0.5]*4))
    check("TODO 7  |+>⊗|+> 归一化",
          norm_pp is not None and np.isclose(norm_pp, 1.0))
except Exception as e:
    print(f"\n[!] 运行出错：{type(e).__name__}: {e}")
    print("    常见原因：TODO 还没填，值是 None，参与运算就会报错。")

passed = sum(1 for _, ok in checks if ok)
for name, ok in checks:
    print(f"  {'[OK]  ' if ok else '[TODO]'} {name}")

print(f"\n通过 {passed} / {len(checks)}")

if passed == len(checks):
    print("\n全部通过。你已经完成了第一周的编程任务。")
    print("接下来：把这份代码 git commit 上去，然后开始 ex2。")
else:
    print("\n还有 TODO 没完成。补完后重新运行本脚本。")
    print("卡住了就把报错信息发给我。")
