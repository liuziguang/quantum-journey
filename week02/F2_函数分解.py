"""
F2 · 函数分解（把需求拆成函数）
===============================
配套阅读：F0_函数学习计划.md 第六节

这个文件练的是**最核心也最难的一项技能**：
    拿到一段中文需求 → 决定该写几个函数、每个干什么 → 再动手写代码

内容：
  Part A  【示范】完整演示"从需求到函数"的五步（读，不用改）
  Part B  【设计练习】看需求，只写函数清单（不判分，自己对照参考答案）
  Part C  【拆一锅粥】把一段烂代码拆成 4 个函数（判分）
  Part D  【独立完成】给你需求，自己设计并实现（判分）

运行：python F2_函数分解.py
预计耗时：1.5–2 小时

⚠️ Part C 和 Part D 用的是**和你作业不同的题目**，
   所以这个文件不会替你把 my_first_program.py 做掉。作业还是要自己写。
"""

import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


print("=" * 66)
print(" F2 · 函数分解")
print("=" * 66)


# ======================================================================
# Part A ·【示范】从需求到函数，完整走一遍
# ======================================================================
print("\n" + "=" * 66)
print(" Part A：示范（读一遍，理解方法）")
print("=" * 66)

print("""
需求原文：
    给定一串数字 numbers，
    1. 求所有数字的总和
    2. 求平均值
    3. 找出最大的数字
    4. 把所有数字翻倍
""")

print("第 1 步：圈出「动词」")
print("""
    1. 求...总和     → 动词：求和
    2. 求平均值      → 动词：求平均
    3. 找出最大的    → 动词：求最大
    4. 翻倍          → 动词：变换每个元素
""")

print("第 2 步：一个动词 → 一个函数（决定名字和输入输出）")
print("""
    total(numbers)      → 输入：一串数字    输出：一个数
    average(numbers)    → 输入：一串数字    输出：一个数
    largest(numbers)    → 输入：一串数字    输出：一个数
    doubled(numbers)    → 输入：一串数字    输出：一串数字（新列表）
""")

print("第 3 步：写函数签名（先不实现，全写 pass）")
print("第 4 步：逐个实现，实现一个测一个")
print("第 5 步：在 main 里串联")


# 【示范代码】这就是第 3–5 步的结果
def total(numbers):
    """返回所有数字的总和"""
    result = 0
    for n in numbers:
        result += n
    return result


def average(numbers):
    """返回平均值"""
    return total(numbers) / len(numbers)      # ← 函数可以调用别的函数！


def largest(numbers):
    """返回最大的数字"""
    best = numbers[0]
    for n in numbers:
        if n > best:
            best = n
    return best


def doubled(numbers):
    """返回每个元素翻倍后的新列表"""
    result = []
    for n in numbers:
        result.append(n * 2)
    return result


if __name__ == "__main__":
    data = [3, 8, 1, 6, 10]
    print(f"\n  数据: {data}")
    print(f"  total(data)    = {total(data)}      (期望 28)")
    print(f"  average(data)  = {average(data)}    (期望 5.6)")
    print(f"  largest(data)  = {largest(data)}    (期望 10)")
    print(f"  doubled(data)  = {doubled(data)}   (期望 [6,16,2,12,20])")


print("\n" + "-" * 66)
print("💡 从示范里要记住三件事：")
print("   ① 每个函数只做一件事——名字里不该出现「和 / 并 / 然后」")
print("   ② 函数可以调用别的函数（average 用了 total）")
print("   ③ 「打印」不写进函数里，统一放在 main 里")
print("-" * 66)


# ======================================================================
# Part B ·【设计练习】只写清单，不写代码
# ======================================================================
print("\n" + "=" * 66)
print(" Part B：设计练习（不判分，写完自己对照答案）")
print("=" * 66)

print("""
下面有 3 个需求。**不要写代码**，只在注释里写出：
    (a) 你会写哪几个函数？（起名字）
    (b) 每个函数的输入是什么、输出是什么？

────────────────────────────────────────
需求 1：一个学生成绩列表 scores
    - 算平均分
    - 找出最高分
    - 数出及格（>=60）的人数
    - 把分数从高到低排序

需求 2：一段英文文本 text
    - 按空格切成单词
    - 统计一共有多少个单词
    - 找出最长的那个单词

需求 3：一个购物车 cart，每项是 (商品名, 单价, 数量)
    - 算总价
    - 找出最贵的那一项（按小计 = 单价 × 数量）
    - 打 8 折后的总价
────────────────────────────────────────
""")

