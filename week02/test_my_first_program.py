"""
my_first_program.py 自动判分器
==============================
用法（在 week02 目录下）：
    python test_my_first_program.py

它会运行你的 my_first_program.py，逐个检查 4 个函数。
每实现一个就跑一次，看对应的 [OK] 有没有亮。

你不需要修改本文件。

判分规则：只有函数"返回了正确的东西"才算通过。
返回 None（还是 pass）、返回错的东西、或者报错 —— 都算未完成。
"""

import io
import sys
import contextlib
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent

# 可以直接传一个路径来判分别的文件（比如参考解）：
#     python test_my_first_program.py solutions/my_first_program_solution.py
if len(sys.argv) > 1:
    TARGET = Path(sys.argv[1])
    if not TARGET.is_absolute():
        TARGET = HERE / TARGET
else:
    TARGET = HERE / "my_first_program.py"

print("=" * 66)
print(f" 判分对象：{TARGET.name}")
print("=" * 66)

if not TARGET.exists():
    print(f"\n❌ 找不到文件：{TARGET}")
    sys.exit(1)

# utf-8-sig 能同时处理「有 BOM」和「无 BOM」两种文件
src = TARGET.read_text(encoding="utf-8-sig")

# ----------------------------------------------------------------------
# 运行学生的程序（把 __name__ 设成 "__main__"，所以 main 块会执行）
# 同时捕获 stdout，这样不会和判分输出混在一起
# ----------------------------------------------------------------------
ns = {"__name__": "__main__", "__file__": str(TARGET)}
buf = io.StringIO()
load_error = None
try:
    with contextlib.redirect_stdout(buf):
        exec(compile(src, str(TARGET), "exec"), ns)
except Exception as e:
    load_error = e
main_output = buf.getvalue()

if load_error is not None:
    print(f"\n⚠️ 运行你的程序时出错了：{type(load_error).__name__}: {load_error}")
    print("   （这不影响下面逐函数判分，但如果 main 里有错要修）")

# ----------------------------------------------------------------------
# 测试数据
# ----------------------------------------------------------------------
DATA = [1 + 2j, 3 - 1j, 0 + 1j, 2 + 0j]
MAGS = [abs(z) for z in DATA]          # [2.236..., 3.162..., 1.0, 2.0]
# 按模长降序应为：3-1j(3.162), 1+2j(2.236), 2+0j(2.0), 0+1j(1.0)
SORTED_DESC = [3 - 1j, 1 + 2j, 2 + 0j, 0 + 1j]


def call(name, *args):
    """安全调用；返回 (是否成功, 结果或错误信息)"""
    fn = ns.get(name)
    if not callable(fn):
        return False, f"没有找到函数 {name}"
    try:
        return True, fn(*args)
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"


def close(a, b, tol=1e-9):
    """数值比较：支持标量、列表、复数列表"""
    try:
        if isinstance(b, list):
            if not isinstance(a, list) or len(a) != len(b):
                return False
            return all(abs(x - y) < tol for x, y in zip(a, b))
        return abs(a - b) < tol
    except Exception:
        return False


checks = []


def check(desc, ok):
    checks.append((desc, bool(ok)))


# ---------- abs_list ----------
ok, r = call("abs_list", DATA)
check("① abs_list(data) 返回正确的模长列表", ok and close(r, MAGS))
check("① abs_list 返回的是 list（不是 numpy 数组也别急，但要是序列）",
      ok and isinstance(r, list))
ok2, r2 = call("abs_list", [])
check("① abs_list([]) 返回空列表", ok2 and isinstance(r2, list) and len(r2) == 0)
ok3, r3 = call("abs_list", [3 + 4j])
check("① abs_list([3+4j]) == [5.0]（勾股数，好验算）", ok3 and close(r3, [5.0]))

# ---------- argmax ----------
ok, r = call("argmax", [1, 5, 3])
check("② argmax([1,5,3]) == 1", ok and r == 1)
ok, r = call("argmax", [9, 1, 2])
check("② argmax([9,1,2]) == 0（最大值在开头，别漏了）", ok and r == 0)
ok, r = call("argmax", [1, 2, 9])
check("② argmax([1,2,9]) == 2（最大值在末尾）", ok and r == 2)
ok, r = call("argmax", MAGS)
check("② argmax(模长列表) == 1（对应 3-1j）", ok and r == 1)

# ---------- total ----------
ok, r = call("total", [1, 2, 3])
check("③ total([1,2,3]) == 6", ok and r == 6)
ok, r = call("total", [])
check("③ total([]) == 0（空列表不能崩）", ok and r == 0)
ok, r = call("total", MAGS)
check("③ total(模长列表) == 各模长之和", ok and close(r, sum(MAGS)))

# ---------- sort_desc ----------
ok, r = call("sort_desc", DATA)
check("④ sort_desc(data) 按模长降序正确", ok and close(r, SORTED_DESC))
check("④ sort_desc 返回的是新列表（长度一致）",
      ok and isinstance(r, list) and len(r) == 4)
# 关键检查：有没有偷偷改掉原列表
# ⚠️ 必须同时要求「结果正确」。否则函数没实现时（返回 None、自然没改任何东西），
#    这条会误判成通过 —— 这正是我第一版犯的错。
_orig = [1 + 2j, 3 - 1j, 0 + 1j, 2 + 0j]
ok, _r = call("sort_desc", _orig)
check("④ sort_desc 没有修改传入的原列表（副作用检查）",
      ok and close(_r, SORTED_DESC)
      and _orig == [1 + 2j, 3 - 1j, 0 + 1j, 2 + 0j])

# ---------- main 输出 ----------
out_lines = [ln for ln in main_output.splitlines() if ln.strip()]
check("⑤ main 至少打印了 4 行结果", len(out_lines) >= 4)

# ----------------------------------------------------------------------
# 汇报
# ----------------------------------------------------------------------
print()
for desc, ok in checks:
    print(f"  {'[OK]  ' if ok else '[TODO]'} {desc}")

passed = sum(1 for _, ok in checks if ok)
total_n = len(checks)
print(f"\n通过 {passed} / {total_n}")

# 分组统计，告诉他还差哪一块
groups = {
    "① abs_list": [c for c in checks if c[0].startswith("①")],
    "② argmax":   [c for c in checks if c[0].startswith("②")],
    "③ total":    [c for c in checks if c[0].startswith("③")],
    "④ sort_desc": [c for c in checks if c[0].startswith("④")],
    "⑤ main 输出": [c for c in checks if c[0].startswith("⑤")],
}
print("\n分块进度：")
for g, items in groups.items():
    done = sum(1 for _, ok in items if ok)
    bar = "█" * done + "░" * (len(items) - done)
    print(f"  {g:<14} {bar}  {done}/{len(items)}")

print()
if passed == total_n:
    print("全部通过。你的 my_first_program.py 完成了。")
    print()
    print("接下来：")
    print("  1) git add -A && git commit -m \"week02: 完成第一个完整程序\"")
    print("  2) 回到 F1 / F2（如果还没做）——它们练的是更系统的函数能力")
elif passed >= total_n - 3:
    print("很接近了。把剩下的补完。")
else:
    print("还有不少没完成。建议一次只攻一个函数，别贪多。")
    print()
    print("先看 ① abs_list 这一组。参考 F1 的 Part E（count_evens 那道题）。")
    print("卡住就把报错发我，格式：我想做 X，试了 Y，报错 Z。")
