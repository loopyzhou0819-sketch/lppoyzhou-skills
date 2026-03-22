#!/usr/bin/env python3
"""
占位拉取脚本：读取 params.json，检查环境变量。
在获得官方 API 文档后，在此文件中实现真实 HTTP 请求与响应解析。
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path


def main() -> None:
    base = Path(__file__).resolve().parent
    params_path = base / "params.json"
    if not params_path.exists():
        print("请先运行: python prompt_to_params.py \"你的提示词\"", file=sys.stderr)
        sys.exit(1)

    params = json.loads(params_path.read_text(encoding="utf-8"))
    app_id = os.environ.get("XHS_APP_ID")
    api_base = os.environ.get("XHS_API_BASE")

    print("当前参数:", json.dumps(params, ensure_ascii=False, indent=2))
    print("\n环境检查:")
    print(f"  XHS_APP_ID:     {'已设置' if app_id else '未设置'}")
    print(f"  XHS_API_BASE:   {api_base or '未设置'}")

    if not api_base:
        print(
            "\n未配置 XHS_API_BASE：请在对接小红书开放平台后设置该变量，"
            "并在此脚本中实现鉴权与请求逻辑。",
            file=sys.stderr,
        )
        sys.exit(0)

    # TODO: import requests; 按官方文档发起请求并打印/保存结果
    print("\n（占位）已具备 API 基址，请在此实现具体请求。")


if __name__ == "__main__":
    main()
