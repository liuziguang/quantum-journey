"""
F1 · 函数基础（动手练）
=======================
配套阅读：F0_函数学习计划.md（如果还没读，先去读）

本文件练 6 件事：
  Part A  定义与调用
  Part B  参数（多个参数、参数顺序）
  Part C  ⚠️ return vs print（初学者最大的坑）
  Part D  返回多个值
  Part E  作用域（局部变量）
  Part F  提前 return

运行：python F1_函数基础.py
判分：文件末尾有自动检查，全绿就说明机制掌握了。
预计耗时：1.5–2 小时

规矩：卡住 30 分钟就发我。格式：「我想做 X，试了 Y，报错 Z」。
"""

import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


print("=" * 66)
print(" F1 · 函数基础")
print("=" * 66)


# ======================================================================
# Part A · 定义与调用
# ======================================================================
print("\n" + "=" * 66)
print(" Part A：定义与调用")
print("=" * 66)

# 【示范】函数的结构：def 名字(参数):  然后缩进的函数体，最后 return 结果
def show_a_message(text):
    """把 text 加个边框打印出来（这个函数只负责显示，所以用 print）"""
    print(f"  >>> {text}")

show_a_message("这是示范：怎么定义、怎么调用")

# TODO 1: 定义函数 square(x)，返回 x 的平方
#   提示：函数体里写  return x ** 2
def square(x):
    """返回 x 的平方"""
    return x**2          

# 调用它，把结果存进变量
sq3 = square(3)

print(f"\nsquare(3) = {sq3}   (期望 9)")
print(f"square(5) = {square(5)}   (期望 25)")


# ======================================================================
# Part B · 参数
# ======================================================================
print("\n" + "=" * 66)
print(" Part B：参数（输入的东西）")
print("=" * 66)

# 【示范】两个参数，按位置对应
def introduce(name, age):
    """打印一句自我介绍"""
    print(f"  我叫 {name}，今年 {age} 岁")

introduce("小明", 25)          # name="小明", age=25

# TODO 2: 定义函数 add(a, b)，返回 a + b
def add(a, b):
    """返回 a + b"""
    return a + b          

# TODO 3: 定义函数 power(base, exp)，返回 base 的 exp 次方
#   注意参数顺序：power(2, 10) 表示 2 的 10 次方
def power(base, exp):
    """返回 base 的 exp 次方"""
    y = base ** exp;
    return y          

print(f"\nadd(2, 3)     = {add(2, 3)}   (期望 5)")
print(f"power(2, 10)  = {power(2, 10)}   (期望 1024)")
print(f"power(10, 2)  = {power(10, 2)}   (期望 100 ← 注意参数顺序！)")


# ======================================================================
# Part C · ⚠️ return vs print（重点！）
# ======================================================================
print("\n" + "=" * 66)
print(" Part C：return vs print —— 这两个完全不是一回事")
print("=" * 66)

# 下面两个函数做的是同一件事（求平方），但一个用 print，一个用 return
def square_print(x):
    """只显示，不返回"""
    print(f"  square_print 打印出: {x**2}")

def square_return(x):
    """把结果交出去"""
    return x ** 2

print("\n【观察 1】调用 square_print：屏幕上出现结果，但函数本身没有产出")
result_of_print = square_print(3)
print(f"  result_of_print 的值是: {result_of_print}")
print("  ↑ 是 None！因为 square_print 只 display，没有 return")

print("\n【观察 2】调用 square_return：屏幕没输出，但函数产出了一个值")
result_of_return = square_return(3)
print(f"  result_of_return 的值是: {result_of_return}")
print("  ↑ 是 9。因为 return 把值交出来了")

print("\n【观察 3】关键差别：能不能拿着结果继续算")
print(f"  用 return 的结果继续计算: {square_return(3) + 1}   ← 可以")
print("  用 print 的结果继续计算: 会报 TypeError，因为 None 不能做加法")

# 证明一下：
try:
    _ = result_of_print + 1
    print("  （没有报错？那不应当）")
