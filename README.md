# lppoyzhou-skills

存放可在 Cursor 中使用的 Agent Skills 与配套脚本。

## 目录说明

| 路径 | 说明 |
|------|------|
| `.cursor/skills/xiaohongshu-content-fetch/` | Cursor 项目 Skill：`SKILL.md`、`reference.md`、`examples.md` |
| `xiaohongshu-content-fetch/` | 提示词解析与占位拉取脚本（Python） |

## 使用 Cursor Skill

用 Cursor 打开本仓库后，Agent 会根据 `SKILL.md` 里的 `description` 在讨论小红书/笔记拉取等话题时选用该 Skill。

## 合规提示

小红书内容拉取 Skill 强调通过**官方开放平台**或**已授权**方式访问数据，不包含绕过登录或违规爬取的实现。
