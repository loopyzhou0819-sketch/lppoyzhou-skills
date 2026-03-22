# 提示词 → 结构化参数示例

## 示例 1

**用户提示词：**  
「帮我找 10 条最近一周关于露营的爆款笔记标题和摘要」

**建议参数 JSON：**

```json
{
  "keywords": ["露营"],
  "limit": 10,
  "time_range": "last_7_days",
  "sort": "hot",
  "fields": ["title", "excerpt"]
}
```

## 示例 2

**用户提示词：**  
「按关键词 咖啡探店 上海，只要前 5 条，按最新排序」

**建议参数 JSON：**

```json
{
  "keywords": ["咖啡探店", "上海"],
  "limit": 5,
  "sort": "latest",
  "fields": ["title", "author", "url", "published_at"]
}
```

## 示例 3

**用户提示词：**  
「不限主题，给我 3 条视频笔记的链接」

**建议参数 JSON：**

```json
{
  "keywords": [],
  "limit": 3,
  "content_type": "video",
  "fields": ["url", "title"]
}
```

Agent 应根据实际可用 API 删减或重命名字段（例如官方仅支持部分筛选项）。