except TypeError as e:
    print(f"  确实报错了: {type(e).__name__}")

# TODO 4: 定义两个函数
#   max_print(items)  —— 打印 items 里的最大值（错误示范，只用 print）
#   max_return(items) —— 返回 items 里的最大值（正确做法）
#   提示：内置函数 max(items) 可以直接求最大值
def max_print(items):
    """打印最大值（错误示范）"""
    print(max(items))          

def max_return(items):
    """返回最大值"""
    return max(items)          

# TODO 5: 用 max_return 的结果继续计算：最大值 + 100
max_plus_100 = max_return([3, 8, 1]) + 100   # <-- 换成 max_return([3, 8, 1]) + 100

print(f"\nmax_return([3,8,1]) 继续算 +100 = {max_plus_100}   (期望 108)")
print("  ↑ 这就是 return 的意义：结果能被继续使用")

# 顺带看看 max_print 返回什么
print("\nmax_print([3,8,1]) 的返回值:")
_print_result = max_print([3, 8, 1])
print(f"  返回了 {_print_result}   ← 又是 None")


# ======================================================================
# Part D · 返回多个值
# ======================================================================
print("\n" + "=" * 66)
print(" Part D：一个函数返回多个值")
print("=" * 66)

# 【示范】Python 可以直接一次赋值给多个变量
x_demo, y_demo = 10, 20
print(f"\n  一次赋两个值: x_demo={x_demo}, y_demo={y_demo}")

def two_values():
    """返回两个值"""
    return 1, 2          # 其实返回的是一个"元组" (1, 2)

p, q = two_values()      # 自动拆开
print(f"  函数返回两个值，自动拆开: p={p}, q={q}")

# 不想拆开也行，它就是一个元组
pair = two_values()
print(f"  不拆开的话是个元组: {pair}，取第一个用 pair[0] = {pair[0]}")

# TODO 6: 定义 min_max(items)，同时返回最小值和最大值
#   例如 min_max([3, 8, 1, 6]) 应该返回 (1, 8)
#   提示：内置函数 min(items) 和 max(items)
def min_max(items):
    """同时返回最小值和最大值"""

    return min(items), max(items)          # <-- 换成 return ...

# 安全地拆包（如果还没实现，不会崩）
_mm = min_max([3, 8, 1, 6])
lo = _mm[0] if isinstance(_mm, tuple) else None
hi = _mm[1] if isinstance(_mm, tuple) else None

print(f"\n  min_max([3,8,1,6]) → min={lo}, max={hi}   (期望 1 和 8)")


# ======================================================================
# Part E · 作用域（局部变量）
# ======================================================================
print("\n" + "=" * 66)
print(" Part E：作用域 —— 函数里的变量，外面看不见")
print("=" * 66)

def scope_demo():
    """函数内部定义的变量，只在这个函数里存在"""
    inner_var = 42
    return inner_var

print(f"\n  调用 scope_demo() 得到 {scope_demo()}")
print("  但函数里的 inner_var 在外面是找不到的。")
print("  如果把下面这行的注释去掉，就会报 NameError：")
print("  # print(inner_var)")

# 证明一下
try:
    print(inner_var)          # noqa: F821  （这一行故意写错，为了演示）
except NameError as e:
    print(f"  确实报错了: {type(e).__name__}")
    print("  ↑ 这不是 bug，是保护机制：函数不会污染外面的变量")

# TODO 7: 定义 count_evens(numbers)，返回 numbers 中偶数的个数
#   要求：在函数内部用一个局部变量（比如 result）来累加
#   提示：for n in numbers:  if n % 2 == 0:  result += 1
def count_evens(numbers):
    """返回 numbers 中偶数的个数"""
    result = 0
    for n in numbers:   
        if n % 2 == 0:
            result += 1          
    return result

print(f"\n  count_evens([1,2,3,4,5,6]) = {count_evens([1, 2, 3, 4, 5, 6])}   (期望 3)")


