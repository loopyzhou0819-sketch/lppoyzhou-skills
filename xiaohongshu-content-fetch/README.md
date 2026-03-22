# xiaohongshu-content-fetch

根据自然语言提示词生成结构化拉取参数；真实数据需接入**小红书开放平台**或你方已授权接口（本仓库不含绕过鉴权的实现）。

## 目录结构

```
xiaohongshu-content-fetch/
├── README.md
├── requirements.txt
└── scripts/
    ├── prompt_to_params.py   # 提示词 → params.json
    └── fetch_stub.py         # 占位：读取 params + 环境变量（可扩展为真实请求）
```

## Cursor Skill

项目内 Skill 路径：`.cursor/skills/xiaohongshu-content-fetch/SKILL.md`  
在 Cursor 中打开本仓库后，Agent 可按描述自动选用该 Skill。

## 使用

```bash
cd xiaohongshu-content-fetch
pip install -r requirements.txt
python scripts/prompt_to_params.py "找5条关于护肤的最新笔记"
# 生成 params.json 后，可自行在 fetch_stub.py 中接入官方 API
python scripts/fetch_stub.py
```

## 合规

仅通过合法 API 或授权数据源访问内容；勿将密钥提交到版本库。
