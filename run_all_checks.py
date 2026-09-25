#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
进度总览 —— 一条命令看到所有练习的完成度
==========================================
用法（在 quantum-journey 目录下）：
    python run_all_checks.py            # 跑全部
    python run_all_checks.py F1         # 只跑名字里含 "F1" 的
    python run_all_checks.py week01     # 只跑 week01 下的

它把每个练习当成独立进程跑一遍，解析出 "通过 N / M"，
然后汇总成一张表。已经通过的练习也用绿色标出来，方便你直接看还差什么。
"""
import re
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
PY = sys.executable

# (相对路径, 显示名)
# ⚠️ 顺序 = 推荐完成顺序。ex1/ex2 排在最后，因为它们是为 S2 线代部分做铺垫的
#    「稍后项」，当前主线是 W2 的函数三件套。
TARGETS = [
    ("week01/ex0_matlab_to_python.py",      "W1 · MATLAB→Python 对照"),
    ("week02/F1_函数基础.py",                "W2 · ① F1 函数基础"),
    ("week02/F2_函数分解.py",                "W2 · ② F2 函数分解"),
    ("week02/test_my_first_program.py",     "W2 · ③ 第一个完整程序"),
    ("week01/ex1_complex_and_vectors.py",   "W1 · 复数与态矢（稍后）"),
    ("week01/ex2_gate_matrices.py",         "W1 · 量子门矩阵（稍后）"),
]

RESULT_RE = re.compile(r"通过\s*(\d+)\s*/\s*(\d+)")


def run_one(rel: str):
    """返回 (已通过, 总数, 状态标记, 备注)"""
    path = HERE / rel
    if not path.exists():
        return 0, 0, "缺失", "文件不存在"

    try:
        p = subprocess.run(
            [PY, str(path)],
            cwd=str(path.parent),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=300,
        )
    except subprocess.TimeoutExpired:
        return 0, 0, "超时", "运行超过 300 秒"

    out = (p.stdout or "") + (p.stderr or "")
    m = None
    for m in RESULT_RE.finditer(out):
        pass                      # 取最后一个匹配
    if not m:
        # 没解析到结果，多半是报错退出
        tail = [ln for ln in (p.stderr or "").strip().splitlines() if ln.strip()]
        hint = tail[-1][:60] if tail else "无输出"
        return 0, 0, "报错", hint

    got, tot = int(m.group(1)), int(m.group(2))
    if got == tot:
        return got, tot, "完成", ""
    if got == 0:
        return got, tot, "未开始", ""
    return got, tot, "进行中", ""


def bar(done: int, total: int, width: int = 12) -> str:
    if total == 0:
        return "─" * width
    filled = round(width * done / total)
    return "█" * filled + "░" * (width - filled)


def main():
    flt = sys.argv[1] if len(sys.argv) > 1 else ""
    targets = [t for t in TARGETS if not flt or flt.lower() in t[0].lower()]

    if not targets:
        print(f"没有匹配 '{flt}' 的练习")
        return 1

    print("=" * 74)
    print(" 量子信息学习 · 练习进度总览")
    print("=" * 74)

    rows = []
    for rel, name in targets:
        got, tot, status, note = run_one(rel)
        rows.append((name, got, tot, status, note))

    print()
    print(f"  {'练习':<26}{'进度':<18}{'得分':<12}{'状态'}")
    print("  " + "-" * 70)
    for name, got, tot, status, note in rows:
        mark = {"完成": "✅", "进行中": "🟡", "未开始": "⬜",
                "报错": "🔴", "缺失": "⚫", "超时": "⏱"}.get(status, "?")
        score = f"{got}/{tot}" if tot else "—"
        print(f"  {name:<26}{bar(got, tot):<18}{score:<12}{mark} {status}"
              + (f"  ({note})" if note else ""))

    done_n = sum(1 for r in rows if r[3] == "完成")
    got_all = sum(r[1] for r in rows)
    tot_all = sum(r[2] for r in rows)

    print()
    print("  " + "-" * 70)
    print(f"  练习完成数: {done_n} / {len(rows)}")
    if tot_all:
        print(f"  总得分    : {got_all} / {tot_all}   {bar(got_all, tot_all, 30)}"
              f"  {100 * got_all / tot_all:.0f}%")

    # 下一步建议
    print()
    print("  " + "-" * 70)
    nxt = next((r for r in rows if r[3] in ("未开始", "进行中", "报错")), None)
    if nxt is None:
        print("  🎉 全部练习通过。下一步：")
        print("     · commit & push")
        print("     · 开始 S2 的向量部分（vec_lab.py，见 07_S2 逐周计划）")
    else:
        print(f"  ➡️  下一个该做的：{nxt[0]}")
        if nxt[3] == "报错":
            print(f"     ⚠️ 报错了：{nxt[4]}")
        elif nxt[2]:
            print(f"     进度 {nxt[1]}/{nxt[2]}，继续补 TODO")
        else:
            print("     还没开始")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
