#!/usr/bin/env python3
"""
从自然语言提示词生成结构化 JSON 参数（启发式规则，可替换为 LLM 调用）。
输出写入同目录下的 params.json，供 fetch_stub 或你的 API 客户端使用。
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def parse_prompt(text: str) -> dict:
    text = text.strip()
    params: dict = {
        "keywords": [],
        "limit": 10,
        "sort": "latest",
        "time_range": None,
        "content_type": "note",
        "fields": ["title", "excerpt", "author"],
    }

    # 条数：N 条 / 前 N 条 / 找 N
    m = re.search(r"(\d+)\s*条", text)
    if m:
        params["limit"] = min(int(m.group(1)), 50)

    # 简单关键词：关于 XXX / 关键词 XXX
    for pat in (r"关于\s*([^\s，,。]+)", r"关键词\s*([^\s，,。]+)"):
        found = re.findall(pat, text)
        params["keywords"].extend(found)

    if not params["keywords"] and len(text) < 80:
        params["keywords"] = [text]

    # 排序
    if re.search(r"爆款|最热|热门", text):
        params["sort"] = "hot"
    if re.search(r"最新|按时间", text):
        params["sort"] = "latest"

    # 时间
    if re.search(r"一周|7\s*天", text):
        params["time_range"] = "last_7_days"
    if re.search(r"一月|30\s*天", text):
        params["time_range"] = "last_30_days"

    # 内容类型
    if re.search(r"视频", text):
        params["content_type"] = "video"

    return params


def main() -> None:
    prompt = " ".join(sys.argv[1:]).strip() if len(sys.argv) > 1 else ""
    if not prompt:
        print("用法: python prompt_to_params.py <提示词>", file=sys.stderr)
        sys.exit(1)

    out = parse_prompt(prompt)
    path = Path(__file__).resolve().parent / "params.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"\n已写入: {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
