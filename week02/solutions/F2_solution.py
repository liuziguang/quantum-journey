"""
F2 参考解：函数分解
===================
⚠️ **先自己做完 F2_函数分解.py，卡住 30 分钟以上，再来看这个。**

运行：
    python F2_solution.py
"""
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

print("=" * 66)
print(" F2 参考解")
print("=" * 66)


# ======================================================================
# Part B · 设计练习的参考答案（这部分不判分，只是给个对照）
# ======================================================================
print("""
--- Part B：设计练习参考答案 ---

需求 1（学生成绩，4 个函数）：
    average(scores)         -> 一个数
    highest(scores)         -> 一个数
    count_passing(scores)   -> 一个整数
    sort_desc(scores)       -> 一个新列表

需求 2（英文文本，3 个函数）：
    split_words(text)       -> 单词列表
    count_words(words)      -> 一个整数
    longest_word(words)     -> 一个字符串

需求 3（购物车，4 个函数）：
    subtotal(item)          -> 一个数（单价 × 数量）  ← 小函数，被下面复用
    cart_total(cart)        -> 一个数
    most_expensive(cart)    -> 一个 item
    apply_discount(amount, rate) -> 一个数

三个要点：
  ① 需求里的「打印 / 显示」不算函数，属于 main
  ② 需求 3 里「小计」出现两次 → 抽成 subtotal（发现重复就抽函数）
  ③ 函数名里出现「和 / 并且 / 然后」→ 说明该拆
""")


# ======================================================================
# Part C · 把"一锅粥"拆成 4 个函数
# ======================================================================
print("--- Part C：拆一锅粥 ---")


def find_evens(numbers):
    """返回 numbers 中所有偶数组成的列表"""
    # TODO 1 答案：建空列表 → 遍历 → 判断 → append
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result


def squares(numbers):
    """返回每个元素平方后的新列表"""
    # TODO 2 答案：结构和 find_evens 一样，只是少了 if
    result = []
    for n in numbers:
        result.append(n * n)
    return result


def argmax(numbers):
    """返回最大值所在的下标"""
    # TODO 3 答案
    # 套路：先假设第 0 个最大 → 遍历 → 谁大就更新下标
    # 注意返回的是【下标】，不是值
    best_pos = 0
    for i in range(len(numbers)):
        if numbers[i] > numbers[best_pos]:
            best_pos = i
    return best_pos


def reverse_list(numbers):
    """返回倒序后的新列表"""
    # TODO 4 答案
    # range(len-1, -1, -1) 从最后一个下标一路数到 0
    result = []
    for i in range(len(numbers) - 1, -1, -1):
        result.append(numbers[i])
    return result


_demo = [3, 8, 1, 6, 10, 7, 4, 2, 9, 5]
print(f"find_evens    = {find_evens(_demo)}")
print(f"squares       = {squares(_demo)}")
print(f"argmax        = {argmax(_demo)}   ← 下标，对应值 {_demo[argmax(_demo)]}")
print(f"reverse_list  = {reverse_list(_demo)}")


# ======================================================================
# Part D · 独立完成（气温题）
# ======================================================================
print("\n--- Part D：独立完成（气温）---")


def average(temps):
    """返回平均气温"""
    # TODO 5 答案：先求和，再除以个数
    s = 0
    for t in temps:
        s += t
    return s / len(temps)


def hottest(temps):
    """返回最高气温"""
    # TODO 6 答案：内置 max() 就够了，不需要自己写循环
    return max(temps)


def count_below_zero(temps):
    """返回低于 0 度的天数"""
    # TODO 7 答案：和 count_evens 完全同构
    c = 0
    for t in temps:
        if t < 0:
            c += 1
    return c


def to_fahrenheit(temps):
    """返回转换后的华氏温度列表"""
    # TODO 8 答案：注意是"返回新列表"，不是改原列表
    result = []
    for t in temps:
        result.append(t * 9 / 5 + 32)
    return result


_week = [-5, 3, 12, 7, -1, 0, 8]
print(f"平均气温:     {average(_week)}")
print(f"最高气温:     {hottest(_week)}")
print(f"低于0度的天数: {count_below_zero(_week)}")
print(f"华氏温度:     {to_fahrenheit(_week)}")


# ======================================================================
# 断言验证：和 F2_函数分解.py 的 12 项检查一一对应
# ======================================================================
print("\n" + "=" * 66)
print(" 验证（与 F2 的 12 项检查对应）")
print("=" * 66)

ok = []

def chk(desc, cond):
    ok.append((desc, bool(cond)))

chk("TODO 1  find_evens(demo) 正确", find_evens(_demo) == [8, 6, 10, 4, 2])
chk("TODO 1  find_evens([1,3,5]) == []", find_evens([1, 3, 5]) == [])
chk("TODO 2  squares([1,2,3]) == [1,4,9]", squares([1, 2, 3]) == [1, 4, 9])
chk("TODO 2  squares([-2,3]) == [4,9]", squares([-2, 3]) == [4, 9])
chk("TODO 3  argmax(demo) == 4", argmax(_demo) == 4)
chk("TODO 3  argmax([99,1,2]) == 0", argmax([99, 1, 2]) == 0)
chk("TODO 4  reverse_list([1,2,3]) == [3,2,1]", reverse_list([1, 2, 3]) == [3, 2, 1])
chk("TODO 4  reverse_list([]) == []", reverse_list([]) == [])
chk("TODO 5  average([10,20,30]) == 20", average([10, 20, 30]) == 20)
chk("TODO 6  hottest([-5,3,12,7]) == 12", hottest([-5, 3, 12, 7]) == 12)
chk("TODO 7  count_below_zero([-5,3,-1,0,7]) == 2", count_below_zero([-5, 3, -1, 0, 7]) == 2)
chk("TODO 8  to_fahrenheit([0,100,-40]) == [32,212,-40]",
    to_fahrenheit([0, 100, -40]) == [32.0, 212.0, -40.0])

for desc, passed in ok:
    print(f"  {'[OK]  ' if passed else '[FAIL]'} {desc}")

n = sum(1 for _, p in ok if p)
print(f"\n通过 {n} / {len(ok)}")
assert n == len(ok), "参考解有问题！"
print("\n[OK] 参考解与 F2 的判分标准一致。")
