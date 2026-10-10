# AGENTS.md

本文件为在本仓库中工作的 AI 助手提供项目约定。修改后请提交，团队共享。

## 项目概览

- **用途**：Python 学习 / 练习项目。
- **依赖管理**：`uv`（`pyproject.toml` 声明依赖，`uv.lock` 锁定版本）。
- **Python 版本**：见 `.python-version`（当前 3.14），要求 `>=3.14`。

## 常用命令

```powershell
uv sync              # 按 uv.lock 创建/同步 .venv（克隆后第一步）
uv run main.py       # 在项目环境中运行入口脚本
uv add <包名>        # 新增依赖（同时更新 pyproject.toml 和 uv.lock）
uv lock --upgrade    # 升级并重新锁定依赖
```

> 不要用全局 `python`/`pip` 直接跑，统一走 `uv run` / `uv add`。

## 代码约定

- **缩进**：4 个空格（见 `.editorconfig`）。
- **编码**：UTF-8，**无 BOM**。
- **换行符**：统一 **LF**（由 `.gitattributes` 强制；`.bat`/`.cmd` 例外，保留 CRLF）。
- **中文注释**：允许且欢迎，UTF-8 下不受换行符转换影响。
- 新增依赖必须通过 `uv add`，并同时提交 `pyproject.toml` 与 `uv.lock`。

## 目录结构

- `main.py` —— 入口脚本。
- `Learn Function.py` —— 练习用脚本。
- `.venv/`、`.idea/` —— 本地产物，**不要提交**。

## 版本管理

- 已忽略：`.venv/`、`.idea/`、`__pycache__/`、`build/`、`dist/` 等。
- 提交信息用简洁的祈使句说明「改了什么」（如 `Add retry logic to main`）。
- 不要提交凭据、令牌或本地绝对路径配置。

## 验证

- 改动后运行 `uv run main.py`，确认脚本可正常执行且无报错。
- 目前没有自动化测试；如新增测试，请同时补充运行方式到本文件。
