"""
Week 1 · 环境自检脚本
=====================
用途：确认你的 Python 工具链是否就绪，并打印出后续要用的关键信息。
运行：python check_env.py
不需要修改任何代码，直接跑。
"""

import importlib
import platform
import sys

# Windows 控制台兼容：强制 UTF-8 输出，避免 GBK 编码报错
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

OK = "[OK]  "
MISS = "[MISS]"
WARN = "[WARN]"

print("=" * 62)
print(" Week 1 环境自检 · 量子信息学习工作区")
print("=" * 62)

# ---------- 1. 解释器 ----------
print("\n--- 1. 解释器 ---")
print(f"Python  : {sys.version.split()[0]}")
print(f"路径    : {sys.executable}")
print(f"系统    : {platform.system()} {platform.release()} ({platform.machine()})")

major, minor = sys.version_info[:2]
if (major, minor) >= (3, 14):
    print(f"{WARN} Python {major}.{minor} 过新：Qiskit / QuTiP / PennyLane 目前无兼容版本。")
    print(f"       请使用 conda 环境 qinfo（Python 3.12）跑量子框架的代码。")
elif (major, minor) == (3, 12):
    print(f"{OK} Python 3.12 —— 量子框架的推荐版本。")
else:
    print(f"{WARN} Python {major}.{minor}：多数框架可用，3.12 最稳妥。")

# ---------- 2. 科学计算基础（第一周就需要） ----------
print("\n--- 2. 科学计算基础（第一周就要用）---")
base_pkgs = ["numpy", "scipy", "matplotlib", "pandas", "sympy"]
base_missing = []
for name in base_pkgs:
    try:
        mod = importlib.import_module(name)
        print(f"{OK} {name:<12} {getattr(mod, '__version__', '?')}")
    except Exception:
        base_missing.append(name)
        print(f"{MISS} {name:<12} 未安装")

# ---------- 3. 开发工具 ----------
print("\n--- 3. 开发工具 ---")
dev_pkgs = ["pytest", "jupyter"]
for name in dev_pkgs:
    try:
        mod = importlib.import_module(name)
        print(f"{OK} {name:<12} {getattr(mod, '__version__', '?')}")
    except Exception:
        print(f"{MISS} {name:<12} 未安装（可选）")

# ---------- 4. 量子框架（Phase 1 后期 ~ Phase 2 才需要） ----------
print("\n--- 4. 量子框架（中期才需要，现在缺了不影响）---")
q_pkgs = ["qiskit", "qutip", "pennylane", "cirq"]
q_found = 0
for name in q_pkgs:
    try:
        mod = importlib.import_module(name)
        q_found += 1
        print(f"{OK} {name:<12} {getattr(mod, '__version__', '?')}")
    except Exception:
        print(f"{MISS} {name:<12} 未安装")

if q_found == 0:
    print(f"{WARN} 一个都没装。这是正常的——第一周不需要量子框架，")
    print(f"       先用纯 numpy 理解原理（这正是 ex1/ex2 的目的）。")

# ---------- 5. 结论 ----------
print("\n" + "=" * 62)
print(" 结论")
print("=" * 62)

if base_missing:
    print(f"\n[!] 缺少基础包：{', '.join(base_missing)}")
    print("    安装命令（用清华镜像加速）：")
    print(f"    python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple {' '.join(base_missing)}")
else:
    print(f"\n{OK} 基础科学计算栈就绪，可以立刻开始 ex1 / ex2。")

print("\n下一步：")
print("  1) 跑通本脚本，把输出保存下来（这是第一周的产物之一）")
print("  2) 去做 00_起点诊断测试.md（闭卷，90 分钟）")
print("  3) 打开 ex1_complex_and_vectors.py，按 TODO 补全代码")
print()
