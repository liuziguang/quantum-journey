"""
F1 参考解：函数基础
===================
⚠️ **先自己做完 F1_函数基础.py，卡住 30 分钟以上，再来看这个。**

运行：
    python F1_solution.py

它会把 8 个 TODO 的标准答案实现一遍并断言验证。
"""
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

print("=" * 66)
print(" F1 参考解")
print("=" * 66)


# ======================================================================
# Part A · 定义与调用
# ======================================================================
print("\n--- Part A：定义与调用 ---")


def square(x):
    """返回 x 的平方"""
    # TODO 1 答案
    # 关键：用 return 把结果交出去，不是 print
    return x ** 2


sq3 = square(3)
print(f"square(3) = {sq3}")
print(f"square(5) = {square(5)}")


# ======================================================================
# Part B · 参数
# ======================================================================
print("\n--- Part B：参数 ---")


def add(a, b):
    """返回 a + b"""
    # TODO 2 答案
    return a + b


def power(base, exp):
    """返回 base 的 exp 次方"""
    # TODO 3 答案
    # 注意参数顺序：(base, exp) —— power(2,10) 是 2 的 10 次方
    return base ** exp


print(f"add(2,3)    = {add(2, 3)}")
print(f"power(2,10) = {power(2, 10)}")
print(f"power(10,2) = {power(10, 2)}   ← 参数顺序反了结果就完全不同")


# ======================================================================
# Part C · return vs print
# ======================================================================
print("\n--- Part C：return vs print ---")


def square_print(x):
    """只显示，不返回"""
    print(f"  [square_print 打印] {x ** 2}")
    # 注意：这里没有 return，所以函数返回 None


def square_return(x):
    """把结果交出去"""
    return x ** 2


def max_print(items):
    """打印最大值（错误示范）"""
    # TODO 4 答案（前半）
    # 只显示，不返回 —— 调用者拿不到任何东西
    print(f"  [max_print 打印] {max(items)}")


def max_return(items):
    """返回最大值"""
    # TODO 4 答案（后半）
    return max(items)


result_of_print = square_print(3)
result_of_return = square_return(3)

print(f"square_print 的返回值 : {result_of_print}   ← None，因为没 return")
print(f"square_return 的返回值: {result_of_return}   ← 9，拿到了")

# TODO 5 答案：用 max_return 的结果继续计算
max_plus_100 = max_return([3, 8, 1]) + 100

print(f"max_return([3,8,1]) + 100 = {max_plus_100}")
_print_result = max_print([3, 8, 1])
print(f"max_print 的返回值       : {_print_result}   ← 又是 None")


# ======================================================================
# Part D · 返回多个值
# ======================================================================
print("\n--- Part D：返回多个值 ---")


def min_max(items):
    """同时返回最小值和最大值"""
    # TODO 6 答案
    # Python 里写 `return a, b` 其实返回的是一个元组 (a, b)
    return min(items), max(items)


_pair = min_max([3, 8, 1, 6])
print(f"min_max([3,8,1,6]) = {_pair}   类型是 {type(_pair).__name__}")

# 可以直接拆开
lo, hi = min_max([3, 8, 1, 6])
print(f"拆开后：lo={lo}, hi={hi}")


# ======================================================================
# Part E · 作用域
# ======================================================================
print("\n--- Part E：作用域 ---")


def count_evens(numbers):
    """返回 numbers 中偶数的个数"""
    # TODO 7 答案
    # result 是【局部变量】—— 只在函数内部存在，函数一结束就消失
    result = 0
    for n in numbers:
        if n % 2 == 0:          # % 是取余数，偶数除 2 余 0
            result += 1
    return result


print(f"count_evens([1,2,3,4,5,6]) = {count_evens([1, 2, 3, 4, 5, 6])}")
print(f"count_evens([1,3,5])       = {count_evens([1, 3, 5])}")


# ======================================================================
# Part F · 提前 return
# ======================================================================
print("\n--- Part F：提前 return ---")


def first_negative(numbers):
    """返回第一个负数；没有则返回 None"""
    # TODO 8 答案
    for n in numbers:
        if n < 0:
            return n            # 找到了，立刻收工，后面不再看
    return None                 # 循环走完都没找到


print(f"first_negative([1,2,-3,4]) = {first_negative([1, 2, -3, 4])}")
print(f"first_negative([1,2,3])    = {first_negative([1, 2, 3])}")


# ======================================================================
# 断言验证：和 F1_函数基础.py 的 15 项检查一一对应
# ======================================================================
print("\n" + "=" * 66)
print(" 验证（与 F1 的 15 项检查对应）")
print("=" * 66)

ok = []

def chk(desc, cond):
    ok.append((desc, bool(cond)))

# Part A
chk("TODO 1  square(3) == 9", square(3) == 9)
chk("TODO 1  square(5) == 25", square(5) == 25)
chk("TODO 1  sq3 == 9", sq3 == 9)
# Part B
chk("TODO 2  add(2,3) == 5", add(2, 3) == 5)
chk("TODO 3  power(2,10) == 1024", power(2, 10) == 1024)
chk("TODO 3  power(10,2) == 100", power(10, 2) == 100)
# Part C
chk("TODO 4  max_return([3,8,1]) == 8", max_return([3, 8, 1]) == 8)
chk("TODO 4  max_print 返回 None（只显示不返回）",
    _print_result is None and max_return([3, 8, 1]) == 8)
chk("TODO 5  max_plus_100 == 108", max_plus_100 == 108)
# Part D
chk("TODO 6  min_max([3,8,1,6]) == (1,8)", min_max([3, 8, 1, 6]) == (1, 8))
chk("TODO 6  min_max([5,5,5]) == (5,5)", min_max([5, 5, 5]) == (5, 5))
# Part E
chk("TODO 7  count_evens([1..6]) == 3", count_evens([1, 2, 3, 4, 5, 6]) == 3)
chk("TODO 7  count_evens([1,3,5]) == 0", count_evens([1, 3, 5]) == 0)
# Part F
chk("TODO 8  first_negative 找到 -3", first_negative([1, 2, -3, 4]) == -3)
chk("TODO 8  first_negative 无负数返回 None（且能找到 -3）",
    first_negative([1, 2, -3, 4]) == -3 and first_negative([1, 2, 3]) is None)

for desc, passed in ok:
    print(f"  {'[OK]  ' if passed else '[FAIL]'} {desc}")

n = sum(1 for _, p in ok if p)
print(f"\n通过 {n} / {len(ok)}")
assert n == len(ok), "参考解有问题！"
print("\n[OK] 参考解与 F1 的判分标准一致。")
print("\n现在回 F1_函数基础.py，把你的 TODO 填上，跑到 15/15。")
