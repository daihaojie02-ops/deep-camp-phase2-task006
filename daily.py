#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
daily.py — 一句话日记工具

把你的日常一句话总结存到本地日志文件，随时翻看。
最小化设计：一个命令一行日志，不依赖数据库。

Usage:
  python daily.py add "今天做了什么"          # 追加一条日志
  python daily.py list                         # 查看最近 10 条
  python daily.py list -n 20                   # 查看最近 20 条
  python daily.py today                        # 查看今天的日志
  python daily.py search "关键词"               # 搜索历史日志
  python daily.py --help                       # 帮助
"""

import sys
import os
import argparse
from datetime import datetime, timezone, timedelta
from pathlib import Path

CST = timezone(timedelta(hours=8))

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LOG_FILE = Path.home() / '.daily_log.md'


def ensure_file():
    """Create log file with header if it doesn't exist."""
    if not LOG_FILE.exists():
        LOG_FILE.write_text(
            "# 📝 每日工作日志\n\n"
            f"> 创建于 {datetime.now(CST).strftime('%Y-%m-%d %H:%M')}\n"
            "> 格式：`- [日期 时间] 内容`\n\n",
            encoding='utf-8'
        )


def cmd_add(entry):
    """Append a log entry."""
    ensure_file()
    now = datetime.now(CST)
    line = f"- [{now.strftime('%Y-%m-%d %H:%M')}] {entry}\n"

    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(line)

    print(f"📝 已记录: [{now.strftime('%Y-%m-%d %H:%M')}] {entry}")
    print(f"   日志文件: {LOG_FILE}")


def cmd_list(n=10):
    """Show recent entries."""
    ensure_file()
    lines = LOG_FILE.read_text(encoding='utf-8').split('\n')

    entries = [l for l in lines if l.startswith('- [')]
    if not entries:
        print("📭 还没有日志记录。运行 `python daily.py add \"今天做了什么\"` 开始记录。")
        return

    recent = entries[-n:]
    today = datetime.now(CST).strftime('%Y-%m-%d')

    print(f"\n📋 最近 {len(recent)} 条日志:\n")
    for e in reversed(recent):
        # Highlight today's entries
        if today in e:
            print(f"  🌟 {e[2:]}")
        else:
            print(f"  {e[2:]}")
    print(f"\n━━━ 共 {len(entries)} 条记录 ━━━ 日志文件: {LOG_FILE}")


def cmd_today():
    """Show today's entries only."""
    ensure_file()
    lines = LOG_FILE.read_text(encoding='utf-8').split('\n')
    today = datetime.now(CST).strftime('%Y-%m-%d')

    entries = [l for l in lines if l.startswith('- [') and today in l]
    if not entries:
        print(f"📭 今天 ({today}) 还没有日志记录。")
        return

    print(f"\n📋 今天 ({today}) 的日志:\n")
    for e in entries:
        print(f"  {e[2:]}")
    print(f"\n共 {len(entries)} 条")


def cmd_search(keyword):
    """Search entries by keyword."""
    ensure_file()
    lines = LOG_FILE.read_text(encoding='utf-8').split('\n')
    matches = [l for l in lines if l.startswith('- [') and keyword.lower() in l.lower()]

    if not matches:
        print(f"🔍 没有找到包含 \"{keyword}\" 的日志。")
        return

    print(f"\n🔍 搜索 \"{keyword}\" — {len(matches)} 条结果:\n")
    for m in reversed(matches):
        print(f"  {m[2:]}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="daily.py — 一句话日记工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python daily.py add "完成了DEEP营004任务，推了GitHub"
  python daily.py list
  python daily.py list -n 5
  python daily.py today
  python daily.py search "DEEP营"
        """
    )
    sub = parser.add_subparsers(dest='cmd', help='命令')

    p_add = sub.add_parser('add', help='追加一条日志')
    p_add.add_argument('entry', help='日志内容（一句话）')

    p_list = sub.add_parser('list', help='查看最近日志')
    p_list.add_argument('-n', type=int, default=10, help='显示条数（默认10）')

    sub.add_parser('today', help='查看今天的日志')

    p_search = sub.add_parser('search', help='搜索日志')
    p_search.add_argument('keyword', help='搜索关键词')

    args = parser.parse_args()

    if args.cmd == 'add':
        cmd_add(args.entry)
    elif args.cmd == 'list':
        cmd_list(args.n)
    elif args.cmd == 'today':
        cmd_today()
    elif args.cmd == 'search':
        cmd_search(args.keyword)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
