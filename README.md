# daily.py — 一句话日记工具

> DEEP 营第二期必做 006：真实需求验证 — 从模糊一句话到可交付的最小契约

## 需求方

戴昊杰（自己）— "帮我把每天做了什么用一句话总结，存到一个文件里，下次能快速翻看"

## 运行入口

```bash
# 追加日志
python daily.py add "完成了DEEP营004任务"

# 查看最近10条
python daily.py list

# 只看今天的
python daily.py today

# 搜索历史
python daily.py search "DEEP营"
```

## 最小可运行

- **零依赖** — Python 标准库
- **零配置** — 首次运行自动创建 `~/.daily_log.md`
- **人类可读** — Markdown 格式，任何编辑器打开

## 样例输入输出

```
$ python daily.py add "完成了005数据分析项目"
📝 已记录: [2026-07-25 23:35] 完成了005数据分析项目

$ python daily.py list
📋 最近 3 条日志:
  🌟 [2026-07-25 23:35] 完成了005数据分析项目...
  🌟 [2026-07-25 23:35] 用Claude Code生成了deep_patrol...
  🌟 [2026-07-25 23:35] 检查DEEP营第二期任务...
```

## 为什么这么简单

这不是一个功能完整的日志系统。这是需求验证——用最少的代码验证一个假设：**"这个需求到底成不成立？"**

验证结果见 [need_verdict.md](./need_verdict.md)：需求成立。

---

*Built with Claude Code Plan Mode — 2026-07-25*