# ↓↓↓ 在这里写下你的答案（用注释，中文即可）↓↓↓

# 需求 1 的函数设计：
#
#
#

# 需求 2 的函数设计：
#
#
#

# 需求 3 的函数设计：
#
#
#

# ↑↑↑ 写完了再往下看参考答案 ↑↑↑

print("\n" + "-" * 66)
print("📖 Part B 参考答案（全部写完后再看）")
print("-" * 66)
print("""
需求 1（4 个函数）：
    average(scores)              -> 一个数
    highest(scores)              -> 一个数
    count_passing(scores)        -> 一个整数
    sort_desc(scores)            -> 一个新列表

需求 2（3 个函数）：
    split_words(text)            -> 单词列表
    count_words(words)           -> 一个整数
    longest_word(words)          -> 一个字符串

需求 3（3–4 个函数）：
    subtotal(item)               -> 一个数（单价 × 数量）  ← 小函数，被下面复用
    cart_total(cart)             -> 一个数
    most_expensive(cart)         -> 一个 item
    apply_discount(amount, rate) -> 一个数

⚠️ 关键点：
   ① 需求里的「打印 / 显示」都不算函数，它们属于 main
   ② 需求 3 里「小计」这个动作出现了两次（算总价、找最贵），
      所以单独抽成 subtotal —— 这叫「发现重复就抽函数」
   ③ 如果你的函数名里有「和」「并且」「然后」，说明该拆开
""")


# ======================================================================
# Part C ·【拆一锅粥】把烂代码拆成好函数
# ======================================================================
print("\n" + "=" * 66)
print(" Part C：拆一锅粥")
print("=" * 66)

print("""
下面这段代码**能跑、结果也对**，但写得很糟：
所有事情混在一起，没有函数，想改一处都很难。

你的任务：把它拆成 4 个函数 + 一个 main。
""")

# ---------- 烂代码（只读，别改这段）----------
numbers_demo = [3, 8, 1, 6, 10, 7, 4, 2, 9, 5]

evens_demo = []
for n in numbers_demo:
    if n % 2 == 0:
        evens_demo.append(n)

squares_demo = []
for n in numbers_demo:
    squares_demo.append(n * n)

best_demo = numbers_demo[0]
best_pos_demo = 0
for i in range(len(numbers_demo)):
    if numbers_demo[i] > best_demo:
        best_demo = numbers_demo[i]
        best_pos_demo = i

rev_demo = []
for i in range(len(numbers_demo) - 1, -1, -1):
    rev_demo.append(numbers_demo[i])
# ---------- 烂代码结束 ----------

print(f"  烂代码的输出: evens={evens_demo}")
print(f"                squares={squares_demo}")
print(f"                best={best_demo}, pos={best_pos_demo}")
print(f"                reversed={rev_demo}")

print("""
你的任务：实现下面 4 个函数，让它们产出上面同样的结果。
    find_evens(numbers)   -> 所有偶数组成的列表
    squares(numbers)      -> 每个元素的平方，组成新列表
    argmax(numbers)       -> 最大值的「下标」（注意是下标不是值！）
    reverse_list(numbers) -> 倒序后的新列表
""")

# TODO 1: 返回所有偶数组成的列表
def find_evens(numbers):
    """返回 numbers 中所有偶数组成的列表"""
    pass          # <-- 换成你的代码


# TODO 2: 返回每个元素的平方组成的新列表
def squares(numbers):
    """返回每个元素平方后的新列表"""
    pass          # <-- 换成你的代码


# TODO 3: 返回最大值的下标
#   提示：先假设第 0 个最大（best_pos = 0），
#        然后 for i in range(len(numbers)): 比较 numbers[i] 和 numbers[best_pos]
def argmax(numbers):
    """返回最大值所在的下标"""
    pass          # <-- 换成你的代码


# TODO 4: 返回倒序后的新列表
#   提示：新列表 result = []，然后从最后一个元素往前 append
#        range(len(numbers) - 1, -1, -1) 会从最后往前数
def reverse_list(numbers):
    """返回倒序后的新列表"""
    pass          # <-- 换成你的代码


