# Codex 本地静态卡片

此入口通过官方 Codex CLI 的 `exec` 使用 ChatGPT 登录，不进入 Deep Agents 模型调用链。
需要支持 `--ignore-user-config`、`--ephemeral`、`--output-schema` 的 Codex CLI、Docker 和 uv。

```bash
uv sync --frozen --all-extras --dev
codex login
uv run design-agent sandbox build
uv run design-agent codex-card '设计一张卡片，文案：设计评审日' --size 1200x627
uv run design-agent codex-card '将标题放大' --thread 上一步输出的线程ID --size 1200x627
```

不读取或复制登录凭据，不修改全局 Codex 配置；仅接受 `codex login status` 报告的
ChatGPT 登录。调用时移除 OPENAI_API_KEY/CODEX_API_KEY，并强制 ChatGPT 登录方式。
额度、模型可用性与限流由 Codex 账号决定，未测量订阅消耗。

每次调用生成独立版本，位于 `workspace/out/codex/<线程>/<版本>/`。
修改以最后一次成功版本的 HTML 为上下文，不依赖 Codex 会话恢复。
默认使用 `workspace/brand`；缺失时明确使用 example-studio 示例品牌。
渲染复用仓库 brand-lint 与 html2png，Docker 断网且不挂载凭据。
检查图片尺寸与非空白；文案准确性、裁切、可读性和品牌一致性需要人工检查。
HTML 是可编辑源文件，引用版本目录内的品牌资料，不能只移动 HTML 而丢弃品牌目录。

首期只提供静态卡片；不接入独立图片生成、语音、Slack、Paper 或后台编排。
执行失败不会更新上一成功源文件，失败版本保留便于排查；错误不会标为交付成功。
本入口尚需在用户电脑进行真实生成、修改及视觉验收。