# ======================================================================
# Part F · 提前 return
# ======================================================================
print("\n" + "=" * 66)
print(" Part F：提前 return（找到就收工）")
print("=" * 66)

# 【示范】函数遇到 return 就立刻结束，后面的代码不再执行
def find_first_zero(numbers):
    """返回第一个 0 所在的下标；没有 0 就返回 None"""
    for i, n in enumerate(numbers):
        if n == 0:
            return i          # 找到了，立刻收工
    return None               # 循环走完还没找到

print(f"\n  find_first_zero([5, 3, 0, 9]) = {find_first_zero([5, 3, 0, 9])}   (期望 2)")
print(f"  find_first_zero([5, 3, 9])    = {find_first_zero([5, 3, 9])}   (期望 None)")

# TODO 8: 定义 first_negative(numbers)，返回第一个负数；没有负数就返回 None
#   模仿上面的 find_first_zero 写法
def first_negative(numbers):
    """返回第一个负数；没有则返回 None"""
    for i in numbers:
        if i < 0:
            return i
    return None          

print(f"\n  first_negative([1, 2, -3, 4]) = {first_negative([1, 2, -3, 4])}   (期望 -3)")
print(f"  first_negative([1, 2, 3])     = {first_negative([1, 2, 3])}   (期望 None)")


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

# Part A
check("TODO 1  square(3) == 9", square(3) == 9)
check("TODO 1  square(5) == 25", square(5) == 25)
check("TODO 1  sq3 == 9", sq3 == 9)

# Part B
check("TODO 2  add(2,3) == 5", add(2, 3) == 5)
check("TODO 3  power(2,10) == 1024", power(2, 10) == 1024)
check("TODO 3  power(10,2) == 100（参数顺序）", power(10, 2) == 100)

# Part C
check("TODO 4  max_return([3,8,1]) == 8", max_return([3, 8, 1]) == 8)
check("TODO 4  max_print 只显示不返回（返回 None）",
      _print_result is None and max_return([3, 8, 1]) == 8)
check("TODO 5  max_plus_100 == 108", max_plus_100 == 108)

# Part D
check("TODO 6  min_max([3,8,1,6]) == (1,8)", min_max([3, 8, 1, 6]) == (1, 8))
check("TODO 6  min_max([5,5,5]) == (5,5)", min_max([5, 5, 5]) == (5, 5))

# Part E
check("TODO 7  count_evens([1..6]) == 3", count_evens([1, 2, 3, 4, 5, 6]) == 3)
check("TODO 7  count_evens([1,3,5]) == 0", count_evens([1, 3, 5]) == 0)

# Part F
check("TODO 8  first_negative 找到 -3",
      first_negative([1, 2, -3, 4]) == -3)
check("TODO 8  first_negative 无负数返回 None（且能找到 -3）",
      first_negative([1, 2, -3, 4]) == -3 and first_negative([1, 2, 3]) is None)

passed = sum(1 for _, ok in checks if ok)
for name, ok in checks:
    print(f"  {'[OK]  ' if ok else '[TODO]'} {name}")

print(f"\n通过 {passed} / {len(checks)}")

if passed == len(checks):
    print("\n全部通过。函数的机制你已经掌握了。")
    print("下一步：F2_函数分解.py —— 学'怎么把一个需求拆成几个函数'。")
elif passed >= len(checks) - 4:
    print("\n很接近了。把剩下的 TODO 补完。")
else:
    print("\n还有不少没完成。别急，这部分本来就是新东西。")
    print("哪个 TODO 卡住了，把编号和报错发我。")

if passed < len(checks):
    print()
    print("-" * 58)
    print("💡 改了代码但分数没变？→ 先按 Ctrl+S 保存，再重新运行。")
    print("   编辑器里的改动只存在内存里；这个判分器读的是磁盘上的文件。")
    print("   VS Code 里文件标签上有个 ● 圆点 = 还有未保存的改动。")
    print("-" * 58)