# ======================================================================
# Part D ·【独立完成】给你需求，自己设计并实现
# ======================================================================
print("\n" + "=" * 66)
print(" Part D：独立完成（换一道新题）")
print("=" * 66)

print("""
需求：给定一周的气温列表 temps（摄氏度）
    1. 算平均气温
    2. 找出最高气温
    3. 数出低于 0 度的天数
    4. 把所有气温转换成华氏度

转换公式：华氏 = 摄氏 × 9 / 5 + 32
""")

# TODO 5: 平均气温
def average(temps):
    """返回平均气温"""
    pass          # <-- 换成你的代码


# TODO 6: 最高气温
def hottest(temps):
    """返回最高气温"""
    pass          # <-- 换成你的代码


# TODO 7: 低于 0 度的天数
def count_below_zero(temps):
    """返回低于 0 度的天数"""
    pass          # <-- 换成你的代码


# TODO 8: 转换成华氏度，返回新列表
def to_fahrenheit(temps):
    """返回转换后的华氏温度列表"""
    pass          # <-- 换成你的代码


# main：串联（这段已经给你写好了，不用改）
if __name__ == "__main__":
    week = [-5, 3, 12, 7, -1, 0, 8]
    print(f"\n  一周气温: {week}")
    print(f"  平均气温:     {average(week)}")
    print(f"  最高气温:     {hottest(week)}")
    print(f"  低于0度的天数: {count_below_zero(week)}")
    print(f"  华氏温度:     {to_fahrenheit(week)}")


# ======================================================================
# 自动检查（不用改）
# ======================================================================
print("\n" + "=" * 66)
print(" 自动检查")
print("=" * 66)

checks = []

def check(name, condition):
    try:
        checks.append((name, bool(condition)))
    except Exception:
        checks.append((name, False))

def _close_list(a, b, tol=1e-9):
    """安全地比较两个列表（a 可能是 None）"""
    if not isinstance(a, list) or len(a) != len(b):
        return False
    try:
        return all(abs(x - y) < tol for x, y in zip(a, b))
    except Exception:
        return False

_demo = [3, 8, 1, 6, 10, 7, 4, 2, 9, 5]

# Part C
check("TODO 1  find_evens 正确", _close_list(find_evens(_demo), [8, 6, 10, 4, 2]))
check("TODO 1  find_evens 无偶数返回空表", _close_list(find_evens([1, 3, 5]), []))
check("TODO 2  squares 正确", _close_list(squares([1, 2, 3]), [1, 4, 9]))
check("TODO 2  squares 处理负数", _close_list(squares([-2, 3]), [4, 9]))
check("TODO 3  argmax 正确（返回下标）", argmax(_demo) == 4)
check("TODO 3  argmax 处理首位最大", argmax([99, 1, 2]) == 0)
check("TODO 4  reverse_list 正确", _close_list(reverse_list([1, 2, 3]), [3, 2, 1]))
check("TODO 4  reverse_list 空表安全", _close_list(reverse_list([]), []))

# Part D
check("TODO 5  average([10,20,30]) == 20", average([10, 20, 30]) == 20)
check("TODO 6  hottest([-5,3,12,7]) == 12", hottest([-5, 3, 12, 7]) == 12)
check("TODO 7  count_below_zero([-5,3,-1,0,7]) == 2",
      count_below_zero([-5, 3, -1, 0, 7]) == 2)
check("TODO 8  to_fahrenheit([0,100,-40]) == [32,212,-40]",
      _close_list(to_fahrenheit([0, 100, -40]), [32.0, 212.0, -40.0]))

passed = sum(1 for _, ok in checks if ok)
for name, ok in checks:
    print(f"  {'[OK]  ' if ok else '[TODO]'} {name}")

print(f"\n通过 {passed} / {len(checks)}")

if passed == len(checks):
    print("\n全部通过。")
    print("现在你已经具备拆解函数的能力了 —— 回到 my_first_program.py，")
    print("用 Part A 示范的五步法把它做出来。")
else:
    print("\n还有 TODO 没完成（Part B 是写注释，不参与判分）。")
    print("卡住了把 TODO 编号和报错发我。")
