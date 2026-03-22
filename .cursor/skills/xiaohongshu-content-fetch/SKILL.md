---
name: xiaohongshu-content-fetch
description: Turns natural-language prompts into structured fetch parameters and coordinates retrieval of Xiaohongshu (小红书) public content via official or user-authorized APIs. Use when the user mentions 小红书, 小红薯, 笔记, 拉取笔记, 根据提示词获取内容, or Xiaohongshu content fetch.
---

# 小红书内容拉取（提示词驱动）

## 目标

根据用户的**自然语言提示词**，产出可执行的**结构化参数**（关键词、数量、排序、时间范围等），并在具备合法凭证时通过**官方或已授权接口**获取内容；禁止协助绕过登录、破解接口或违反平台服务条款的大规模爬取。

## 工作流程

1. **解析提示词**  
   从用户描述中提取：`keywords`（主题/话题）、`limit`（条数）、`sort`（最新/最热等，若 API 支持）、`time_range`（可选）、`content_type`（笔记/视频等，若可区分）。

2. **确认数据来源**  
   - **首选**：小红书开放平台 / 企业合作提供的合法 API 与密钥。  
   - **用户自有数据**：导出文件、已授权的 MCP 或内部系统。  
   - **未授权抓取**：仅说明风险与合规要求，不提供具体规避手段。

3. **输出约定**  
   - 先给出 **JSON 参数草案**（见 [examples.md](examples.md)）。  
   - 若项目内存在脚本：可建议运行 `python scripts/prompt_to_params.py "用户原话"` 生成参数文件。  
   - 实际 HTTP 调用需用户配置环境变量与端点（见 [reference.md](reference.md)）。

4. **结果呈现**  
   将每条内容整理为：`title`、`author`、`url`（若有）、`published_at`（若有）、`summary`/`excerpt`、`tags`（若有），避免泄露他人隐私字段。

## 合规与边界

- 遵守 [小红书用户协议](https://www.xiaohongshu.com/terms) 与开放平台规则。  
- 不生成：自动登录脚本、验证码绕过、签名逆向、批量无授权抓取教程。  
- 对「只想输入链接就扒全文」类需求：引导使用官方分享/开放平台能力，或说明需权利方授权。

## 项目内资源

| 路径 | 说明 |
|------|------|
| [reference.md](reference.md) | 开放平台入口、环境变量、接口占位说明 |
| [examples.md](examples.md) | 提示词 → 参数 JSON 示例 |
| `../../../xiaohongshu-content-fetch/scripts/` | 提示词解析与占位拉取脚本（仓库根下独立代码目录） |

## 快速检查清单

- [ ] 提示词已转为结构化参数  
- [ ] 已明确使用官方 API 或用户授权数据源  
- [ ] 输出不含需保密的 token 或 Cookie  
- [ ] 未提供违反 ToS 的抓取实现  
