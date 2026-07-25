# Plan Mode 记录

## 使用方式

本任务在 Claude Code 中通过 **Plan Mode** 先行设计，再实施。

## Plan Mode 流程

### Step 1: 需求分析

**Prompt:** "006需求方自己对自己说：帮我把每天做了什么用一句话总结，存到一个文件里。分析这个需求。"

**输出：** 需求真实——用户确实每天在多任务场景下工作（DEEP营、开发、学习），但缺乏固定记录习惯。当前状态是"有时记在聊天记录里，有时没记"，验证了需求的真实性。

### Step 2: 规格设计

**Prompt:** "设计 spec.md。明确用户、输入、输出、约束和非目标。"

**输出：** 约束包括：纯文本存储、零外部依赖、CLI 接口、Markdown 格式。非目标包括：GUI、手机端、数据库、标签系统。这些约束直接来自 need_raw.md 的 3 轮对话。

### Step 3: 方案对比

**Prompt:** "对比至少3种实现方案。"

**输出：** 4 种方案对比：
- A (Markdown+CLI) — 选定
- B (SQLite) — 过度设计
- C (JSON) — 可读性差
- D (云服务) — 违反本地约束

### Step 4: 实施

**Prompt:** "基于 spec.md 和 acceptance.md，生成 daily.py。"

**Claude Code Plan Mode 记录：**
```
Plan file: C:\Users\26414\.claude\plans\glittery-floating-castle.md
  - 006任务拆解: need_raw → spec → acceptance → Plan Mode → 最小交付 → 试用 → 判断
  - 需求方: 用户自己
  - 核心: '帮我把每天做了什么用一句话总结，存到一个文件里，下次能快速翻看'
```

## Plan Mode 截图证据

由于 Plan Mode 在对话中运行（非独立截图），以下是关键决策点：

1. **需求澄清阶段** — 确认了需求方自己、使用场景、边界
2. **方案对比阶段** — 4 选 1，选了 Markdown + CLI
3. **实施阶段** — 生成 daily.py（120 行，Python 标准库）

---

*Plan Mode 使用的核心理念：先设计（spec/acccceptance）再写代码，拒绝模糊需求直接开撸。*
